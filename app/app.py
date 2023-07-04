from flask import Flask, render_template,request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	float_features = [float(value) for key, value in request.form.items()]
	features = [float_features]
	prediction = model.predict(features)
	return render_template("index.html", prediction_text = prediction[0].upper())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)