# procrastination-predictor-ml
A Machine Learning project that predicts student procrastination based on daily habits using a Decision Tree model with a Streamlit web interface.
Procrastination Predictor

Overview

This project predicts whether a student is likely to procrastinate using Machine Learning techniques. It analyzes daily habits and behavioral patterns to classify the risk of procrastination.

Objective

The main objective of this project is to develop a predictive model that helps identify procrastination behavior based on key lifestyle factors and promotes better time management.

Features

- Predicts procrastination risk (High or Low)
- Uses Decision Tree Machine Learning model
- Interactive user interface built with Streamlit
- Simple and easy-to-use design

Input Parameters

The model takes the following inputs:

- Study Hours
- Phone Usage Hours
- Sleep Hours
- Assignments Pending
- Deadline Days

Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit

Project Structure

Procrastination-Predictor/
│── data/
│   └── procrastination_data.csv
│── src/
│   └── model.py
│── app.py
│── requirements.txt
│── README.md

Installation

1. Clone the repository or download the project folder
2. Open the project in VS Code or any IDE
3. Install required libraries using:

pip install -r requirements.txt

How to Run

Run the following command in terminal:

streamlit run app.py

Then open the local URL displayed in the terminal.

Output

The system predicts whether the user has a high or low risk of procrastination based on the provided inputs.

Dataset

The dataset used in this project is manually created and contains features such as study hours, phone usage, sleep hours, assignments pending, and deadline days.

Limitations

- Small dataset size
- Data is manually created
- May not fully represent real-world scenarios

Future Scope

- Use real-world data collection
- Improve model accuracy
- Add more behavioral features such as stress level and motivation
- Develop a mobile application

Conclusion

This project demonstrates how Machine Learning can be used to analyze and predict human behavior. It provides insights into procrastination patterns and helps users improve productivity and time management.
<img width="1920" height="1080" alt="procrastination-predictor-proof" src="https://github.com/user-attachments/assets/f514acf7-6a3b-445b-bb01-b6d6e44e6ea9" />
