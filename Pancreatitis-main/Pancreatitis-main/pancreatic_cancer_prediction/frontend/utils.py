import google.generativeai as genai
import os
import re

# Set your Google AI API Key
GEMINI_API_KEY = "AIzaSyAOKiUnn6rl4fUkyPjcYE1LYRZLsuIqiVo"  # Replace with your actual API key

# Configure the API
genai.configure(api_key=GEMINI_API_KEY)

def get_ai_prediction(input_data):
    """
    Queries Google Gemini AI (gemini-1.5-pro-latest) and extracts only the risk percentage and risk level.
    """
    prompt = f"""
    You are a medical assistant AI. Based on the following patient details, provide a **numeric risk percentage** and classify as "High Risk" or "Low Risk".
    
    Patient Details:
    - Age: {input_data['Age']}
    - Gender: {"Male" if input_data['Gender'] == 1 else "Female"}
    - BMI: {input_data['BMI']}
    - Alcohol Consumption (units per week): {input_data['Alcohol_Consumption']}
    - Smoking Habit: {"Yes" if input_data['Smoking_Habit'] == 1 else "No"}
    - Cholesterol Level: {input_data['Cholesterol_Level']}
    - Blood Sugar Level: {input_data['Blood_Sugar_Level']}
    
    **Response Format (STRICTLY FOLLOW THIS FORMAT):**
    ```
    Risk Percentage: XX.X%
    Risk Level: High Risk / Low Risk
    ```
    """
    
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        text_response = response.text.strip()

        # Extract percentage and risk level using regex
        percentage_match = re.search(r"Risk Percentage: (\d+(\.\d+)?)%", text_response)
        level_match = re.search(r"Risk Level: (High Risk|Low Risk)", text_response)

        if percentage_match and level_match:
            risk_percentage = float(percentage_match.group(1))
            risk_level = level_match.group(1)
            return risk_percentage, risk_level
        else:
            return None, f"Error: Gemini response format incorrect. Full response:\n{text_response}"
    except Exception as e:
        return None, f"Error: {e}"
