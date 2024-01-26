from flask import Flask, request, jsonify
from socketserver import ThreadingMixIn
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('linear_regression_model.joblib')

app = Flask(__name__)

class ThreadingFlaskServer(ThreadingMixIn, Flask):
    pass

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    average_value = data['average_value']
    province_name = data['province_name']
    input_data = pd.DataFrame([[average_value, province_name]], columns=['average_value', 'province_name'])
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app = ThreadingFlaskServer(__name__)
    app.run(debug=True)
