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
                             icons = ['activity', 'heart', 'person'],
                           #starting page
                           default_index=0)

# Diabetes prediction page
if(selected =='Diabetes Prediction'):
    # page title
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
        Diagnosis = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if(Diagnosis[0]==1):
            Diab_Diagnosis= 'The person is diabetic'
        else:
            Diab_Diagnosis= 'The person is not diabetic'

    st.success(Diab_Diagnosis)

# Heart Disease Prediction page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2 = st.columns(2)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col1:
        cp = st.text_input('Chest pain type')
    with col2:
        trestbps = st.text_input('resting blood pressure')
    with col1:
        chol = st.text_input('serum cholestoral in mg/dl')
    with col2:
        fbs = st.text_input('fasting blood sugar')
    with col1:
        restecg = st.text_input('resting electrocardiographic results')
    with col1:
        thalach = st.text_input('maximum heart rate achieved')
    with col2:
        exang = st.text_input('exercise induced angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope = st.text_input('the slope of the peak exercise ST segment')
    with col1:
        ca = st.text_input('number of major vessels colored by flourosopy')
    with col2:
        thal = st.text_input('thal')

        # code for prediction
        Heart_Diagnosis = ''

        if st.button('Heart Disease Test Result'):
           # H_Diagnosis = heart_model.predict([[age, sex, cp,  trestbps,  chol,  fbs,  restecg,  thalach,  exang,
                                               # oldpeak,  slope,  ca,  thal]])
           H_Diagnosis = heart_model.predict([[
               float(age), int(sex), int(cp), float(trestbps), float(chol), int(fbs),
               int(restecg), float(thalach), int(exang), float(oldpeak), float(slope), int(ca), int(thal)
           ]])

        if (H_Diagnosis[0] == 1):
                 Heart_Diagnosis = 'The person has heart disease'
        else:
                Heart_Diagnosis = 'The person does not have heart disease'

        st.success(Heart_Diagnosis)

# Parkinsons Disease Prediction page
if(selected=='Parkinsons Disease Prediction'):
    st.title('Parkinson Disease Prediction using ML')
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
    # code for prediction
    Parkinson_Diagnosis = ''

    if st.button('Parkinson Disease Test Result'):
        P_Diagnosis = parkinsons_model.predict(
            [[float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ),float(DDP),float(Shimmer),float(Shimmer_dB),float(APQ3),float(APQ5),
              float(APQ),float(DDA),float(NHR),float(HNR),float(RPDE),float(DFA),float(spread1),float(spread2),float(D2),float(PPE)]])
        if (P_Diagnosis[0] == 1):
            Parkinson_Diagnosis = 'The person has Parkinson disease'
        else:
            Parkinson_Diagnosis = 'The person does not have parkinson disease'

    st.success(Parkinson_Diagnosis)