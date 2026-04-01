import os
import pickle
import sys

sys.path.append(os.path.dirname(__file__))

from preprocessing import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, "models/model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "models/vectorizer.pkl"), "rb"))

def predict_resume(text):
    text = clean_text(text)
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    prob = max(model.predict_proba(X)[0])
    return pred, prob