import streamlit as st

def calculate_bmi(weight, height):
    bmi = (weight / (height**2)) * 703
    return bmi

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in pounds:")
height_ft = st.number_input("Enter your height in feet:")
height_in = st.number_input("Enter your height in inches:")

if weight and height_ft and height_in:
    height = (height_ft * 12) + height_in
    bmi = calculate_bmi(weight, height)
    st.write("Your BMI is:", bmi)
