# Cat-and-dog-detection

#### This Project is Detection of Cat Or Dog from the Image using the Convolutional Neural Network with the respected Accuracy. In this project I've Created a convoltional Neural Network From scratch to detect a Cat or a Dog in the Image using Deep Learning Algorithm. 

## Objective
#### In this project I've created a model to detect wheather the image is of cat or dog with the help of Convolutional Neural Network and optimise it to get the better accuracy.
####
## Convolutional Neural Network
#### Convolutional Neural Network (CNN), also known as ConvNet, comes under Artificial Neural Network (ANN) that, when compared to other FC-layer networks, has enhanced feeds and an impressive potential to generate power, can detect highly embedded features of objects, particularly location data, and can correctly determine. The in-depth CNN model has a limited number of processing layers that can differentiate different aspects of input data (example, picture) using multiple output levels. The first layers identify and create high-level functionalities (with low releases), and the deeper layers create low-level functionalities (with high releases).

![6](https://user-images.githubusercontent.com/52160632/121932125-1fdd0680-cd62-11eb-875b-3424497cb234.jpeg)

## Dataset Description
#### The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal).

#### Chest X-ray images (anterior-posterior) were selected from retrospective cohorts of pediatric patients of one to five years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care.

![3](https://user-images.githubusercontent.com/52160632/122100964-6a798400-ce31-11eb-91d3-9a21965c65ce.png)

#### For the analysis of chest x-ray images, all chest radiographs were initially screened for quality control by removing all low quality or unreadable scans. The diagnoses for the images were then graded by two expert physicians before being cleared for training the AI system. In order to account for any grading errors, the evaluation set was also checked by a third expert.


![4](https://user-images.githubusercontent.com/52160632/122100978-706f6500-ce31-11eb-85f9-bb123bec8506.png)

## Image Augmentation
#### Deep networks need large amount of training data to achieve good performance. To build a powerful image classifier using very little training data, image augmentation is usually required to boost the performance of deep networks. Image augmentation artificially creates training images through different ways of processing or combination of multiple processing, such as random rotation, shifts, shear and flips, etc.

# Model
![Screenshot (101)](https://user-images.githubusercontent.com/52160632/122267008-0b327700-cef8-11eb-870b-6d5b08a4dbdb.png)

#### As we can see the model summary in which the entire model structure is shown in which the first convolutional layer is created with 128,128,3 size with the ReLu activation function. After the convolutional layer there is a Max pooling layer with the pool size of 2,2. There are 3 convolutional layers and max pooling layer with some dropout of 10% and 20% and at the last stages of the layer there is a flatten layer to flatten the data so that we can get the output in the dense layer with the help of sigmoid function.

![Screenshot (103)](https://user-images.githubusercontent.com/52160632/122449694-c83dd580-cfc3-11eb-897d-4c627cff767a.png)
#### As we can see model performance and our model gives 96.53% accuracy in the training set and 90.06% in the test set with the training loss of 0.09 and test loss of 0.37.
#### We can see the graph of model’s training accuracy vs test accuracy and training loss vs test loss in all the 25 epochs in which our model is trained. Model accuracy is slightly increasing in every epoch and model loss is decreasing in epochs. 

![5](https://user-images.githubusercontent.com/52160632/122449841-f0c5cf80-cfc3-11eb-8f35-1920138ec4eb.png)

### Model Output






