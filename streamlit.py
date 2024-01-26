import streamlit as st
import requests

API_URL = "http://localhost:5000/predict"  # Update this URL with your API endpoint

def get_prediction(average_value, province_name):
    payload = {
        'average_value': average_value,
        'province_name': province_name
    }
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        prediction = response.json()['prediction']
        return prediction
    else:
        return None

def main():
    st.title('Prediction API Client')

    average_value = st.number_input('Enter average value:')
    province_name = st.text_input('Enter province name:')
    if st.button('Get Prediction'):
        prediction = get_prediction(average_value, province_name)
        if prediction is not None:
            st.write('Prediction:', prediction)
        else:
            st.write('Failed to retrieve prediction.')

if __name__ == '__main__':
    main()
