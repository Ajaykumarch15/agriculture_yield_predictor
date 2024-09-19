import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('my_model_linear.pkl')
st.snow()

# Title of the app
st.title("Agricultural Yield Prediction")

# User input for the features
soil_quality = st.number_input('Enter Soil Quality (numeric scale)', min_value=1, max_value=500)
seed_variety = st.number_input('Enter Seed Variety (numeric scale)', min_value=0, max_value=5)
fertilizer_amount = st.number_input('Enter Fertilizer Amount (kg per hectare)', min_value=0.0, step=0.1)
rainfall_mm = st.number_input('Enter Rainfall (mm)', min_value=0.0, step=0.1)
sunny_days = st.number_input('Enter Sunny Days (days)', min_value=0, max_value=365)
irrigation_schedule = st.number_input('Enter Irrigation Schedule (days)', min_value=0, max_value=365)

# Button to predict
if st.button('Predict Yield'):
    # Organize inputs into the correct format for prediction
    input_data = np.array([[soil_quality, seed_variety, fertilizer_amount, sunny_days,rainfall_mm, irrigation_schedule]])

    # Make a prediction
    prediction = model.predict(input_data)

    # Display the result
    st.success(f'Predicted Yield: {prediction[0]:.2f} kg per hectare')
    st.snow()
