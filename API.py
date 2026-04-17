from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

modelo = pickle.load(open('modelo.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    pred = modelo.predict([data['input']])
    return jsonify({'prediccion': pred.tolist()})

app.run()
