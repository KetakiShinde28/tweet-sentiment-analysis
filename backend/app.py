from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from preprocess import clean_text

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load('model/sentiment_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    cleaned_text = clean_text(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)
    return jsonify({'sentiment': prediction[0]})  # No int() here since it's already a string like "joy"

if __name__ == '__main__':
    app.run(debug=True)
