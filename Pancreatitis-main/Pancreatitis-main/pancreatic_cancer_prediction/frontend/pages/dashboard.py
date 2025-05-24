import streamlit as st
import matplotlib.pyplot as plt
from utils import get_ai_prediction  # Get risk percentage from AI

# Set Page Config
st.set_page_config(page_title="Personal Risk Prediction | Dashboard", layout="wide")

# Title
st.markdown("<h1 class='title'>📊 Personal Risk Prediction | Dashboard</h1>", unsafe_allow_html=True)

# User Input Section
st.markdown("### 🔍 Enter Your Details")
age = st.number_input("Age", min_value=20, max_value=90, value=50)
gender = st.selectbox("Gender", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
alcohol = st.number_input("Alcohol Consumption (units per week)", min_value=0, max_value=50, value=5)
smoking = st.selectbox("Smoking Habit", ["Yes", "No"])
cholesterol = st.number_input("Cholesterol Level", min_value=100, max_value=300, value=150)
blood_sugar = st.number_input("Blood Sugar Level", min_value=50, max_value=300, value=100)

# Convert Categorical Inputs to Numeric Values
gender_map = {"Male": 1, "Female": 0}
smoking_map = {"Yes": 1, "No": 0}

# Store Inputs as Dictionary
input_data = {
    "Age": age,
    "Gender": gender_map[gender],
    "BMI": bmi,
    "Alcohol_Consumption": alcohol,
    "Smoking_Habit": smoking_map[smoking],
    "Cholesterol_Level": cholesterol,
    "Blood_Sugar_Level": blood_sugar
}

# Prediction Button
if st.button("🔍 Get AI Prediction"):
    risk_percentage, risk_level = get_ai_prediction(input_data)

    if risk_percentage is not None:
        st.subheader("AI Risk Assessment")
        st.metric(label="Risk Percentage", value=f"{risk_percentage:.1f}%")

        # Generate Pie Chart
        fig, ax = plt.subplots()
        labels = ["Probability of Having Pancreatic Cancer", "Probability of Not Having It"]
        values = [risk_percentage, 100 - risk_percentage]
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff6666', '#66b3ff'])
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        
        st.pyplot(fig)
    else:
        st.error("Error: Could not generate risk prediction.")

st.markdown("</div>", unsafe_allow_html=True)
