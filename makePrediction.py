import cv2
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , Flatten , Conv2D , MaxPooling2D , Dropout , Activation , BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adam , Adamax
from tensorflow.keras import regularizers
from tensorflow.keras.applications.xception import preprocess_input
import keras
#import Image

base_model = tf.keras.applications.xception.Xception(weights= 'imagenet' ,include_top = False , input_shape = (150,150,3) , pooling = 'max' )

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'de', 'nothing', 'space']

model = Sequential([
   base_model, 
           BatchNormalization(),
    Dense(256,activation = 'relu'),
    Dropout(.5),
    Dense(29 , activation= 'softmax' )
])

#print(tf.version.VERSION)
model.load_weights('Model/ASLModel.h5')

def predictImage(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    # Make prediction
    prediction = model.predict(img_array)
    # Find the index of the class with the highest probability
    predicted_class_index = np.argmax(prediction)
    # Get the corresponding probability
    highest_probability = prediction[0, predicted_class_index]
    # Print the index and probability
    print("Predicted class index:", alphabet[predicted_class_index])
    print("Highest probability:", highest_probability)
    return alphabet[predicted_class_index]

def getRandChar():
    # get random character from alphabet
    # return it
    return ''