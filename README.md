
# Health Assistant

![Health Assistant](![image](https://github.com/user-attachments/assets/5f8bdc59-f082-48f8-a7d2-d676a418a9bf)
) 

## Overview

The Health Assistant application is a machine learning-based tool designed to predict the likelihood of diabetes, heart disease, and Parkinson's disease in users. Additionally, it provides exercise suggestions tailored to specific diseases, helping users maintain a healthy lifestyle. This application utilizes Streamlit for an interactive web interface and various machine learning models for predictions.

## Features

- **Disease Prediction**: Predicts the likelihood of the following conditions:
  - Diabetes
  - Heart Disease
  - Parkinson's Disease

- **Personalized Exercise Suggestions**: Based on the predicted disease, the application recommends suitable exercises.

- **User-friendly Interface**: Built with Streamlit for an intuitive user experience.

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pickle (for model serialization)

## Installation

To set up the Health Assistant application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/health-assistant.git
   cd health-assistant
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Pre-trained Models**:
   - Ensure that the model files (e.g., `diabetes_model.sav`, `heart_disease_model.sav`, `parkinsons_model.sav`) are available in the project directory.

## Usage

To run the Health Assistant application, execute the following command:

```bash
streamlit run main.py
```

1. Open your web browser and navigate to `http://localhost:8501`.
2. Select the disease prediction you want to perform.
3. Input the required information to receive predictions and exercise suggestions.

## Example Input

### Diabetes Prediction
- Number of Pregnancies: 2
- Glucose Level: 120
- Blood Pressure: 70
- Skin Thickness: 30
- Insulin Level: 200
- BMI: 25
- Diabetes Pedigree Function: 0.5
- Age: 45

### Heart Disease Prediction
- Age: 55
- Sex: 1
- Chest Pain Types: 2
- Resting Blood Pressure: 130
- Serum Cholestoral: 250
- Fasting Blood Sugar > 120 mg/dl: 1
- Resting Electrocardiographic Results: 1
- Maximum Heart Rate Achieved: 150
- Exercise Induced Angina: 0

### Parkinson's Prediction
- MDVP:Fo(Hz): 0.5
- MDVP:Fhi(Hz): 0.6
- Jitter(%): 0.002
- Shimmer: 0.05
- HNR: 20.0
