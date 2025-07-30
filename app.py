import streamlit as st
import pandas as pd
import joblib

# Load pipeline
pipeline = joblib.load("income_pipeline_balanced.pkl")

# ---- Page Config ----
st.set_page_config(page_title="Incometer", page_icon="💰", layout="wide")

# ---- Title Section ----
st.markdown("""
<h1 style='text-align:center; color:#4CAF50; font-size:65px; font-weight:900;'>
    Incometer 💵
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; font-size:20px; color:#555;'>
    Predict Your Earnings Potential Instantly.
</p>
""", unsafe_allow_html=True)

# ---- Layout: Two Columns ----
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔹 Basic Information")
    age = st.number_input("Age", 17, 90)
    education_num = st.number_input("Education Number (1-16)", 1, 16)
    hours_per_week = st.number_input("Hours per Week", 1, 100)

    with st.expander("🔹 Financial Details"):
        capital_gain = st.number_input("Capital Gain", 0, 100000)
        capital_loss = st.number_input("Capital Loss", 0, 100000)

    with st.expander("🔹 Work & Education"):
        workclass = st.selectbox("Workclass", [
            "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov",
            "Local-gov", "State-gov", "Without-pay", "Never-worked"
        ])
        education = st.selectbox("Education", [
            "Bachelors", "Some-college", "11th", "HS-grad", "Prof-school",
            "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th",
            "Masters", "1st-4th", "10th", "Doctorate", "5th-6th",
            "Preschool"
        ])
        occupation = st.selectbox("Occupation", [
            "Tech-support", "Craft-repair", "Other-service", "Sales",
            "Exec-managerial", "Prof-specialty", "Handlers-cleaners",
            "Machine-op-inspct", "Adm-clerical", "Farming-fishing",
            "Transport-moving", "Priv-house-serv", "Protective-serv",
            "Armed-Forces"
        ])
        marital_status = st.selectbox("Marital Status", [
            "Married-civ-spouse", "Divorced", "Never-married", "Separated",
            "Widowed", "Married-spouse-absent", "Married-AF-spouse"
        ])

    with st.expander("🔹 Demographics"):
        relationship = st.selectbox("Relationship", [
            "Wife", "Own-child", "Husband", "Not-in-family",
            "Other-relative", "Unmarried"
        ])
        race = st.selectbox("Race", [
            "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"
        ])
        sex = st.selectbox("Sex", ["Male", "Female"])
        native_country = st.selectbox("Native Country", [
            "United-States", "Cambodia", "England", "Puerto-Rico", "Canada",
            "Germany", "Outlying-US(Guam-USVI-etc)", "India", "Japan",
            "Greece", "South", "China", "Cuba", "Iran", "Honduras",
            "Philippines", "Italy", "Poland", "Jamaica", "Vietnam",
            "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic",
            "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary",
            "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia",
            "El-Salvador", "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"
        ])

# ---- Create DataFrame ----
# ---- Create DataFrame ----
input_data = pd.DataFrame([{
    "age": age,
    "workclass": workclass,
    "education": education,
    "education.num": education_num,        # must match training
    "marital.status": marital_status,      # must match training
    "occupation": occupation,
    "relationship": relationship,
    "race": race,
    "sex": sex,
    "capital.gain": capital_gain,          # must match training
    "capital.loss": capital_loss,          # must match training
    "hours.per.week": hours_per_week,      # must match training
    "native.country": native_country,
    "fnlwgt": 1                             # <-- Add dummy value
}])
      # must match training




# ---- Prediction ----
with col2:
    st.subheader("Prediction")
    if st.button("Predict Income 🚀"):
        proba = pipeline.predict_proba(input_data)[0][1]  # probability of >50K
        
        # Adjusted threshold
        result = ">50K" if proba >= 0.4 else "<=50K"


        if result == ">50K":
            st.markdown(
                "<div style='padding:20px; background-color:#C8E6C9; text-align:center; border-radius:10px;'>"
                "<h3 style='color:#2E7D32;'>Predicted Income: >50K</h3></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div style='padding:20px; background-color:#FFCDD2; text-align:center; border-radius:10px;'>"
                "<h3 style='color:#B71C1C;'>Predicted Income: <=50K</h3></div>",
                unsafe_allow_html=True
            )
