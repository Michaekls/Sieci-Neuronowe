# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:23:00 2021

@author: m_war
"""

from odczyt_pliku import odczyt_z_pliku, odczyt_z_pliku2

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout

from tensorflow.keras.layers import Activation,BatchNormalization

shape=64

        
model = Sequential()

#1st Convolutional Layer
model.add(Conv2D(96, input_shape=(64,64,1), kernel_size=(11,11), strides=(4,4), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same'))

#2nd Convolutional Layer
model.add(Conv2D(filters=256, kernel_size=(5, 5), strides=(1,1), padding='same'))
model.add(BatchNormalization())
model.add((Activation('relu')))
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same'))

#3rd Convolutional Layer
model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))

#4th Convolutional Layer
model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))

#5th Convolutional Layer
model.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same'))

#Passing it to a Fully Connected layer
model.add(Flatten())
# 1st Fully Connected Layer
model.add(Dense(4096))
model.add(Activation('relu'))
# Add Dropout to prevent overfitting
model.add(Dropout(0.4))

#2nd Fully Connected Layer
model.add(Dense(4096))
model.add(Activation('relu'))
#Add Dropout
model.add(Dropout(0.4))

#3rd Fully Connected Layer
model.add(Dense(1000))
model.add(Activation('relu'))
#Add Dropout
model.add(Dropout(0.4))

#Output Layer
model.add(Dense(2))
model.add(Activation('softmax'))

_shape=64
_k='10'

dane=[]
wyjscie=[]
for i in range(35):
    dane,wyjscie=odczyt_z_pliku(str(i),_k)
    
    ############  

x_train = np.array(dane)
x_test = np.array(wyjscie)


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

# history=model.fit(x_train, x_test, epochs=8)
# model.save("model_k6_PoPw_dw_64_alexnet.h5")

########################### do sprawdzenia, ile dobrze przypasuje ##############
dane_sprawdzenie=[]
wyjscie_sprawdzenie=[]
for i in range(10):
     dane_sprawdzenie,wyjscie_sprawdzenie=odczyt_z_pliku2(str(i),_k)

    
    ############    czytamy
dane_sprawdzenie=np.array(dane_sprawdzenie)
wyjscie_sprawdzenie=np.array(wyjscie_sprawdzenie)

#uczenie modelu
history=model.fit(x_train, x_test, epochs=4, verbose=1, validation_data=(dane_sprawdzenie, wyjscie_sprawdzenie))

model.save("pol_model_k15_PoPr_alexnet.h5")

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

#Sprawdzenie dokladnosci
test_loss, test_acc = model.evaluate(dane_sprawdzenie, wyjscie_sprawdzenie, verbose=2)

print('\nTest accuracy:', test_acc)

