
# Multiple Disease Prediction System

This repository contains a Streamlit-based web application for predicting the likelihood of three different conditions using machine learning models: **Diabetes**, **Heart Disease**, and **Parkinson's Disease**.

## Overview

This app allows users to input specific medical data for each condition and receive a diagnosis based on trained models. The models used are:

- **Diabetes Prediction Model**: Predicts diabetes using parameters such as glucose levels, BMI, and age.
- **Heart Disease Prediction Model**: Uses factors like cholesterol levels, resting blood pressure, and age for prediction.
- **Parkinson’s Disease Prediction Model**: Predicts Parkinson’s disease based on voice-related parameters.
- 
## Requirements

- Python 3.x
- Streamlit
- streamlit-option-menu
- scikit-learn
- TensorFlow/Keras
- Pickle (for loading models)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repo/Multiple-Disease-Prediction-System.git
   cd Multiple-Disease-Prediction-System
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have the trained models in the working directory:

   - `trained_model.sav` for Diabetes Prediction
   - `heart_disease_model.sav` for Heart Disease Prediction
   - `parkinsons_model.sav` for Parkinson’s Disease Prediction

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open the app in your web browser (usually at `http://localhost:8501`).

3. Use the sidebar to select a prediction type and enter the required data.

4. Click the **Test Result** button to receive the prediction.

## Models Training

The models were trained using various datasets specific to each disease:

- **Diabetes Dataset**: Includes features like glucose levels, blood pressure, and BMI.
- **Heart Disease Dataset**: Uses features such as age, cholesterol levels, and maximum heart rate.
- **Parkinson’s Dataset**: Consists of voice measurements like jitter, shimmer, and HNR.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Datasets were obtained online from reliable medical data repositories.
- Models were trained using `scikit-learn` and `TensorFlow/Keras`.

---

Make sure to adjust the repository URL, dataset details, and any other specifics based on your project setup.
