import streamlit as st
import joblib
import numpy as np

model = joblib.load("salary_prediction_model.pkl")

st.title("🎓 Student Salary Prediction")

cgpa = st.number_input("CGPA")
coding = st.number_input("Coding Skill Score")
internships = st.number_input("Internships Count")
aptitude = st.number_input("Aptitude Score")
mock = st.number_input("Mock Interview Score")

if st.button("Predict Salary"):
    data = np.array([[cgpa, coding, internships, aptitude, mock]])
    prediction = model.predict(data)
    st.success(f"Predicted Salary: {prediction[0]:.2f} LPA")