# State-of-the-art methods on monocular 3D pose estimation / 3D mesh recovery

Benchmark Leaderboard and state-of-the-art method list on monocular 3D pose estimation / 3D mesh recovery

Feel free to [contribute](#Contribute)!

## Contents
 - [Benchmark Leaderboard](#Benchmark-Leaderboard)
 - [arXiv Papers](#arXiv-Papers)
 - [Conference Papers](#conference-papers)
   - 2020: [CVPR](#2020-CVPR), [ECCV](#2020-ECCV)
   - 2019: [CVPR](#2019-CVPR), [ICCV](#2019-ICCV)
   - 2018: [CVPR](#2018-CVPR), [ECCV](#2018-ECCV), [Others](#2018-Others)
   - 2017: [CVPR](#2017-CVPR), [ICCV](#2017-ICCV)
   - 2016: [CVPR](#2016-CVPR), [ECCV](#2016-ECCV)
 - [Journal Papers](#Journal-Papers)
 - [Datasets](#Datasets)
 - [Other Related Papers](#Other-related-papers)

## Benchmark Leaderboard

### Evaluation Matrix

See [``evaluation``](evaluation.md) to get more details on evaluation matrix for 3D pose estimation / mesh recovery.

### Comparisons on Human3.6M.

See [``datasets/Human3.6M``](datasets/Human3.6M.md) to get more details on Human3.6M

#### State-of-the-art 3D pose estimation methods

| Methods | Publication | MPJPE</downarrow> | PA-MPJPE</downarrow> | link |
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

Evaluation Datasets of MPJPE: Human3.6M | Human3.6M | HumanEva-I | 3DPW 
| Methods | Publication | MPJPE\downarrow | PA-MPJPE\downarrow | MPJPE\downarrow | PA-MPJPE\downarrow | link |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
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

## Conference Papers

### 2020 ECCV
comming soon...

### 2020 CVPR

##### VIBE
**VIBE: Video Inference for Human Body Pose and Shape Estimation**

_Muhammed Kocabas, Nikos Athanasiou, Michael J. Black_

[\[arxiv\]](https://arxiv.org/abs/1912.05656) [\[Pytorch code\]](https://github.com/mkocabas/VIBE)

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

## Contribute

Contributions are welcome! 
Please feel free to [pull requests](https://github.com/Arthur151/SOTA-on-monocular-3D-pose-and-shape-estimation/pulls), [open an issue](https://github.com/Arthur151/SOTA-on-monocular-3D-pose-and-shape-estimation/issues) or send me email (yusun@stu.hit.edu.cn) to add/correct state-of-the-art methods.