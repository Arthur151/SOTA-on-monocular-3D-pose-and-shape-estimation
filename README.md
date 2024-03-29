# State-of-the-art methods on monocular 3D pose estimation / 3D mesh recovery

Benchmark Leaderboard and state-of-the-art method list on monocular 3D pose estimation / 3D mesh recovery

Feel free to [contribute](#Contribute)!

## Contents
 - [Benchmark Leaderboard](#Benchmark-Leaderboard)
 - [arXiv Papers](#arXiv-Papers)
 - [Conference Papers](#conference-papers)
   - 2020: [CVPR](#2020-CVPR), [ECCV](#2020-ECCV), [Others](#2020-Others)
   - 2019: [CVPR](#2019-CVPR), [ICCV](#2019-ICCV)
   - 2018: [CVPR](#2018-CVPR), [ECCV](#2018-ECCV), [Others](#2018-Others)
   - 2017: [CVPR](#2017-CVPR), [ICCV](#2017-ICCV)
   - 2016: [CVPR](#2016-CVPR), [ECCV](#2016-ECCV)
 - [Journal Papers](#Journal-Papers)
 - [Datasets](#Datasets)
 - [Other Related Papers](#Other-related-papers)

## Benchmark Leaderboard

### Evaluation Matrix

See [``evaluation_matrix.py``](evaluation_matrix.py) in Numpy / Pytorch to get more details on evaluation matrix for 3D pose estimation / mesh recovery. In general, MPJPE and PA-MPJPE are mean 3D joint errors. The lower, the better.

### Comparisons on Human3.6M.

See [``datasets/Human3.6M``](datasets/Human3.6M.md) to get more details on [Human3.6M](http://vision.imar.ro/human3.6m/description.php)

#### State-of-the-art 3D pose estimation methods

| Methods | Publication | MPJPE | PA-MPJPE | link |
| :----: | :----: | :----: | :----: | :----: |
| [OANet](#OANet) |  ICCV19 |  42.9 | 32.8 | [\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Cheng_Occlusion-Aware_Networks_for_3D_Human_Pose_Estimation_in_Video_ICCV_2019_paper.html) |
| [3DMPPE](#3DMPPE) |  ICCV19 | 54.4 | - | [\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Moon_Camera_Distance-Aware_Top-Down_Approach_for_3D_Multi-Person_Pose_Estimation_From_ICCV_2019_paper.html) [\[code\]](https://github.com/mks0601/3DMPPE_ROOTNET_RELEASE) |
| [SemGCN](#SemGCN) |  CVPR19 | 57.6 | - | [\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Zhao_Semantic_Graph_Convolutional_Networks_for_3D_Human_Pose_Regression_CVPR_2019_paper.html) [\[code\]](https://github.com/garyzhao/SemGCN) |
| [VideoPose3D](#VideoPose3D) |  CVPR19 | 46.8 | 36.5 | [\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Pavllo_3D_Human_Pose_Estimation_in_Video_With_Temporal_Convolutions_and_CVPR_2019_paper.html) [\[code\]](https://github.com/facebookresearch/VideoPose3D) |
| [EpipolarPose](#EpipolarPose) |  CVPR19 | 51.8 | 45.0 | [\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Kocabas_Self-Supervised_Learning_of_3D_Human_Pose_Using_Multi-View_Geometry_CVPR_2019_paper.html) [\[code\]](https://github.com/mkocabas/EpipolarPose) |
| [FBN](#FBN) |  TPAMI | 61.1 | - | [\[arxiv\]](https://arxiv.org/abs/1901.04877) |
| [TP-Net](#TP-Net) |  ECCV18 | 58.2 | 44.1 | [\[conf\]](http://openaccess.thecvf.com/content_ECCV_2018/html/Mir_Rayat_Imtiaz_Hossain_Exploiting_temporal_information_ECCV_2018_paper.html) [\[code\]](https://github.com/rayat137/Pose_3D) |
| [IHPR](#IHPR) |  ECCV18 | 64.1 | 49.6 | [\[conf\]](http://openaccess.thecvf.com/content_ECCV_2018/html/Xiao_Sun_Integral_Human_Pose_ECCV_2018_paper.html) [\[code\]](https://github.com/JimmySuen/integral-human-pose) |
| [MVC](#MVC) |  CVPR18 | 66.8 | 51.6 | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Rhodin_Learning_Monocular_3D_CVPR_2018_paper.html) |
| [Deephar](#Deephar) |  CVPR18 | 53.2 | - | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Luvizon_2D3D_Pose_Estimation_CVPR_2018_paper.html) [\[code\]](https://github.com/dluvizon/deephar) |
| [ODS](#ODS) |  CVPR18 | 56.2 | 41.8 | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Pavlakos_Ordinal_Depth_Supervision_CVPR_2018_paper.html) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) |
| [LPG](#LPG-AAAI18) |  AAAI18 | 60.4 | 45.7 | [\[conf\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471) |
| [CHPR](#CHPR) |  ICCV17 | 92.4 | 59.1 | [\[conf\]](http://openaccess.thecvf.com/content_iccv_2017/html/Sun_Compositional_Human_Pose_ICCV_2017_paper.html) |
| [3DPB](#3DPB) |  ICCV17 | 62.9 | 47.7 | [\[conf\]](http://openaccess.thecvf.com/content_iccv_2017/html/Martinez_A_Simple_yet_ICCV_2017_paper.html) [\[code\]](https://github.com/una-dinosauria/3d-pose-baseline) |
| [RPSM](#RPSM) |  CVPR17 | 73.1 | - | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Lin_Recurrent_3D_Pose_CVPR_2017_paper.html) [\[code\]](https://github.com/MudeLin/RPSM) |
| [C2F](#C2F) |  CVPR17 | 71.9 | 51.9 | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Pavlakos_Coarse-To-Fine_Volumetric_Prediction_CVPR_2017_paper.html) [\[code\]](https://github.com/geopavlakos/c2f-vol-demo) |
| [LFD](#LFD) |  CVPR17 | 113.0 | - | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Tome_Lifting_From_the_CVPR_2017_paper.html) [\[code\]](https://github.com/DenisTome/Lifting-from-the-Deep-release) |
| [SMD](#SMD) |  CVPR16 | 88.4 | - | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2016/html/Zhou_Sparseness_Meets_Deepness_CVPR_2016_paper.html) [\[code\]](https://github.com/chuxiaoselena/SparsenessMeetsDeepness) |

#### State-of-the-art 3D mesh recovery methods

See [``datasets/3DPW``](datasets/3DPW.md) to get more details on [3DPW](https://virtualhumans.mpi-inf.mpg.de/3DPW/)

Evaluation Datasets of MPJPE: Human3.6M | Human3.6M | HumanEva-I | 3DPW 
| Methods | Publication | MPJPE | PA-MPJPE | MPJPE | PA-MPJPE | link |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [ROMP](#ROMP) |  ICCV21 | - | - | - | 47.3 | [\[arxiv\]](https://arxiv.org/abs/2008.12272) [\[code\]](https://github.com/Arthur151/ROMP) |
| [VIBE](#VIBE) |  CVPR20 | 65.6 | 41.4 | - | 51.9 | [\[arxiv\]](https://arxiv.org/abs/1912.05656) [\[code\]](https://github.com/mkocabas/VIBE) |
| [DSD-SATN](#DSD-SATN) |  ICCV19 | 59.1 | 42.4 | - | 69.5 | [\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Sun_Human_Mesh_Recovery_From_Monocular_Images_via_a_Skeleton-Disentangled_Representation_ICCV_2019_paper.html) [\[code\]](https://github.com/JDAI-CV/DSD-SATN) |
| [SPIN](#SPIN) |  ICCV19 | - | 41.1 | - | 59.2 | [\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Kolotouros_Learning_to_Reconstruct_3D_Human_Pose_and_Shape_via_Model-Fitting_ICCV_2019_paper.html) [\[code\]](https://github.com/nkolot/SPIN) |
| [Texturepose](#Texturepose) |  ICCV19 | - | 49.7 | - | - | [\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Pavlakos_TexturePose_Supervising_Human_Mesh_Estimation_With_Texture_Consistency_ICCV_2019_paper.html) [\[code\]](https://www.seas.upenn.edu/~pavlakos/projects/texturepose/) |
| [DenseRaC](#DenseRaC) |  ICCV19 | 76.8 | 48.0 | - | - | [\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Xu_DenseRaC_Joint_3D_Pose_and_Shape_Estimation_by_Dense_Render-and-Compare_ICCV_2019_paper.html) |
| [HoloPose](#HoloPose) |  CVPR19 |  60.2 | 46.5 | - | - | [\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Guler_HoloPose_Holistic_3D_Human_Reconstruction_In-The-Wild_CVPR_2019_paper.html) [\[code\]](http://arielai.com/holopose) |
| [GCMR](#GCMR) |  CVPR19 | 71.9 | 50.1 | - | - | [\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Kolotouros_Convolutional_Mesh_Regression_for_Single-Image_Human_Shape_Reconstruction_CVPR_2019_paper.html) [\[code\]](https://github.com/nkolot/GraphCMR) |
| [HMR-video](#HMR-video) |  CVPR19 | - | 56.9 | - | 72.6 | [\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Kanazawa_Learning_3D_Human_Dynamics_From_Video_CVPR_2019_paper.html) [\[code\]](https://github.com/akanazawa/human_dynamics) |
| [HMR](#HMR) |  CVPR18 | 87.9 | 58.1 | - | - | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Kanazawa_End-to-End_Recovery_of_CVPR_2018_paper.html) [\[code\]](https://github.com/akanazawa/hmr) [\[Pytorch\]](https://github.com/MandyMo/pytorch_HMR) |
| [UP](#UP) |  CVPR17 | 80.7 | - | 74.5 | - | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Lassner_Unite_the_People_CVPR_2017_paper.html) [\[code\]](http://up.is.tuebingen.mpg.de/) |
| [SMPLify](#SMPLify) |  ECCV16 | 82.3 | - | 79.9 | - | [\[Paper\]](http://files.is.tue.mpg.de/black/papers/BogoECCV2016.pdf) [\[code\]](http://smplify.is.tue.mpg.de/) |

## Valuable Code

### Differential Renderer

##### NMR CVPR18
**Neural 3D Mesh Renderer**

_Hiroharu Kato, Yoshitaka Ushiku, Tatsuya Harada_
[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Kato_Neural_3D_Mesh_CVPR_2018_paper.html) [\[Project\]](http://hiroharu-kato.com/projects_en/neural_renderer.html) [\[Tensorflow - official\]](https://github.com/hiroharu-kato/neural_renderer) [\[Pytorch\]](https://github.com/daniilidis-group/neural_renderer) 

## Method Zoo

## arXiv Papers

##### [\[2008.12272\]](https://arxiv.org/abs/2008.12272) CenterHMR: a Bottom-up Single-shot Method for Multi-person 3D Mesh Recovery from a Single Image  
_Yu Sun, Qian Bao, Wu Liu, Yili Fu, Tao Mei_

##### [\[2004.13985\]](https://arxiv.org/abs/2004.13985) Motion Guided 3D Pose Estimation from Videos  
_Jingbo Wang, Sijie Yan, Yuanjun Xiong, Dahua Lin_

##### [\[2003.10350\]](https://arxiv.org/abs/2003.10350) Weakly Supervised 3D Human Pose and Shape Reconstruction with Normalizing Flows  
_Andrei Zanfir, Eduard Gabriel Bazavan, Hongyi Xu, Bill Freeman, Rahul Sukthankar, Cristian Sminchisescu_

##### [\[2003.10873\]](https://arxiv.org/abs/2003.10873) EllipBody: A Light-weight and Part-based Representation for Human Pose and Shape Recovery  
_Min Wang, Feng Qiu, Wentao Liu, Chen Qian, Xiaowei Zhou, Lizhuang Ma_

##### [\[2004.01166\]](https://arxiv.org/abs/2004.01166) Bodies at Rest: 3D Human Pose and Shape Estimation from a Pressure Image using Synthetic Data  
_Henry M. Clever, Zackory Erickson, Ariel Kapusta, Greg Turk, C. Karen Liu, Charles C. Kemp_

##### [\[2004.02186\]](https://arxiv.org/abs/2004.02186) Lightweight Multi-View 3D Pose Estimation through Camera-Disentangled Representation  
_Edoardo Remelli, Shangchen Han, Sina Honari, Pascal Fua, Robert Wang_

##### [\[2004.03143\]](https://arxiv.org/abs/2004.03143) Predicting Camera Viewpoint Improves Cross-dataset Generalization for 3D Human Pose Estimation  
_Zhe Wang, Daeyun Shin, Charless C. Fowlkes_

##### [\[2004.03989\]](https://arxiv.org/abs/2004.03989) Multi-Person Absolute 3D Human Pose Estimation with Weak Depth Supervision  
_Marton Veges, Andras Lorincz_  
[\[Code\]](https://github.com/fabbrimatteo/LoCO)

##### [\[2004.05275\]](https://arxiv.org/abs/2004.05275) Multi-View Matching (MVM): Facilitating Multi-Person 3D Pose Estimation Learning with Action-Frozen People Video  
_Yeji Shen, C.-C. Jay Kuo_  

##### [\[2004.05815\]](https://arxiv.org/abs/2004.05815) MulayCap: Multi-layer Human Performance Capture Using A Monocular Video Camera  
_Zhaoqi Su, Weilin Wan, Tao Yu, Lingjie Liu, Lu Fang, Wenping Wang, Yebin Liu_

##### [\[2004.03686\]](https://arxiv.org/abs/2004.03686) Exemplar Fine-Tuning for 3D Human Pose Fitting Towards In-the-Wild 3D Human Pose Estimation    
_Hanbyul Joo, Natalia Neverova, Andrea Vedaldi_

## Conference Papers

### 2021 ICCV

##### ROMP
**Monocular, One-stage, Regression of Multiple 3D People**  
_Yu Sun, Qian Bao, Wu Liu, Yili Fu, Michael J. Black, Tao Mei_  
[\[arxiv\]](https://arxiv.org/abs/2008.12272) [\[Pytorch code\]](https://github.com/Arthur151/ROMP)

### 2020 ECCV

##### Pose2Mesh: Graph Convolutional Network for 3D Human Pose and Mesh Recovery from a 2D Human Pose
_Hongsuk Choi, Gyeongsik Moon, and Kyoung Mu Lee_  
[\[arxiv\]](https://arxiv.org/abs/2008.09047)


##### Full-Body Awareness from Partial Observations  
_Chris Rockwell and David F. Fouhey_  
[\[paper\]](https://crockwell.github.io/partial_humans/data/2820.pdf)

##### Unsupervised Human 3D Pose Representation with Viewpoint and Pose Disentanglement
_Qiang Nie, Ziwei Liu, Yunhui Liu_  
[\[arxiv\]](https://arxiv.org/abs/2007.07053)

### 2020 CVPR

##### ETD 
**Cascaded Deep Monocular 3D Human Pose Estimation With Evolutionary Training Data**  
_Shichao Li, Lei Ke, Kevin Pratama, Yu-Wing Tai, Chi-Keung Tang, Kwang-Ting Cheng_  
[\[conf\]](https://openaccess.thecvf.com/content_CVPR_2020/html/Li_Cascaded_Deep_Monocular_3D_Human_Pose_Estimation_With_Evolutionary_Training_CVPR_2020_paper.html) [\[Pytorch code\]](https://github.com/Nicholasli1995/EvoSkeleton)

##### DKA
**Deep Kinematics Analysis for Monocular 3D Human Pose Estimation**  
_Jingwei Xu, Zhenbo Yu, Bingbing Ni, Jiancheng Yang, Xiaokang Yang, Wenjun Zhang_  
[\[conf\]](https://openaccess.thecvf.com/content_CVPR_2020/html/Xu_Deep_Kinematics_Analysis_for_Monocular_3D_Human_Pose_Estimation_CVPR_2020_paper.html)

##### 3D Human Mesh Regression With Dense Correspondence
_Wang Zeng, Wanli Ouyang, Ping Luo, Wentao Liu, Xiaogang Wang_  
[\[conf\]](http://openaccess.thecvf.com/content_CVPR_2020/html/Zeng_3D_Human_Mesh_Regression_With_Dense_Correspondence_CVPR_2020_paper.html)

##### Object-Occluded Human Shape and Pose Estimation from a Single Color Image
_Tianshu Zhang, Buzhen Huang and Yangang Wang_  
[\[pdf\]](https://www.yangangwang.com/papers/ZHANG-OOH-2020-03.pdf)

##### Weakly-Supervised 3D Human Pose Learning via Multi-view Images in the Wild
_Umar Iqbal, Pavlo Molchanov, Jan Kautz_  
[\[arxiv\]](https://arxiv.org/abs/2003.07581)

##### Attention Mechanism Exploits Temporal Contexts: Real-time 3D Human Pose Reconstruction
_Ruixu Liu1, Ju Shen1, He Wang1, Chen Chen2, Sen-ching Cheung3, Vijayan Asari1_   
[\[pdf\]](https://webpages.uncc.edu/cchen62/3D-pose.pdf)

##### Multiview-Consistent Semi-Supervised Learning for 3D Human Pose Estimation
_Rahul Mitra, Nitesh B. Gundavarapu, Abhishek Sharma, Arjun Jain_  
[\[conf\]](https://openaccess.thecvf.com/content_CVPR_2020/html/Mitra_Multiview-Consistent_Semi-Supervised_Learning_for_3D_Human_Pose_Estimation_CVPR_2020_paper.html)

##### VIBE
**VIBE: Video Inference for Human Body Pose and Shape Estimation**  
_Muhammed Kocabas, Nikos Athanasiou, Michael J. Black_  
[\[arxiv\]](https://arxiv.org/abs/1912.05656) [\[Pytorch code\]](https://github.com/mkocabas/VIBE)

##### Multiperson
**Coherent Reconstruction of Multiple Humans From a Single Image***  
_Wen Jiang, Nikos Kolotouros, Georgios Pavlakos, Xiaowei Zhou, Kostas Daniilidis_  
[\[conf\]](http://openaccess.thecvf.com/content_CVPR_2020/html/Jiang_Coherent_Reconstruction_of_Multiple_Humans_From_a_Single_Image_CVPR_2020_paper.html)

##### ActiveMoCap
**ActiveMoCap: Optimized Viewpoint Selection for Active Human Motion Capture**  
_Sena Kiciroglu, Helge Rhodin, Sudipta N. Sinha, Mathieu Salzmann, Pascal Fua_  
[\[conf\]](https://openaccess.thecvf.com/content_CVPR_2020/html/Kiciroglu_ActiveMoCap_Optimized_Viewpoint_Selection_for_Active_Human_Motion_Capture_CVPR_2020_paper.html)

##### PandaNet
**PandaNet: Anchor-Based Single-Shot Multi-Person 3D Pose Estimation**  
_Abdallah Benzine, Florian Chabot, Bertrand Luvison, Quoc Cuong Pham, Catherine Achard_  
[\[conf\]](https://openaccess.thecvf.com/content_CVPR_2020/html/Benzine_PandaNet_Anchor-Based_Single-Shot_Multi-Person_3D_Pose_Estimation_CVPR_2020_paper.html)

##### LoCO
**Compressed Volumetric Heatmaps for Multi-Person 3D Pose Estimation**  
_Matteo Fabbri, Fabio Lanzi, Simone Calderara, Stefano Alletto, Rita Cucchiara_  
[\[arxiv\]](https://arxiv.org/abs/2004.00329) [\[Code\]](https://github.com/fabbrimatteo/LoCO)

##### Pgp
**Self-Supervised 3D Human Pose Estimation via Part Guided Novel Image Synthesis**  
_Jogendra Nath Kundu, Siddharth Seth, Varun Jampani, Mugalodi Rakesh, R. Venkatesh Babu, Anirban Chakraborty_  
[\[arxiv\]](https://arxiv.org/abs/2004.04400) [\[Project\]](https://sites.google.com/view/pgp-human)

### 2020-Others

##### AAAI2020 - 3D Human Pose Estimation using Spatio-Temporal Networks with Explicit Occlusion Training  
_Yu Cheng, Bo Yang, Bo Wang, Robby T. Tan_ [\[arxiv\]](https://arxiv.org/abs/2004.11822)


### 2019 ICCV

##### DSD-SATN
**Human Mesh Recovery From Monocular Images via a Skeleton-Disentangled Representation**

_Yu Sun, Yun Ye, Wu Liu, Wenpeng Gao, Yili Fu, Tao Mei_

[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Sun_Human_Mesh_Recovery_From_Monocular_Images_via_a_Skeleton-Disentangled_Representation_ICCV_2019_paper.html) [\[Pytorch code\]](https://github.com/JDAI-CV/DSD-SATN)

##### SPIN
**Learning to Reconstruct 3D Human Pose and Shape via Model-Fitting in the Loop**

_Nikos Kolotouros, Georgios Pavlakos, Michael J. Black, Kostas Daniilidis_

[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Kolotouros_Learning_to_Reconstruct_3D_Human_Pose_and_Shape_via_Model-Fitting_ICCV_2019_paper.html) [\[Pytorch code\]](https://github.com/nkolot/SPIN)

##### TexturePose
**TexturePose: Supervising Human Mesh Estimation With Texture Consistency**

_Georgios Pavlakos, Nikos Kolotouros, Kostas Daniilidis_

[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Pavlakos_TexturePose_Supervising_Human_Mesh_Estimation_With_Texture_Consistency_ICCV_2019_paper.html) [\[Pytorch code\]](https://www.seas.upenn.edu/~pavlakos/projects/texturepose/)

##### DenseRaC
**DenseRaC: Joint 3D Pose and Shape Estimation by Dense Render-and-Compare**

_Yuanlu Xu, Song-Chun Zhu, Tony Tung_

[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Xu_DenseRaC_Joint_3D_Pose_and_Shape_Estimation_by_Dense_Render-and-Compare_ICCV_2019_paper.html)

##### BSFMV
**On Boosting Single-Frame 3D Human Pose Estimation via Monocular Videos**

_Zhi Li, Xuan Wang, Fei Wang, Peilin Jiang_
[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Li_On_Boosting_Single-Frame_3D_Human_Pose_Estimation_via_Monocular_Videos_ICCV_2019_paper.html)

##### STR-GCN

**Exploiting Spatial-Temporal Relationships for 3D Pose Estimation via Graph Convolutional Networks**

_Yujun Cai, Liuhao Ge, Jun Liu, Jianfei Cai, Tat-Jen Cham, Junsong Yuan, Nadia Magnenat Thalmann_
[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Cai_Exploiting_Spatial-Temporal_Relationships_for_3D_Pose_Estimation_via_Graph_Convolutional_ICCV_2019_paper.html)

##### GOR
**Monocular 3D Human Pose Estimation by Generation and Ordinal Ranking**

_Saurabh Sharma, Pavan Teja Varigonda, Prashast Bindal, Abhishek Sharma, Arjun Jain_
[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Sharma_Monocular_3D_Human_Pose_Estimation_by_Generation_and_Ordinal_Ranking_ICCV_2019_paper.html)

##### C3DPO
**C3DPO: Canonical 3D Pose Networks for Non-Rigid Structure From Motion**

_David Novotny, Nikhila Ravi, Benjamin Graham, Natalia Neverova, Andrea Vedaldi_
[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Novotny_C3DPO_Canonical_3D_Pose_Networks_for_Non-Rigid_Structure_From_Motion_ICCV_2019_paper.html)

##### HEMlets
**HEMlets Pose: Learning Part-Centric Heatmap Triplets for Accurate 3D Human Pose Estimation**

_Kun Zhou, Xiaoguang Han, Nianjuan Jiang, Kui Jia, Jiangbo Lu_
[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Zhou_HEMlets_Pose_Learning_Part-Centric_Heatmap_Triplets_for_Accurate_3D_Human_ICCV_2019_paper.html)

##### ONS
**Optimizing Network Structure for 3D Human Pose Estimation**

_Hai Ci, Chunyu Wang, Xiaoxuan Ma, Yizhou Wang_
[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Ci_Optimizing_Network_Structure_for_3D_Human_Pose_Estimation_ICCV_2019_paper.html)

##### DK
**Distill Knowledge From NRSfM for Weakly Supervised 3D Pose Learning**

_Chaoyang Wang, Chen Kong, Simon Lucey_
[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Wang_Distill_Knowledge_From_NRSfM_for_Weakly_Supervised_3D_Pose_Learning_ICCV_2019_paper.html)

##### OANet
**Occlusion-Aware Networks for 3D Human Pose Estimation in Video**

_Yu Cheng, Bo Yang, Bo Wang, Wending Yan, Robby T. Tan_

[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Cheng_Occlusion-Aware_Networks_for_3D_Human_Pose_Estimation_in_Video_ICCV_2019_paper.html)

##### 3DMPPE
**Camera Distance-Aware Top-Down Approach for 3D Multi-Person Pose Estimation From a Single RGB Image**

_Gyeongsik Moon, Ju Yong Chang, Kyoung Mu Lee_

[\[conf\]](http://openaccess.thecvf.com/content_ICCV_2019/html/Moon_Camera_Distance-Aware_Top-Down_Approach_for_3D_Multi-Person_Pose_Estimation_From_ICCV_2019_paper.html) [\[Pytorch code\]](https://github.com/mks0601/3DMPPE_ROOTNET_RELEASE)

### 2019 CVPR

##### GCMR
**Convolutional Mesh Regression for Single-Image Human Shape Reconstruction**

_Nikos Kolotouros, Georgios Pavlakos, Kostas Daniilidis_

[\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Kolotouros_Convolutional_Mesh_Regression_for_Single-Image_Human_Shape_Reconstruction_CVPR_2019_paper.html) [\[Pytorch code\]](https://github.com/nkolot/GraphCMR)

##### HoloPose
**HoloPose: Holistic 3D Human Reconstruction In-The-Wild**

_Riza Alp Guler, Iasonas Kokkinos_

[\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Guler_HoloPose_Holistic_3D_Human_Reconstruction_In-The-Wild_CVPR_2019_paper.html) [\[code\]](http://arielai.com/holopose)

##### HMR-video
**Learning 3D Human Dynamics From Video**

_Angjoo Kanazawa, Jason Y. Zhang, Panna Felsen, Jitendra Malik_

[\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Kanazawa_Learning_3D_Human_Dynamics_From_Video_CVPR_2019_paper.html) [\[Tensorflow code\]](https://github.com/akanazawa/human_dynamics)

##### SemGCN
**Semantic Graph Convolutional Networks for 3D Human Pose Regression**

_Long Zhao, Xi Peng, Yu Tian, Mubbasir Kapadia, Dimitris N. Metaxas_

[\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Zhao_Semantic_Graph_Convolutional_Networks_for_3D_Human_Pose_Regression_CVPR_2019_paper.html) [\[Pytorch code\]](https://github.com/garyzhao/SemGCN)

##### VideoPose3D
**3D Human Pose Estimation in Video With Temporal Convolutions and Semi-Supervised Training**

_Dario Pavllo, Christoph Feichtenhofer, David Grangier, Michael Auli_

[\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Pavllo_3D_Human_Pose_Estimation_in_Video_With_Temporal_Convolutions_and_CVPR_2019_paper.html) [\[Pytorch code\]](https://github.com/facebookresearch/VideoPose3D)

##### EpipolarPose
**Self-Supervised Learning of 3D Human Pose Using Multi-View Geometry**

_Muhammed Kocabas, Salih Karagoz, Emre Akbas_

[\[conf\]](http://openaccess.thecvf.com/content_CVPR_2019/html/Kocabas_Self-Supervised_Learning_of_3D_Human_Pose_Using_Multi-View_Geometry_CVPR_2019_paper.html) [\[Pytorch code\]](https://github.com/mkocabas/EpipolarPose)

### 2018 ECCV

##### TP-Net
**Exploiting temporal information for 3D human pose estimation**

_Mir Rayat Imtiaz Hossain, James J. Little_

[\[conf\]](http://openaccess.thecvf.com/content_ECCV_2018/html/Mir_Rayat_Imtiaz_Hossain_Exploiting_temporal_information_ECCV_2018_paper.html) [\[code\]](https://github.com/rayat137/Pose_3D)

##### IHPR
**Integral Human Pose Regression**

_Xiao Sun, Bin Xiao, Fangyin Wei, Shuang Liang, Yichen Wei_

[\[conf\]](http://openaccess.thecvf.com/content_ECCV_2018/html/Xiao_Sun_Integral_Human_Pose_ECCV_2018_paper.html) [\[Pytorch code\]](https://github.com/JimmySuen/integral-human-pose)

### 2018 CVPR

##### HMR
**End-to-End Recovery of Human Shape and Pose**

_Angjoo Kanazawa, Michael J. Black, David W. Jacobs, Jitendra Malik_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Kanazawa_End-to-End_Recovery_of_CVPR_2018_paper.html) [\[Tensorflow - official\]](https://github.com/akanazawa/hmr) [\[Pytorch\]](https://github.com/MandyMo/pytorch_HMR)

##### MVC 
**Learning Monocular 3D Human Pose Estimation From Multi-View Images**

_Helge Rhodin, Jörg Spörri, Isinsu Katircioglu, Victor Constantin, Frédéric Meyer, Erich Müller, Mathieu Salzmann, Pascal Fua_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Rhodin_Learning_Monocular_3D_CVPR_2018_paper.html)

##### Deephar
**2D/3D Pose Estimation and Action Recognition Using Multitask Deep Learning**

_Diogo C. Luvizon, David Picard, Hedi Tabia_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Luvizon_2D3D_Pose_Estimation_CVPR_2018_paper.html) [\[code\]](https://github.com/dluvizon/deephar)

##### ODS
**Ordinal Depth Supervision for 3D Human Pose Estimation**  
_Georgios Pavlakos, Xiaowei Zhou, Kostas Daniilidis_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Pavlakos_Ordinal_Depth_Supervision_CVPR_2018_paper.html) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) 

##### Deephar
**2D/3D Pose Estimation and Action Recognition Using Multitask Deep Learning**  
_Diogo C. Luvizon, David Picard, Hedi Tabia_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Pavlakos_Ordinal_Depth_Supervision_CVPR_2018_paper.html) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) 

### 2018 Others

##### LPG-AAAI18
**Learning Pose Grammar to Encode Human Body Configuration for 3D Pose Estimation**   
_Hao-Shu Fang, Yuanlu Xu, Wenguan Wang, Xiaobai Liu, Song-Chun Zhu_

[\[conf\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471)

##### OriNet-BMVC18
**OriNet: A Fully Convolutional Network for 3D Human Pose Estimation**  
_Chenxu Luo, Xiao Chu, Alan Yuille_  
[\[arxiv\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471) [\[code\]](https://github.com/chenxuluo/OriNet-demo)

### 2017 ICCV
comming soon...

### 2017 CVPR

##### UP
**Unite the People: Closing the Loop Between 3D and 2D Human Representations**

_Christoph Lassner, Javier Romero, Martin Kiefel, Federica Bogo, Michael J. Black, Peter V. Gehler_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Lassner_Unite_the_People_CVPR_2017_paper.html) [\[code\]](http://up.is.tuebingen.mpg.de/)

##### RPSM
**Recurrent 3D Pose Sequence Machines**  
_Mude Lin, Liang Lin, Xiaodan Liang, Keze Wang, Hui Cheng_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Lin_Recurrent_3D_Pose_CVPR_2017_paper.html) [\[code\]](https://github.com/MudeLin/RPSM)

##### C2F
**Coarse-To-Fine Volumetric Prediction for Single-Image 3D Human Pose**  
_Georgios Pavlakos, Xiaowei Zhou, Konstantinos G. Derpanis, Kostas Daniilidis_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Pavlakos_Coarse-To-Fine_Volumetric_Prediction_CVPR_2017_paper.html) [\[code\]](https://github.com/geopavlakos/c2f-vol-demo)

##### LFD
**Lifting From the Deep: Convolutional 3D Pose Estimation From a Single Image**  
_Denis Tome, Chris Russell, Lourdes Agapito_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Tome_Lifting_From_the_CVPR_2017_paper.html) [\[code\]](https://github.com/DenisTome/Lifting-from-the-Deep-release)

### 2016 ECCV

###### SMPLify
**Keep it SMPL: Automatic Estimation of {3D} Human Pose and Shape from a Single Image**  
_Bogo Federica, Kanazawa  Angjoo, Lassner Christoph, Gehler Peter, Romero Javier, Black Michael J._

[\[Paper\]](http://files.is.tue.mpg.de/black/papers/BogoECCV2016.pdf) [\[code\]](http://smplify.is.tue.mpg.de/)

### 2016 CVPR

###### SMD
**Sparseness Meets Deepness: 3D Human Pose Estimation from Monocular Video**  
_Xiaowei Zhou, Menglong Zhu, Spyridon Leonardos, Kosta Derpanis, Kostas Daniilidis_

[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2016/html/Zhou_Sparseness_Meets_Deepness_CVPR_2016_paper.html) [\[code\]](https://github.com/chuxiaoselena/SparsenessMeetsDeepness)

[\[Back to top\]](#Contents)

## Journal-Papers

###### FBN
**Feature Boosting Network For 3D Pose Estimation**  
_Jun Liu, Henghui Ding, Amir Shahroudy, Ling-Yu Duan, Xudong Jiang, Gang Wang, Alex C. Kot_

[\[arxiv\]](https://arxiv.org/abs/1901.04877)

## Datasets

###### Deep Fashion3D
Deep Fashion3D: A Dataset and Benchmark for 3D Garment Reconstruction from Single Images  
_Heming Zhu and Yu Cao and Hang Jin and Weikai Chen and Dong Du and Zhangye Wang and Shuguang Cui and Xiaoguang Han_  
[\[arxiv\]](https://arxiv.org/abs/2003.12753) [\[project\]](https://kv2000.github.io/2020/03/25/deepFashion3DRevisited/)

###### 3DBodyTex.Pose
Towards Generalization of 3D Human Pose Estimation In The Wild  
_Renato Baptista, Alexandre Saint, Kassem Al Ismaeil, Djamila Aouada_  
[\[arxiv\]](https://arxiv.org/abs/2004.09989)

###### GPA
Geometric Pose Affordance: 3D Human Pose with Scene Constraints  
_Zhe Wang, Liyan Chen, Shaurya Rathore, Daeyun Shin, Charless Fowlkes_
[\[arxiv\]](https://arxiv.org/abs/1905.07718) [\[project\]](http://wangzheallen.github.io/GPA)

##### JTA
Learning to Detect and Track Visible and Occluded Body Joints in a Virtual World    
_Matteo Fabbri, Fabio Lanzi, Simone Calderara, Andrea Palazzi, Roberto Vezzani, Rita Cucchiara_  
[\[arxiv\]](https://arxiv.org/abs/1803.08319) [\[project\]](https://aimagelab.ing.unimore.it/imagelab/page.asp?IdPage=25)


## Contribute

Contributions are welcome! 
Please feel free to [pull requests](https://github.com/Arthur151/SOTA-on-monocular-3D-pose-and-shape-estimation/pulls), [open an issue](https://github.com/Arthur151/SOTA-on-monocular-3D-pose-and-shape-estimation/issues) or send me email (yusun@stu.hit.edu.cn) to add/correct state-of-the-art methods.
