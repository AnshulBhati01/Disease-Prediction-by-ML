import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️"
)

# Add custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #FFEFD5;
    }
    .sidebar .sidebar-content {
        background-color: #f7f7f7;
        padding: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .stTextInput>div>div>input {
        padding: 10px;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        font-size: 16px;
        width: 100%;
    }
    .compact-row .stTextInput {
        margin-bottom: 10px;
    }
    h1, h2 {
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open('C:/Users/Adtiya Kumar/Desktop/major project/models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Adtiya Kumar/Desktop/major project/models/heart_disease_model.sav', 'rb'))
cardiovascular_model = pickle.load(open('C:/Users/Adtiya Kumar/Downloads/cardiovascular_model.sav', 'rb'))

# Option menu in the center of the page
with st.container():
    st.markdown("<h1 style='text-align: center;'>Select Disease</h1>", unsafe_allow_html=True)
    selected_option = option_menu(
        '',
        ['Diabetes Prediction', 'Hypertension Prediction', 'Cardiovascular Disease Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person']
    )

# Display input fields based on the selected option
if selected_option:
    if selected_option == 'Diabetes Prediction':
        st.title('Diabetes Prediction using ML')
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                Pregnancies = st.text_input('Number of Pregnancies', key='Pregnancies')
                SkinThickness = st.text_input('Skin Thickness value', key='SkinThickness')
                DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', key='DiabetesPedigreeFunction')
            with col2:
                Glucose = st.text_input('Glucose Level', key='Glucose')
                Insulin = st.text_input('Insulin Level', key='Insulin')
                Age = st.text_input('Age of the Person', key='Age')
            with col3:
                BloodPressure = st.text_input('Blood Pressure value', key='BloodPressure')
                BMI = st.text_input('BMI value', key='BMI')

        # Code for Prediction
        diab_diagnosis = ''
        # Creating a button for Prediction
        if st.button('Diabetes Test Result'):
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)

    elif selected_option == 'Hypertension Prediction':
        st.title('Hypertension Prediction using ML')
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                age = st.text_input('Age (In Years)', key='age')
                trestbps = st.text_input('Resting Blood Pressure 94-200 (in mm HG)', key='trestbps')
                restecg = st.text_input('Resting Electrocardiographic results', key='restecg')
                oldpeak = st.text_input('ST depression induced by exercise', key='oldpeak')
            with col2:
                sex = st.text_input('Sex 1,0(0= female, 1 = male)', key='sex')
                chol = st.text_input('Serum Cholestoral in mg/dl', key='chol')
                thalach = st.text_input('Maximum Heart Rate achieved', key='thalach')
                slope = st.text_input('Slope of the peak exercise ST segment', key='slope')
            with col3:
                cp = st.text_input('Chest Pain types', key='cp')
                fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', key='fbs')
                exang = st.text_input('Exercise Induced Angina', key='exang')
                ca = st.text_input('Major vessels colored by flourosopy', key='ca')
                thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', key='thal')

        # Code for Prediction
        heart_diagnosis = ''
        # Creating a button for Prediction
        if st.button('Heart Disease Test Result'):
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

        st.success(heart_diagnosis)

    elif selected_option == 'Cardiovascular Disease Prediction':
        st.title('Cardiovascular Disease Prediction using ML')
        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                age = st.text_input('Age', key='age')
                restingBP = st.text_input('Resting Blood Pressure', key='restingBP')
                restingrelectro = st.text_input('Resting Electrocardiographic results', key='restingrelectro')
                oldpeak = st.text_input('ST depression induced by exercise', key='oldpeak')
            with col2:
                gender = st.text_input('Gender', key='gender')
                serumcholestrol = st.text_input('Serum Cholestoral in mg/dl', key='serumcholestrol')
                maxheartrate = st.text_input('Maximum Heart Rate achieved', key='maxheartrate')
                slope = st.text_input('Slope of the peak exercise ST segment', key='slope')
            with col3:
                chestpain = st.text_input('Chest Pain types', key='chestpain')
                fastingbloodsugar = st.text_input('Fasting Blood Sugar > 120 mg/dl', key='fastingbloodsugar')
                exerciseangia = st.text_input('Exercise Induced Angina', key='exerciseangia')
                noofmajorvessels = st.text_input('Major vessels colored by flourosopy', key='noofmajorvessels')

        # Code for Prediction
        cardiovascular_diagnosis = ''
        # Creating a button for Prediction
        if st.button('Cardiovascular Disease Test Result'):
            user_input = [age, gender, chestpain, restingBP, serumcholestrol, fastingbloodsugar, restingrelectro, maxheartrate, exerciseangia, oldpeak, slope, noofmajorvessels]
            user_input = [float(x) for x in user_input]
            cardiovascular_prediction = cardiovascular_model.predict([user_input])

            if cardiovascular_prediction[0] == 1:
                cardiovascular_diagnosis = 'The person is having cardiovascular disease'
            else:
                cardiovascular_diagnosis = 'The person does not have any cardiovascular disease'

        st.success(cardiovascular_diagnosis)

# Add this section to handle the case when no option is selected
else:
    st.markdown("<h2 style='text-align: center;'>Please select a disease prediction option from the menu above.</h2>", unsafe_allow_html=True)
