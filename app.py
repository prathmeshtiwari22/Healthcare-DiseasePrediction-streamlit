import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Exercise Suggestion'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'exercise'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# Exercise suggestions dataset
exercises = {
    'Diabetes': "1. Walking\n2. Cycling\n3. Swimming\n4. Aerobic exercises",
    'Heart Disease': "1. Walking\n2. Jogging\n3. Cycling\n4. Light weight training",
    'Parkinson\'s': "1. Stretching\n2. Dancing\n3. Yoga\n4. Balance exercises",
    'Hypertension': "1. Brisk walking\n2. Cycling\n3. Swimming\n4. Yoga",
    'Asthma': "1. Walking\n2. Yoga\n3. Swimming (in warm water)\n4. Breathing exercises",
    'Osteoporosis': "1. Weight-bearing exercises\n2. Resistance training\n3. Tai Chi\n4. Dancing",
    'Arthritis': "1. Low-impact aerobic exercises\n2. Strength training\n3. Swimming\n4. Stretching",
    'Back Pain': "1. Walking\n2. Stretching\n3. Core strengthening\n4. Yoga",
    'Depression': "1. Aerobic exercises\n2. Yoga\n3. Dance\n4. Hiking",
    'Anxiety': "1. Yoga\n2. Tai Chi\n3. Walking\n4. Pilates",
    'Chronic Fatigue Syndrome': "1. Low-impact aerobics\n2. Stretching\n3. Swimming\n4. Walking",
    'Fibromyalgia': "1. Gentle aerobic exercises\n2. Stretching\n3. Yoga\n4. Water aerobics",
    'Multiple Sclerosis': "1. Stretching\n2. Walking\n3. Swimming\n4. Balance exercises",
    'COPD': "1. Walking\n2. Breathing exercises\n3. Cycling\n4. Swimming",
    'Obesity': "1. Walking\n2. Swimming\n3. Cycling\n4. Aerobic exercises",
    'Kidney Disease': "1. Walking\n2. Yoga\n3. Cycling (low intensity)\n4. Stretching",
    'Liver Disease': "1. Walking\n2. Light aerobics\n3. Cycling\n4. Yoga",
    'Cancer': "1. Walking\n2. Yoga\n3. Tai Chi\n4. Stretching",
    'Epilepsy': "1. Low-impact aerobics\n2. Yoga\n3. Walking\n4. Swimming",
    'Dementia': "1. Walking\n2. Dancing\n3. Gardening\n4. Balance exercises",
    'Allergies': "1. Walking\n2. Cycling\n3. Swimming\n4. Stretching",
    'Scleroderma': "1. Range-of-motion exercises\n2. Swimming\n3. Stretching\n4. Tai Chi",
    'Celiac Disease': "1. Walking\n2. Yoga\n3. Swimming\n4. Light resistance training",
    'Gout': "1. Low-impact aerobics\n2. Swimming\n3. Walking\n4. Stretching",
    'Bipolar Disorder': "1. Aerobic exercises\n2. Yoga\n3. Walking\n4. Dance",
    'PTSD': "1. Yoga\n2. Walking\n3. Tai Chi\n4. Mindfulness meditation",
    'Hyperthyroidism': "1. Light aerobic exercises\n2. Stretching\n3. Yoga\n4. Walking",
    'Hypothyroidism': "1. Walking\n2. Resistance training\n3. Yoga\n4. Swimming",
    'Pneumonia': "1. Breathing exercises\n2. Walking (as tolerated)\n3. Stretching\n4. Light aerobics",
    'Sickle Cell Disease': "1. Low-impact aerobics\n2. Swimming\n3. Walking\n4. Stretching",
    'Insomnia': "1. Yoga\n2. Walking\n3. Relaxation techniques\n4. Breathing exercises",
    'Vertigo': "1. Balance exercises\n2. Tai Chi\n3. Walking\n4. Yoga",
    'Carpal Tunnel Syndrome': "1. Wrist stretches\n2. Hand strengthening\n3. Yoga\n4. Swimming",
    'Tendonitis': "1. Stretching\n2. Strength training\n3. Low-impact aerobics\n4. Swimming",
    'Plantar Fasciitis': "1. Stretching\n2. Low-impact aerobics\n3. Swimming\n4. Walking",
    'Menopause': "1. Walking\n2. Yoga\n3. Aerobic exercises\n4. Strength training",
    'Pregnancy': "1. Walking\n2. Swimming\n3. Prenatal yoga\n4. Light strength training",
    'Acid Reflux': "1. Walking\n2. Yoga\n3. Stretching\n4. Low-impact aerobics",
    'Irritable Bowel Syndrome': "1. Yoga\n2. Walking\n3. Tai Chi\n4. Swimming",
    'Schizophrenia': "1. Walking\n2. Yoga\n3. Aerobic exercises\n4. Mindfulness",
    'HIV/AIDS': "1. Walking\n2. Yoga\n3. Stretching\n4. Low-impact aerobics",
    'Psoriasis': "1. Swimming\n2. Yoga\n3. Walking\n4. Stretching",
    'Ulcerative Colitis': "1. Walking\n2. Yoga\n3. Light aerobics\n4. Swimming",
    'Lyme Disease': "1. Gentle yoga\n2. Walking\n3. Swimming\n4. Tai Chi",
    'Cushing\'s Syndrome': "1. Light aerobic exercises\n2. Yoga\n3. Walking\n4. Stretching",
    'Addison\'s Disease': "1. Gentle yoga\n2. Walking\n3. Stretching\n4. Low-impact aerobics",
    'Thyroid Cancer': "1. Walking\n2. Light resistance training\n3. Yoga\n4. Swimming",
    'Aortic Aneurysm': "1. Light walking\n2. Swimming (gentle)\n3. Stretching\n4. Yoga",
    'Chronic Sinusitis': "1. Breathing exercises\n2. Yoga\n3. Walking\n4. Stretching",
    'Raynaud\'s Disease': "1. Gentle exercises (indoors)\n2. Swimming\n3. Stretching\n4. Yoga",
    'Rheumatoid Arthritis': "1. Swimming\n2. Low-impact aerobics\n3. Stretching\n4. Tai Chi",
}

# Modify the chatbot section in your existing Streamlit code
if selected == 'Exercise Suggestion':
    st.title('Exercise Suggestion Chatbot')

    # Input for disease
    disease_input = st.text_input('Enter your disease (e.g., Diabetes, Heart Disease, Parkinson\'s):')

    # Button to get exercise suggestion
    if st.button('Get Exercise Suggestion'):
        if disease_input:
            suggestion = exercises.get(disease_input, "Sorry, I don't have suggestions for that disease.")
            st.success(f"Suggested exercises for {disease_input}:\n{suggestion}")
        else:
            st.warning("Please enter a disease to get exercise suggestions.")

