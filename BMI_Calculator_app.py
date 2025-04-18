import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .title {
        color: #4CAF50; /* Green color for title */
        background-color: #f0f0f0; /* Light grey background */
        padding: 10px;
        border-radius: 5px;
    }
    .input-label {
        color: #2196F3; /* Blue color for input labels */
    }
    .bmi-result {
        color: #FF5722; /* Deep orange color for BMI result */
        font-weight: bold;
        background-color: #FFF9C4; /* Light yellow background for BMI result */
        padding: 15px;
        border-radius: 5px;
        font-size: 24px; /* Larger font size */
        text-align: center; /* Center align the BMI result */
    }
    .category {
        color: #673AB7; /* Purple color for categories */
    }
    .button-blur {
        filter: blur(2px); /* Blur effect for the button */
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 BMI Calculator 🌟", anchor=None)
st.markdown("<div class='title'>Please enter your details below to calculate your BMI:</div>", unsafe_allow_html=True)
height = st.number_input("📏 Enter your height (in cm):", min_value=100, max_value=250, value=175, format="%d")
weight = st.number_input("⚖️ Enter your weight (in kg):", min_value=40, max_value=200, value=70, format="%d")

if st.button("Calculate", help="Click to calculate your BMI", key="calculate_button"):
    bmi = weight / ((height / 100) ** 2)
    st.markdown(f"<div class='bmi-result'>💡 YOUR BMI IS: **{bmi:.2f}**</div>", unsafe_allow_html=True)
    st.balloons()

st.markdown("<div class='category'>### 📊 BMI CATEGORIES ###</div>", unsafe_allow_html=True)
st.write("_ **UNDERWEIGHT:** BMI LESS THAN 18.5")
st.write("_ **NORMAL WEIGHT:** BMI BETWEEN 18.5 AND 24.9")
st.write("_ **OVERWEIGHT:** BMI BETWEEN 25 AND 29.9")
st.write("_ **OBESITY:** BMI OF 30 AND GREATER")