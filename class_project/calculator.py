# bmi_calculator.py

import streamlit as st

st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("BMI Calculator")

# User input
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=1.0, step=0.1)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.info("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")

