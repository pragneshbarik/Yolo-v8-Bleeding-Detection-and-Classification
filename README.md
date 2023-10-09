# SVNIT_MLIP_2

# Capsule Endoscopy

## Evaluation Metrics

 ### Classification Metrics
| Metric (in probability)| Value    |
|------------------------|----------|
| Accuracy               |   0.7864 |
| Recall (Bleeding)                 |   0.9602 |
| Recall (Non Bleeding)                 |   0.6126|
| F1-Score (Bleeding)               |  0.8180  |
| F1-Score (Non Bleeding)               |  0.7415  |
| F1-Score (Weighted)               |  0.7798  |

### Detection Metrics
| Metric (in probability)| Value          |
|------------------------|----------------|
|  mAP50 |     0.652      |
| mAP50-95|     0.336     |


### Training Metrics

| **Confusion Metrics** | **Confusion Metrics Normalized**|
|------ |---------------------|
|![confusion_matrix](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/31ef191b-b8f4-4dc8-a336-6a2a340db6d3)|![confusion_matrix_normalized](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/7a7d65d3-aa1c-43c1-bf19-7c40d390da9f)|


| **F1 Curve** | **P Curve**|**PR Curve** |**R Curve**|
|------ |---------------------|------ |---------------------|
|![F1_curve](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/ec099737-cbbb-4da3-9cfd-4a0bb5913a58)|![P_curve](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/a14ef28c-51e8-4c99-8ffd-58307e6c2280)|![PR_curve](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/e8073211-0c11-4e22-9559-7e50b6aa47da)|![R_curve](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/28c4cf9f-9e21-471a-92d8-de5b5ad80851)



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

| **Imagename** | **A0047.png** | **A0043.png**|**A0048.png**|**A0040.png**|**A0035.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/b81cf6fd-58eb-4812-a174-46d1af28ae72)|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/4e51a286-98e9-44af-85b3-cc0cc79dfbef)|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/fb8d5cc0-9d46-46b1-b9a7-6d46215ceb57)| ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/bd986059-75c4-40ef-be4f-1c334fb14766)|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/b1a4b811-3341-41fc-bdda-c82a55c6641e)
|


## Interpretability Plots (Cam Plots of 2nd last layer)                                                                                                         
| **Imagename** | **A0001_cam.png** | **A0033_cam.png**|**A0035_cam.png**|**A0040_cam.png**|**A0041_cam.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_1\Interpretability_plots\A0001_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Interpretability_plots\A0033_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Interpretability_plots\A0035_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_1\Interpretability_plots\A0040_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_1\Interpretability_plots\A0041_cam.png" alt="Image 1">|

# Testing Dataset 2
## Detection and Classification

| **Imagename** | **A0258.png** | **A0260.png**|**A0500.png**|**A0261.png**|**A0498.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/b3024ef7-79cf-46ed-b2c0-24962f9f0fdc)
| ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/43632a5e-2389-4648-9839-ead3c0abe104)
|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/e6d69155-ff8c-4064-8b03-ed3462270385)
| ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/5ed99275-804b-41ac-8697-d53105f52676)
|![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/f38d6335-3211-427e-8cb3-83c146813db3)
|

## Interpretability Plots (Cam Plots of 2nd last layer)                                                                                                        ![image](https://github.com/pragneshbarik/misahub-challenge/assets/65221256/d39be5d0-25e2-4276-a209-c0aca05d85dd)
 
| **Imagename** | **A0211_cam.png** | **A0498_cam.png**|**A0500_cam.png**|**A0532_cam.png**|**A0551_cam.png**|
|------ |---------------------|---------------------|---------------------|---------------------|---------------------|
|**Images** | <img src="Images_README\testing_dataset_2\Interpretability_plots\A0211_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\Interpretability_plots\A0498_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\Interpretability_plots\A0500_cam.png" alt="Image 1">| <img src="Images_README\testing_dataset_2\Interpretability_plots\A0532_cam.png" alt="Image 1">|<img src="Images_README\testing_dataset_2\Interpretability_plots\A0551_cam.png" alt="Image 1">|

