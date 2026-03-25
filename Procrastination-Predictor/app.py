import streamlit as st
from src.model import train_model

# Load model
model = train_model()

st.title("🧠 Procrastination Predictor")

# Inputs
study_hours = st.sidebar.slider("Study Hours", 0, 10, 3)
phone_hours = st.sidebar.slider("Phone Hours", 0, 10, 5)
sleep_hours = st.sidebar.slider("Sleep Hours", 0, 10, 6)
assignments_pending = st.sidebar.slider("Assignments Pending", 0, 10, 2)
deadline_days = st.sidebar.slider("Deadline Days", 0, 10, 3)

# Prediction
if st.sidebar.button("Predict"):
    input_data = [[study_hours, phone_hours, sleep_hours, assignments_pending, deadline_days]]
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("⚠️ High Procrastination Risk")
    else:
        st.success("✅ Low Procrastination Risk")