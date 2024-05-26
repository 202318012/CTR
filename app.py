from flask import Flask, render_template, request, jsonify
import pandas as pd
from src.predictions import predict

app = Flask(__name__, template_folder='template')

def mock_predict(input_data):
    return {"prediction": "This is a mock prediction based on the input: " + str(input_data)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    try:
        gender = request.form['gender']
        age = request.form['age']
        location = request.form['location']
        usage = request.form['usage']
        edu_level = request.form['edu_level']
        income_level = request.form['income_level']
        language = request.form['language']
        weekends = request.form['weekends']
        weekdays = request.form['weekdays']
        interaction = request.form['interaction']
        ctr = request.form['ctr']
        likes = request.form['likes']
        followed = request.form['followed']


        # X_test = pd.DataFrame({'Age': [age], 'Gender': [gender], 'Location': [location], 'Language': [language], 'Education Level': [edu_level], 'Likes and Reactions': [likes], 'Followed Accounts': [followed], 'Device Usage': [usage], 'Time Spent Online (hrs/weekday)': [weekdays], 'Time Spent Online (hrs/weekend)': [weekends], 'Click-Through Rates (CTR)': [ctr], 'Ad Interaction Time (sec)': [interaction], 'Income Level': [income_level]})
        X_test = pd.DataFrame({'Age': [age], 'Gender': [gender], 'Location': [location], 'Language': [language], 'Education Level': [edu_level], 'Likes and Reactions': [likes], 'Followed Accounts': [followed], 'Device Usage': [usage], 'Time Spent Online (hrs/weekday)': [weekdays], 'Time Spent Online (hrs/weekend)': [weekends], 'Click-Through Rates (CTR)': [ctr], 'Ad Interaction Time (sec)': [interaction], 'Income Level': [income_level]})

        prediction = predict(X_test)
        
        return render_template('index.html', predicted = f'{prediction} %')


    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
