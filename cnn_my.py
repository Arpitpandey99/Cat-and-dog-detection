# Part 1 - Biulding the CNN

#Importing the keras library and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#Initialising the Convolutional Neural Network
classifier = Sequential()

# Step 1 - Convolution layer
classifier.add(Convolution2D(32,(3,3), input_shape = (64,64,3),
                             activation = 'relu'))

# Step 2 - Pooling layer
classifier.add(MaxPooling2D(pool_size = (2,2)))

#Adding the second convolution layer
classifier.add(Convolution2D(32,(3,3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full Connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1 , activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                   metrics = ['accuracy'])


# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('E://Data\Deep_Learning_A_Z//Volume 1 - Supervised Deep Learning//Part 2 - Convolutional Neural Networks (CNN)//Section 8 - Building a CNN//cat-and-dog-detection//dataset//training_set',
                                                 target_size = (64,64),
                                                 batch_size = 64,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('E://Data//Deep_Learning_A_Z//Volume 1 - Supervised Deep Learning//Part 2 - Convolutional Neural Networks (CNN)//Section 8 - Building a CNN//cat-and-dog-detection//dataset//test_set',
                                            target_size = (64,64),
                                            batch_size = 64,
                                            class_mode = 'binary')

history = classifier.fit_generator(training_set,
                         steps_per_epoch = (8000/64),
                         epochs = 10,
                         validation_data = test_set,
                         validation_steps = (2000/64))

print(history)
# Predicting the result 
from keras.preprocessing import image
import numpy as np
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg',
                            target_size = (64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image,axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'


import matplotlib.pyplot as plt
fig1, ax1 = plt.subplots(1,2,figsize = (20,5))
    
for i,j in enumerate(['accuracy','loss']):
    ax1[i].plot(history.history[j],'o-',color = 'green')
    ax1[i].plot(history.history['val_'+j],'o-',color = '#D66520')
    ax1[i].set_title('Model '+str(j))
    ax1[i].set_xlabel('epochs')
    ax1[i].set_ylabel(j)
    ax1[i].legend(['train','val'])
