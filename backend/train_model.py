import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import joblib
from preprocess import clean_text

# Function to load data from .txt
def load_data(filepath):
    texts = []
    labels = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if ';' in line:
                text, label = line.strip().split(';')
                texts.append(clean_text(text))
                labels.append(label)
    return texts, labels

# Load datasets
X_train, y_train = load_data('data/train.txt')
X_val, y_val = load_data('data/val.txt')

# Build pipeline with TF-IDF + Logistic Regression
vectorizer = TfidfVectorizer(max_features=10000)
model = LogisticRegression(max_iter=1000)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_val_vectorized = vectorizer.transform(X_val)

model.fit(X_train_vectorized, y_train)

# Evaluate
preds = model.predict(X_val_vectorized)
print(classification_report(y_val, preds))

# Save model and vectorizer
joblib.dump(model, 'model/sentiment_model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')
