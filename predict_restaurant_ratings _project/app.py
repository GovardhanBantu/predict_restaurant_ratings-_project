import streamlit as st
import pandas as pd
import numpy as np

# Load model
df = pd.read_csv('restaurant_data.csv')


st.title("🍽️ Restaurant Rating Predictor")

st.markdown("Predict the **Aggregate Rating** of a restaurant based on its features.")

# Input fields
city = st.number_input("City (as encoded number)", min_value=0)
cuisines = st.number_input("Cuisines (as encoded number)", min_value=0)
has_table_booking = st.selectbox("Has Table Booking?", ['No', 'Yes'])
has_online_delivery = st.selectbox("Has Online Delivery?", ['No', 'Yes'])
is_delivering_now = st.selectbox("Is Delivering Now?", ['No', 'Yes'])
price_range = st.selectbox("Price Range", [1, 2, 3, 4])
votes = st.number_input("Number of Votes", min_value=0)

# Convert categorical inputs to numerical
has_table_booking = 1 if has_table_booking == 'Yes' else 0
has_online_delivery = 1 if has_online_delivery == 'Yes' else 0
is_delivering_now = 1 if is_delivering_now == 'Yes' else 0

# Predict button
if st.button("Predict Rating"):
    features = np.array([[city, cuisines, has_table_booking, has_online_delivery,
                          is_delivering_now, price_range, votes]])

    prediction = model.predict(features)[0]
    st.success(f"Predicted Aggregate Rating: ⭐ {round(prediction, 2)}")

