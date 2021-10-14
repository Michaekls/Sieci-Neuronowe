# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:23:00 2021

@author: m_war

"""
from odczyt_pliku import odczyt_z_pliku, odczyt_z_pliku2

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.applications.resnet50 import ResNet50

_shape=64
_k='10'

for i in range(80):
    dane,wyjscie=odczyt_z_pliku(str(i),_k)
    
    ############  

dane=[]
wyjscie=[]
x_train = np.array(dane)
x_test = np.array(wyjscie) 


model = ResNet50(weights=None,classes=2, input_shape=(_shape,_shape,1))

model.compile(#tf.keras.optimizers.Adam(lr=0.00001),
              optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

#model.fit(x_train, x_test, epochs=4)

#model.save("model_k6_PoPw_pol_dw1_64_resnet.h5")

########################### do sprawdzenia, ile dobrze przypasuje ##############
dane_sprawdzenie=[]
wyjscie_sprawdzenie=[]
for i in range(4):
    dane_sprawdzenie,wyjscie_sprawdzenie=odczyt_z_pliku2(str(i),_k)


    ############    czytamy
dane_sprawdzenie=np.array(dane_sprawdzenie)
wyjscie_sprawdzenie=np.array(wyjscie_sprawdzenie)


#history=model.fit(x_train, x_test, epochs=4, verbose=1, validation_data=(dane_sprawdzenie, wyjscie_sprawdzenie),class_weight=classWeight)
history=model.fit(x_train, x_test, epochs=4, verbose=1, validation_data=(dane_sprawdzenie, wyjscie_sprawdzenie))

model.save("pol_model_k15_PoPr_resnet.h5")

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


test_loss, test_acc = model.evaluate(dane_sprawdzenie, wyjscie_sprawdzenie, verbose=2)

print('\nTest accuracy:', test_acc)