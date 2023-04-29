import streamlit as st
import pandas as pd
import numpy as np

# App title and description
st.title("Embolic Stroke of Undetermined Source (ESUS) Criteria Calculator")
st.markdown("""
This app helps you determine if a patient meets the criteria for an Embolic Stroke of Undetermined Source (ESUS), 
which is a specific subtype of ischemic stroke. The criteria include clinical, imaging, and other diagnostic features.

Please input the patient's information and the app will calculate whether the patient meets the ESUS criteria. 
Remember that this app should not replace a professional medical opinion, and it is advised to consult a healthcare 
professional for proper diagnosis and treatment.
""")

# Input patient information
st.header("Patient Information")
age = st.number_input("Age (years)", min_value=1, max_value=120)
sex = st.selectbox("Sex", options=["Male", "Female"])
atrial_fibrillation = st.selectbox("Atrial Fibrillation", options=["Yes", "No"])
previous_stroke = st.selectbox("Previous Stroke", options=["Yes", "No"])
lacunar_stroke = st.selectbox("Lacunar Stroke", options=["Yes", "No"])
imaging_evidence = st.selectbox("Imaging Evidence of ≥1.5 cm Stroke", options=["Yes", "No"])

# Function to calculate ESUS Criteria
def esus_criteria(age, sex, atrial_fibrillation, previous_stroke, lacunar_stroke, imaging_evidence):
    if atrial_fibrillation == "No" and previous_stroke == "No" and lacunar_stroke == "No" and imaging_evidence == "Yes":
        return True
    else:
        return False

# Calculate ESUS Criteria
esus_status = esus_criteria(age, sex, atrial_fibrillation, previous_stroke, lacunar_stroke, imaging_evidence)

# Display results
st.header("Results")
if esus_status:
    st.success("The patient meets the criteria for ESUS.")
else:
    st.error("The patient does not meet the criteria for ESUS.")
