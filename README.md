# Resume Job Recommender

An intelligent web application that automatically matches resumes to relevant job postings using Natural Language Processing (NLP) and similarity-based recommendation techniques. Built with Streamlit for an interactive and user-friendly experience.

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-purple?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-blue?logo=numpy)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green)

---

## Key Features

- Resume parsing and text preprocessing  
- Job recommendation using similarity scoring  
- NLP-based feature extraction  
- Displays top matching job roles  
- Interactive and simple UI with Streamlit  
- Fast and lightweight implementation  

---

## Project Structure

```
resume-job-recommender/
│
├── data/
│ └── jobs.csv
├── models/
│ ├── model.pkl
│ └── vectorizer.pkl
├── src/
│ ├── preprocessing.py
│ ├── train_model.py
│ ├── predict.py
│ ├── utils.py
│ └── matcher.py
├── images/
│   └── homepage.png
    └── result.png
├── app.py
├── requirements.txt
└── run.bat
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/hassan-ali786/resume-job-recommender.git
cd resume-job-recommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## How It Works

1. User uploads or pastes resume text  
2. Text is cleaned and preprocessed  
3. Features are extracted using NLP techniques  
4. Similarity is calculated between resume and job descriptions  
5. Top matching job recommendations are displayed  

---

## Machine Learning & NLP

- Text Vectorization: TF-IDF  
- Similarity Measure: Cosine Similarity  
- Libraries:
  - scikit-learn  
  - NLTK / basic NLP preprocessing  

---

## Requirements

```
streamlit
pandas
numpy
scikit-learn
nltk
```

---


## Use Cases

- Job recommendation systems  
- Resume screening automation  
- NLP portfolio project  
- Career guidance tools  

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository  
2. Create a new branch  
3. Submit a pull request  

---

## License

This project is open-source and available under the MIT License.

---

## Author

Hassan Ali 
Data Science and Machine Learning Enthusiast  

---

## Future Improvements

- Integration with real job APIs  
- Support for PDF/DOC resume uploads  
- Advanced NLP models (BERT, embeddings)  
- User profile and history tracking  
