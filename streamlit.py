import streamlit as st
from flask import Flask, request, jsonify
import joblib
import pandas as pd
from threading import Thread

# Load the model
model = joblib.load('linear_regression_model.joblib')

# Create a Flask app
app = Flask(__name__)

# Define the prediction function
def predict(average_value, province_name):
    input_data = pd.DataFrame([[average_value, province_name]], columns=['average_value', 'province_name'])
    prediction = model.predict(input_data)
    return prediction.tolist()

# Define a route for prediction endpoint
@app.route('/predict', methods=['GET'])
def predict_endpoint():
    # Get data from the request
    data = request.json

    average_value = data['average_value']
    province_name = data['province_name']

    # Make prediction
    prediction = predict(average_value, province_name)

    # Return prediction as JSON
    return jsonify({'prediction': prediction})

def run_flask():
    app.run(debug=True)

if __name__ == '__main__':
    # Run Flask app in a separate thread
    Thread(target=run_flask).start()
