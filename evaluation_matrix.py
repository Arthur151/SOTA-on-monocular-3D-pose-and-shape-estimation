import torch
import numpy as np

def mpjpe(predicted, target):
    """
    Mean per-joint position error (i.e. mean Euclidean distance),
    often referred to as "Protocol #1" in many papers.
    """
    assert predicted.shape == target.shape
    return torch.mean(torch.norm(predicted - target, dim=len(target.shape)-1))

def weighted_mpjpe(predicted, target, w):
    """
    Weighted mean per-joint position error (i.e. mean Euclidean distance)
    """
    assert predicted.shape == target.shape
    assert w.shape[0] == predicted.shape[0]
    return torch.mean(w * torch.norm(predicted - target, dim=len(target.shape)-1))

def p_mpjpe_torch(predicted, target, with_sRt=False,full_torch=False,with_aligned=False):
    """
    Pose error: MPJPE after rigid alignment (scale, rotation, and translation),
    often referred to as "Protocol #2" in many papers.
    """
    assert predicted.shape == target.shape

    muX = torch.mean(target, dim=1, keepdim=True)
    muY = torch.mean(predicted, dim=1, keepdim=True)
    #print(predicted, target)

    X0 = target - muX
    Y0 = predicted - muY
    X0[X0**2<1e-6]=1e-3
    '''
    print(X0)
    if (X0**2<1e-10).sum()>0 or (X0**2>1e10).sum()>0:
        print('Error !')
        print(X0[X0**2<1e-10],X0[X0**2>1e10])
        print(predicted[X0**2<1e-10],predicted[X0**2>1e10])
        return torch.tensor(1.),(torch.ones(3).cuda(),torch.ones((3,3)).cuda(),torch.ones(3).cuda())
    '''
    normX = torch.sqrt(torch.sum(X0**2, dim=(1, 2), keepdim=True))
    normY = torch.sqrt(torch.sum(Y0**2, dim=(1, 2), keepdim=True))

    normX[normX<1e-3]=1e-3

    X0 /= normX
    Y0 /= normY

    H = torch.matmul(X0.transpose(1,2), Y0)
    if full_torch:
        U, s, V = batch_svd(H)
    else:
        U, s, Vt = np.linalg.svd(H.cpu().numpy())
        V = torch.from_numpy(Vt.transpose(0, 2, 1)).cuda()
        U = torch.from_numpy(U).cuda()
        s = torch.from_numpy(s).cuda()

    #U, s, V = U.unsqueeze(0), s.unsqueeze(0), V.unsqueeze(0)
    #V = Vt.transpose(2, 1)
    R = torch.matmul(V, U.transpose(2, 1))

    # Avoid improper rotations (reflections), i.e. rotations with det(R) = -1
    sign_detR = torch.sign(torch.unsqueeze(torch.det(R[0]), 0))
    V[:, :, -1] *= sign_detR.unsqueeze(0)
    s[:, -1] *= sign_detR.flatten()
    R = torch.matmul(V, U.transpose(2, 1)) # Rotation

    tr = torch.unsqueeze(torch.sum(s, dim=1, keepdim=True), 2)

    a = tr * normX / normY # Scale
    t = muX - a*torch.matmul(muY, R) # Translation

    #避免出现nan：

    if (a!=a).sum()>0:

        print('NaN Error!!')
        print('UsV:',U,s,V)
        print('aRt:',a,R,t)
    a[a!=a]=1.
    R[R!=R]=0.
    t[t!=t]=0.
    # Perform rigid transformation on the input
    predicted_aligned = a*torch.matmul(predicted, R) + t
    if with_sRt:
        return torch.sqrt(((predicted_aligned - target)**2).sum(-1)).mean(),(a,R,t)#torch.mean(torch.norm(predicted_aligned - target, dim=len(target.shape)-1))
    if with_aligned:
        return torch.sqrt(((predicted_aligned - target)**2).sum(-1)).mean(),predicted_aligned
    # Return MPJPE
    return torch.sqrt(((predicted_aligned - target)**2).sum(-1)).mean()#torch.mean(torch.norm(predicted_aligned - target, dim=len(target.shape)-1))#,(a,R,t),predicted_aligned


def batch_svd(H):
    num = H.shape[0]
    U_batch, s_batch, V_batch = [],[],[]
    for i in range(num):
        U, s, V = H[i].svd(some=False)
        U_batch.append(U.unsqueeze(0))
        s_batch.append(s.unsqueeze(0))
        V_batch.append(V.unsqueeze(0))
    return torch.cat(U_batch,0),torch.cat(s_batch,0),torch.cat(V_batch,0)

def p_mpjpe(predicted, target, with_sRt=False,full_torch=False,with_aligned=False,each_separate=False):
    """
    Pose error: MPJPE after rigid alignment (scale, rotation, and translation),
    often referred to as "Protocol #2" in many papers.
    """
    assert predicted.shape == target.shape

    muX = np.mean(target, axis=1, keepdims=True)
    muY = np.mean(predicted, axis=1, keepdims=True)

    X0 = target - muX
    Y0 = predicted - muY
    '''
    if (X0**2<1e-10).sum()>0 or (X0**2>1e10).sum()>0:
        print('Error !')
        print(X0[X0**2<1e-10],X0[X0**2>1e10])
        print(predicted[X0**2<1e-10],predicted[X0**2>1e10])
        return 1.,(np.ones(3),np.ones((3,3)),np.ones(3))
    '''
    normX = np.sqrt(np.sum(X0**2, axis=(1, 2), keepdims=True))
    normY = np.sqrt(np.sum(Y0**2, axis=(1, 2), keepdims=True))

    X0 /= (normX+1e-6)
    Y0 /= (normY+1e-6)


    H = np.matmul(X0.transpose(0, 2, 1), Y0).astype(np.float16).astype(np.float64)
    U, s, Vt = np.linalg.svd(H)
    V = Vt.transpose(0, 2, 1)
    R = np.matmul(V, U.transpose(0, 2, 1))

    # Avoid improper rotations (reflections), i.e. rotations with det(R) = -1
    sign_detR = np.sign(np.expand_dims(np.linalg.det(R), axis=1))
    V[:, :, -1] *= sign_detR
    s[:, -1] *= sign_detR.flatten()
    R = np.matmul(V, U.transpose(0, 2, 1)) # Rotation

    tr = np.expand_dims(np.sum(s, axis=1, keepdims=True), axis=2)

    a = tr * normX / normY # Scale
    t = muX - a*np.matmul(muY, R) # Translation

    # Perform rigid transformation on the input
    predicted_aligned = a*np.matmul(predicted, R) + t
    if each_separate:
        return np.linalg.norm(predicted_aligned - target, axis=len(target.shape)-1)

    error = np.mean(np.linalg.norm(predicted_aligned - target, axis=len(target.shape)-1))
    if with_sRt and not with_aligned:
        return error, (a,R,t)
    if with_aligned:
        return error,(a,R,t),predicted_aligned
    # Return MPJPE
    return error

def n_mpjpe(predicted, target):
    """
    Normalized MPJPE (scale only), adapted from:
    https://github.com/hrhodin/UnsupervisedGeometryAwareRepresentationLearning/blob/master/losses/poses.py
    """
    assert predicted.shape == target.shape

    norm_predicted = torch.mean(torch.sum(predicted**2, dim=3, keepdim=True), dim=2, keepdim=True)
    norm_target = torch.mean(torch.sum(target*predicted, dim=3, keepdim=True), dim=2, keepdim=True)
    scale = norm_target / norm_predicted
    return mpjpe(scale * predicted, target)

def mean_velocity_error(predicted, target):
    """
    Mean per-joint velocity error (i.e. mean Euclidean distance of the 1st derivative)
    """
    assert predicted.shape == target.shape

    velocity_predicted = np.diff(predicted, axis=0)
    velocity_target = np.diff(target, axis=0)

    return np.mean(np.linalg.norm(velocity_predicted - velocity_target, axis=len(target.shape)-1))

def test():
    for i in range(100):
        r1 = np.random.rand(3,14,3)
        r2 = np.random.rand(3,14,3)
        pmpjpe = p_mpjpe(r1, r2,with_sRt=False)
        pmpjpe_torch = p_mpjpe_torch(torch.from_numpy(r1), torch.from_numpy(r2),with_sRt=False,full_torch=True)
        print('pmpjpe: {}; {:.6f}; {:.6f}; {:.6f}'.format(pmpjpe==pmpjpe_torch.numpy(),pmpjpe,pmpjpe_torch.numpy(), pmpjpe-pmpjpe_torch.numpy()))
        '''
        pmpjpe,(s,R,t),(H,U, s, Vt) = p_mpjpe(r1, r2,with_sRt=True)
        pmpjpe_torch,(s_torch,R_torch,t_torch),(H_torch,U_torch, s_torch, Vt_torch) = p_mpjpe_torch(torch.from_numpy(r1), torch.from_numpy(r2),with_sRt=True,full_torch=True)
        print('s:',s==s_torch.numpy(),s,s_torch.numpy())
        print('R:',R==R_torch.numpy(),R,R_torch.numpy())
        print('t:',t==t_torch.numpy(),t,t_torch.numpy())
        print(H)
        print(H_torch)
        print(U)
        print(U_torch)
        print(Vt)
        print(Vt_torch)
        print(s)
        print(s_torch)
        '''

if __name__ == '__main__':
    test()
