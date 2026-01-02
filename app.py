import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Set up the app title and description
st.title("Canada Per Capita Income Predictor")
st.write("This app predicts the per capita income for a given year based on historical data.")

# Load the saved model
try:
    with open('income_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please run the notebook to export 'income_model.pkl'.")

# Create a user input for the year
year_input = st.number_input("Enter the Year (e.g., 2025):", min_value=1970, max_value=2100, value=2020)

# Prediction button
if st.button("Predict Income"):
    # Reshape input for the model
    prediction = model.predict([[year_input]])
    
    # Display the result
    st.success(f"The predicted per capita income for {year_input} is ${prediction[0]:,.2f} CAD")

# Optional: Show historical data (requires the original CSV)
if st.checkbox("Show Historical Data"):
    try:
        df = pd.read_csv('canada_per_capita_income.csv')
        st.dataframe(df)
        st.line_chart(df.set_index('year'))
    except FileNotFoundError:
        st.warning("CSV data file not found for visualization.")