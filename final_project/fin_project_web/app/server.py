from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

# читаем модель из файла
with open('models/fpro_pipeline.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg

@app.route('/predict', methods=['POST'])
def predict_func():
	features = request.json
	cols = ['status','baths','sqft','zipcode','beds','stories','type_of_house','age_of_house']
	features_f = pd.DataFrame([features], columns=cols)
	predict = model.predict(features_f)
	return jsonify({'prediction': round(np.exp(predict[0]))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)