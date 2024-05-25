# -*- coding: utf-8 -*-
"""
Created on Mon May 20 02:26:41 2024

@author: Adtiya Kumar
"""

import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users\Adtiya Kumar/Desktop/major project/models/heart_disease_model.sav', 'rb'))

input_data = (63,1,0,130,330,1,0,132,1,1.8,2,3,3)
# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')