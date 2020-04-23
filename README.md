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
   - 2016: [CVPR](#2016-CVPR)
 - [Journal Papers](#Journal-Papers)
 - [Datasets](#Datasets)
 - [Other Related Papers](#Other-related-papers)

## Benchmark Leaderboard

### Evaluation Matrix

See [``evaluation``](evaluation.md) to get more details on evaluation matrix for 3D pose estimation / mesh recovery.

### Comparisons on Human3.6M.

See [``datasets/Human3.6M``](datasets/Human3.6M.md) to get more details on Human3.6M

| Methods | Publication | MPJPE | PA-MPJPE | link |
| :----: | :----: | :----: | :----: | :----: |
| [ODS](#ODS) |  AAAI18 | 60.4 | 45.7 | [\[conf\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) |
| [ODS](#ODS) |  AAAI18 | 60.4 | 45.7 | [\[conf\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) |
| [ODS](#ODS) |  AAAI18 | 60.4 | 45.7 | [\[conf\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) |
| [ODS](#ODS) |  AAAI18 | 60.4 | 45.7 | [\[conf\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) |
| [ODS](#ODS) |  AAAI18 | 60.4 | 45.7 | [\[conf\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) |
| [Deephar](#Deephar) |  CVPR18 | 53.2 | - | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Luvizon_2D3D_Pose_Estimation_CVPR_2018_paper.html) [\[code\]](https://github.com/dluvizon/deephar) |
| [ODS](#ODS) |  CVPR18 | 56.2 | 41.8 | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Pavlakos_Ordinal_Depth_Supervision_CVPR_2018_paper.html) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) |
| [LPG](#LPG) |  AAAI18 | 60.4 | 45.7 | [\[conf\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471) |
| [CHPR](#CHPR) |  ICCV17 | 92.4 | 59.1 | [\[conf\]](http://openaccess.thecvf.com/content_iccv_2017/html/Sun_Compositional_Human_Pose_ICCV_2017_paper.html) |
| [3DPB](#3DPB) |  ICCV17 | 62.9 | 47.7 | [\[conf\]](http://openaccess.thecvf.com/content_iccv_2017/html/Martinez_A_Simple_yet_ICCV_2017_paper.html) [\[code\]](https://github.com/una-dinosauria/3d-pose-baseline) |
| RPSM |  CVPR17 | 73.1 | - | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Lin_Recurrent_3D_Pose_CVPR_2017_paper.html) [\[code\]](https://github.com/MudeLin/RPSM) |
| [C2F](#C2F) |  CVPR17 | 71.9 | 51.9 | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Pavlakos_Coarse-To-Fine_Volumetric_Prediction_CVPR_2017_paper.html) [\[code\]](https://github.com/geopavlakos/c2f-vol-demo) |
| [LFD](#LFD) |  CVPR17 | 113.0 | - | [\[conf\]](http://openaccess.thecvf.com/content_cvpr_2017/html/Tome_Lifting_From_the_CVPR_2017_paper.html) [\[code\]](https://github.com/DenisTome/Lifting-from-the-Deep-release) |
| [SMD](#SMD) |  CVPR16 | 88.4 | - | [\[arxiv\]](https://arxiv.org/abs/1511.09439) [\[code\]](https://github.com/chuxiaoselena/SparsenessMeetsDeepness) |



## Method Zoo

## arXiv Papers

## Conference Papers

### 2020 CVPR

### 2020 ECCV

### 2019 CVPR

### 2018 CVPR

##### ODS
Ordinal Depth Supervision for 3D Human Pose Estimation  
_Georgios Pavlakos, Xiaowei Zhou, Kostas Daniilidis_
[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Pavlakos_Ordinal_Depth_Supervision_CVPR_2018_paper.html) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) 

##### Deephar
2D/3D Pose Estimation and Action Recognition Using Multitask Deep Learning  
_Diogo C. Luvizon, David Picard, Hedi Tabia_
[\[conf\]](http://openaccess.thecvf.com/content_cvpr_2018/html/Pavlakos_Ordinal_Depth_Supervision_CVPR_2018_paper.html) [\[code\]](https://github.com/geopavlakos/ordinal-pose3d) 

### 2018 ICCV

### 2018 Others

##### LPG 
Learning Pose Grammar to Encode Human Body Configuration for 3D Pose Estimation   
_Hao-Shu Fang, Yuanlu Xu, Wenguan Wang, Xiaobai Liu, Song-Chun Zhu_
[\[conf\]](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16471)

### 2017 CVPR

### 2017 ECCV

### 2016 CVPR

###### Sparseness Meets Deepness: 3D Human Pose Estimation from Monocular Video
_Xiaowei Zhou, Menglong Zhu, Spyridon Leonardos, Kosta Derpanis, Kostas Daniilidis_

## Journal-Papers


## Contribution

Contributions are welcome! 
Please feel free to [pull requests](https://github.com/Arthur151/SOTA-on-monocular-3D-pose-and-shape-estimation/pulls), [open an issue](https://github.com/Arthur151/SOTA-on-monocular-3D-pose-and-shape-estimation/issues) or send me email (yusun@stu.hit.edu.cn) to add/correct state-of-the-art methods.