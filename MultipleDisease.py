import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model

diabetes_model = pickle.load(open('trained_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# create webpage sidebars for navigation

with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction'],
                            icons= ['activity', 'heart', 'person'],
                           #starting page
                           default_index=0)

# Diabetes prediction page
if(selected =='Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediciton using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('BP value')
    with col1:
        SkinThickness = st.text_input('Skin thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age')

    #code for prediction
    Diab_Diagnosis = ''

    if st.button('Diabetes Test Result'):
        Diagnosis = diabetes_prediction(
            [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        if(Diagnosis[0]==1):
            Diab_Diagnosis= 'The person is diabetic'
        else:
            Diab_Diagnosis= 'The person is not diabetic'

    st.success(Diab_Diagnosis)

# Heart Disease Prediction page
if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    col1, col2= st.columns(2)
    with col1:
        age: st.text_input('Age')
    with col2:
        sex: st.text_input('Sex')
    with col1:
        cp: st.text_input('Chest pain type')
    with col2:
        trestbps: st.text_input('resting blood pressure')
    with col1:
        chol: st.text_input('serum cholestoral in mg/dl')
    with col2:
        fbs: st.text_input('fasting blood sugar')
    with col1:
        restecg: st.text_input('resting electrocardiographic results (values 0,1,2)')
    with col1:
        thalach: st.text_input('maximum heart rate achieved')
    with col2:
        exang: st.text_input('exercise induced angina')
    with col1:
        oldpeak: st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope: st.text_input('the slope of the peak exercise ST segment')
    with col1:
        ca: st.text_input('number of major vessels (0-3) colored by flourosopy')
    with col2:
        thal: st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        # code for prediction
        Heart_Diagnosis = ''

        if st.button('Heart Disease Test Result'):
            H_Diagnosis = diabetes_prediction(
                [age,  sex,  cp,  trestbps,  chol,  fbs,  restecg,  thalach,  exang,  oldpeak,  slope,  ca,  thal])
            if (H_Diagnosis[0] == 1):
                Heart_Diagnosis = 'The person has heart disease'
            else:
                Heart_Diagnosis = 'The person does not have heart disease'

        st.success(Heart_Diagnosis)

# Parkinsons Disease Prediction page
if(selected=='Parkinsons Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    Fo:st.text_input(' Average vocal fundamental frequency')
    Fhi:st.text_input(' Maximum vocal fundamental frequency')
    Flo:st.text_input(' Minimum vocal fundamental frequency')
    Jitter:st.text_input('Jitter(%) - Percentage of cycle-to-cycle variability of the period duration')
    Abs: st.text_input('Jitter(Abs) - Absolute value of cycle-to-cycle variability of the period duration')
    RAP:st.text_input('Relative measure of the pitch disturbance')
    PPQ:st.text_input(' Pitch perturbation quotient')
    DDP:st.text_input(' Average absolute difference of differences between jitter cycles')
    Shimmer:st.text_input('Variations in the voice amplitude')
    APQ:st.text_input('APQ')
    DDA:st.text_input('DDA')
    NHR:st.text_input(' Noise-to-harmonics Ratio and')
    HNR:st.text_input('Harmonics-to-noise Ratio')
    RPDE:st.text_input(' Recurrence period density entropy')
    DFA:st.text_input('Signal fractal scaling exponent')
    spread1:st.text_input('discrete probability distribution of occurrence of relative semitone variations')
    spread2:st.text_input('Three nonlinear measures of fundamental frequency variation')
    D2:st.text_input('correlation dimension')
    PPE:st.text_input('Entropy of the discrete probability distribution of occurrence of relative semitone variations')

    # code for prediction
    Parkinson_Diagnosis = ''

    if st.button('Heart Disease Test Result'):
        P_Diagnosis = diabetes_prediction(
            [Fo,Fhi,Flo,Jitter,Abs,RAP,PPQ,DDP,Shimmer,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])
        if (H_Diagnosis[0] == 1):
            Parkinson_Diagnosis = 'The person has Parkinson disease'
        else:
            Parkinson_Diagnosis = 'The person does not have parkinson disease'

    st.success(Parkinson_Diagnosis)