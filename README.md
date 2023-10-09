# SVNIT_MLIP_2

# Capsule Endoscopy

## Evaluation Metrics

 ### Classification Metrics
| Metric (in probability)| Value    |
|------------------------|----------|
| Accuracy               |   0.7864782276546982 |
| Recall (Bleeding)                 |   0.9602750190985485 |
| Recall (Non Bleeding)                 |   0.612681436210848|
| F1-Score (Bleeding)               |  0.8180930686625448  |
| F1-Score (Non Bleeding)               |  0.741562644475266  |
| F1-Score (Weighted)               |  0.7798278565689054  |
### Training Metrics

### Detection Metrics
| Metric (in probability)| Value          |
|------------------------|----------------|
|  mAP50 |     0.652      |
| mAP50-95|     0.336     |

# Validation Dataset
## Detection and Classification

| **Imagename** | **img- (271).png** | **img- (386).png**|**img- (389).png**|**img- (406).png**|**img- (409).png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | |<img src="Images_README\validation_dataset\classification_and_detection\img- (389).png" alt="Image 1">| <img src="Images_README\validation_dataset\classification_and_detection\img- (406).png" alt="Image 1">|<img src="Images_README\validation_dataset\classification_and_detection\img- (409).png" alt="Image 1">|
|**Confidance**| 0.96 | 0.96 |0.96 | 0.96 |0.96 |
                                                                                                         

| **Imagename** | **img- (608).png** | **img- (609).png**|**img- (797).png**|**img- (908).png**|**img- (912).png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\validation_dataset\classification_and_detection\img- (608).png" alt="Image 1">| <img src="Images_README\validation_dataset\classification_and_detection\img- (609).png" alt="Image 1">|<img src="Images_README\validation_dataset\classification_and_detection\img- (797).png" alt="Image 1">| <img src="Images_README\validation_dataset\classification_and_detection\img- (908).png" alt="Image 1">|<img src="Images_README\validation_dataset\classification_and_detection\img- (912).png" alt="Image 1">|
|**Confidance**| 0.96 | 0.96 |0.97 | 0.97 |0.97 |

## Interpretability Plots (Cam Plots of 2nd last layer)

### Test Dataset 1

| **Imagename** | **A0010.png** | **A0021.png**|**A0031.png**|**A0040.png**|**A0045.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Cam Images** | ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/d4f9ba16-fa0a-477f-b65c-473bb858a8df)| ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/ead3de41-9dfd-4654-8a8b-dc264198a273)|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/d0369a27-069f-41d7-b110-dbf56b24c5a4)| ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/92306a7b-edb8-4943-9f68-956665a44cb1)|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/52080bf0-c102-4d83-b92b-75f4a6cb0b4e)


### Test Dataset 2
| **Imagename** | **A0164.png** | **A0256.png**|**A0300.png**|**A0384.png**|**A0473.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**CAM Images** | ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/80a92f3f-d64a-41d0-b16b-22723c67c7e1)| ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/37361d83-a8bd-4c8d-869e-a7cdbe11b89f)|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/06f7f812-1a4d-4147-bd3a-274cb84b7851)|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/c24f688e-c112-4249-8c2d-133a80c7a411)|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/ce9addc6-25c2-4e1f-a5ce-52360d8b795b)


# Testing Dataset 1
## Detection and Classification

| **Imagename** | **A0001.png** | **A0033.png**|**A0035.png**|**A0040.png**|**A0041.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_1\Classification_and_detection\A0001.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Classification_and_detection\A0033.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Classification_and_detection\A0035.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Classification_and_detection\A0040.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Classification_and_detection\A0041.png" alt="Image 1">|
|**Confidance**| 0.29 | 0.75 |0.44 | 0.37 | 0.27 |

## Interpretability Plots (Cam Plots of 2nd last layer)                                                                                                         
| **Imagename** | **A0001_cam.png** | **A0033_cam.png**|**A0035_cam.png**|**A0040_cam.png**|**A0041_cam.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_1\Interpretability_plots\A0001_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Interpretability_plots\A0033_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Interpretability_plots\A0035_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Interpretability_plots\A0040_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Interpretability_plots\A0041_cam.png" alt="Image 1">|

# Testing Dataset 2
## Detection and Classification

| **Imagename** | **A0211.png** | **A0498.png**|**A0500.png**|**A0532.png**|**A0551.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_2\classification_and_detection\A0211.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\classification_and_detection\A0498.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\classification_and_detection\A0500.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\classification_and_detection\A0532.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\classification_and_detection\A0551.png" alt="Image 1">|
|**Confidance**| 0.27 | 0.28 |0.62 | 0.27 |0.32 |

## Interpretability Plots (Cam Plots of 2nd last layer)                                                                                                         
| **Imagename** | **A0211_cam.png** | **A0498_cam.png**|**A0500_cam.png**|**A0532_cam.png**|**A0551_cam.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_2\Interpretability_plots\A0211_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\Interpretability_plots\A0498_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\Interpretability_plots\A0500_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\Interpretability_plots\A0532_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\Interpretability_plots\A0551_cam.png" alt="Image 1">|

