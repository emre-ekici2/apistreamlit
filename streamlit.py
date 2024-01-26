import streamlit as st
import joblib
import pandas as pd
import requests

# Load the pre-trained model
model = joblib.load('linear_regression_model.joblib')

def get_prediction(average_value, province_name):
    input_data = pd.DataFrame([[average_value, province_name]], columns=['average_value', 'province_name'])
    prediction = model.predict(input_data)
    return prediction.tolist()

def main():
    st.title('Prediction API Client')

    average_value = st.number_input('Enter average value:')
    province_name = st.text_input('Enter province name:')
    
    if st.button('Get Prediction'):
        payload = {
            'average_value': average_value,
            'province_name': province_name
        }
        response = requests.post('https://apiapp-group3-warninglevels.streamlit.app/', json=payload) 
        if response.status_code == 200:
            prediction = response.json()['prediction']
            st.write('Prediction:', prediction)
        else:
            st.write('Failed to retrieve prediction.')

if __name__ == '__main__':
    main()
