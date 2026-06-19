# pyrefly: ignore [missing-import]
from collections import Counter
import csv
import streamlit as st
# pyrefly: ignore [missing-import]
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Travel Recommendation System", layout="wide")

st.title("✈️ Travel & Hotel Recommendation System")
st.markdown("Explore flight data and get personalized hotel recommendations based on your destination.")

# Try to load the recommender model
try:
    recommender_dict = joblib.load('hotel_recommender.joblib')
    st.sidebar.success("Model loaded successfully!")
except Exception as e:
    recommender_dict = {}
    st.sidebar.error("Could not load recommender model. Please run the training notebook first.")

st.header("🏨 Hotel Recommendations")

if recommender_dict:
    # Allow user to pick a destination to get hotel recommendations
    places = list(recommender_dict.keys())
    selected_place = st.selectbox("Select your destination:", places)
    
    if st.button("Get Recommendations"):
        recommendations = recommender_dict.get(selected_place, [])
        if recommendations:
            st.subheader(f"Top Hotels in {selected_place}")
            
            for i, rec in enumerate(recommendations):
                st.markdown(f"**{i+1}. {rec['name']}**")
                st.write(f"- 💵 Average Price per day: ${rec['avg_price']:.2f}")
                st.write(f"- ⭐ Recommendation Score: {rec['score']:.4f}")
                st.markdown("---")
        else:
            st.warning("No recommendations found for this place.")
else:
    st.info("Train the model in the Jupyter Notebook to unlock recommendations.")

st.header("📊 Data Visualizations")
st.markdown("*(Load the CSV files into the app folder to see visualizations here)*")

try:
    prices = []
    flight_types = []
    with open('flights.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                prices.append(float(row['price']))
                flight_types.append(row['flightType'])
            except (ValueError, KeyError):
                pass
    
    st.subheader("Flight Prices Distribution")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.hist(prices, bins=30, color='skyblue', edgecolor='black')
    ax.set_title("Distribution of Flight Prices")
    st.pyplot(fig)
    
    st.subheader("Flight Types")
    type_counts = Counter(flight_types)
    st.bar_chart(type_counts)
    
except Exception as e:
    st.write("Could not load flights data for visualization.")
