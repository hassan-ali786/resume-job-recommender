import pandas as pd
import pickle
import os
import sys

sys.path.append(os.path.dirname(__file__))

from preprocessing import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "resumes.csv")
model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

os.makedirs(os.path.join(BASE_DIR, "models"), exist_ok=True)

# Load dataset
df = pd.read_csv(data_path)

# Fix columns (IMPORTANT)
df = df.rename(columns={
    "Resume": "resume_text",
    "Category": "category"
})

# Clean text
df["resume_text"] = df["resume_text"].apply(clean_text)

X = df["resume_text"]
y = df["category"]

# Vectorize
vectorizer = TfidfVectorizer(max_features=5000)
X_vect = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_vect, y)

# Save
pickle.dump(model, open(model_path, "wb"))
pickle.dump(vectorizer, open(vectorizer_path, "wb"))

print("Model trained successfully")