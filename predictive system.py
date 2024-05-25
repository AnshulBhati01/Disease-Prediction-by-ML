# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users\Adtiya Kumar/Desktop/major project/models/diabetes_model.sav', 'rb'))

input_data = (5,116,74,0,0,25.6,0.201,30)
# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not Diabetic')
else:
  print('The person is Diabetic')
