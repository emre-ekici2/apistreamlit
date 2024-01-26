from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('linear_regression_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    average_value = data['average_value']
    province_name = data['province_name']

    input_data = pd.DataFrame([[average_value, province_name]], columns=['average_value', 'province_name'])

    prediction = model.predict(input_data)

    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
