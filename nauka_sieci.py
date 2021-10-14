# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:23:00 2021

@author: m_war
"""
from odczyt_pliku import odczyt_z_pliku, odczyt_z_pliku2


import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.utils import compute_class_weight

_shape=64
_k="10"

dane=[]
wyjscie=[]
for i in range(100):
     dane,wyjscie=odczyt_z_pliku(str(i),_k)
    
    ############  

x_train = np.array(dane)
x_test = np.array(wyjscie)


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(_shape,_shape)),
    #tf.keras.layers.Dense(1024,activation="relu",input_shape=(shape,shape)),
    tf.keras.layers.Dense(512,activation='sigmoid'), #"sigmoid"
    tf.keras.layers.Dense(256,activation='sigmoid'),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(16,activation='relu'),
    tf.keras.layers.Dense(2,activation="softmax") # 
    ])



model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

########################### do sprawdzenia, ile dobrze przypasuje ##############
dane_sprawdzenie=[]
wyjscie_sprawdzenie=[]
for i in range(10):
    dane_sprawdzenie,wyjscie_sprawdzenie=odczyt_z_pliku2(str(i))

    
    ############    czytamy
dane_sprawdzenie=np.array(dane_sprawdzenie)
wyjscie_sprawdzenie=np.array(wyjscie_sprawdzenie)

classWeight = compute_class_weight('balanced',np.unique(x_test),x_test)
classWeight = dict(enumerate(classWeight))

history=model.fit(x_train, x_test, epochs=6, verbose=1, validation_data=(dane_sprawdzenie, wyjscie_sprawdzenie))


model.save("pol_model_k6_PoPr_autorska.h5")

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model dokladnosci')
plt.ylabel('dokladnosc')
plt.xlabel('epoka')
plt.legend(['trenowane', 'testowe'], loc='upper left')
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