import streamlit as st
from model import predict_calories

st.set_page_config(page_title="Calories Burnt Predictor", layout="centered")

st.title(" Calories Burnt Prediction App")

with st.form("user_input"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=10, max_value=100)
    weight = st.number_input("Weight (kg)", min_value=20)
    height = st.number_input("Height (cm)", min_value=100)
    walk_km = st.number_input("Walking Distance (km)", min_value=0.0)
    run_km = st.number_input("Running Distance (km)", min_value=0.0)
    exercise_hr = st.number_input("Exercise Duration (hours)", min_value=0.0)

    submitted = st.form_submit_button("Predict")

if submitted:
    calories, heartbeat = predict_calories(gender, age, weight, height, walk_km, run_km, exercise_hr)
    st.success(f"Estimated Heartbeat Rate: {heartbeat:.2f} bpm")
    st.success(f"Calories Burnt: {calories:.2f} kcal")
