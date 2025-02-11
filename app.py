# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 22:02:09 2025

@author: nraje
"""

import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
# Load the trained model
with open(r"C:\Users\maren\INNOMATICS_327\ML_classes_327\PROJECTS\House_Price_Prediction_Project_1\elite27.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Amarendra Nayak Presents")
st.title("🏡 House Price Prediction App")

# User input fields
square_feet = st.number_input("Enter Square Feet:", min_value=500, max_value=10000, )
bedrooms = st.number_input("Enter Number of Bedrooms:", min_value=1, max_value=10, )
bathrooms = st.number_input("Enter Number of Bathrooms:", min_value=1, max_value=10)
neighborhood = st.selectbox("Select Neighborhood --> 0:Rural  1:Semi Urban   2: Urban:", [0, 1, 2])
year_built = st.number_input("Enter Year Built:", min_value=1900, max_value=2025)

# Predict price
if st.button("Predict Price 💰"):
    user_data = np.array([[square_feet, bedrooms, bathrooms, neighborhood, year_built]], dtype=object)
    prediction = model.predict(user_data)
    st.success(f"🏠 Estimated House Price: ${prediction[0]:,.2f}")

#C:\Users\maren\AppData\Roaming\Python\Python312\Scripts\streamlit.exe run app.py