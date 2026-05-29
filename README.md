# Resume Job Recommender

An intelligent web application that automatically matches resumes to relevant job postings using Natural Language Processing (NLP) and similarity-based recommendation techniques. Built with Streamlit for an interactive and user-friendly experience.

---

## Live Demo:
https://resume-job-recommender-ovbmfzmfxzylcedghofmaa.streamlit.app/

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
│ └── resumes.csv
├── models/
│ ├── model.pkl
│ └── vectorizer.pkl
├── src/
│ ├── preprocessing.py
│ ├── train_model.py
│ ├── predict.py
│ └── utils.py
├── images/
│   └── homepage.png
    └── result.png
├── app.py
└── requirements.txt
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

## Future Improvements

- Integration with real job APIs  
- Support for PDF/DOC resume uploads  
- Advanced NLP models (BERT, embeddings)  
- User profile and history tracking

 ---

##  Application Screenshots

![Home](https://raw.githubusercontent.com/hassan-ali786/resume-job-recommender/main/images/homepage.png)
![Result](https://raw.githubusercontent.com/hassan-ali786/resume-job-recommender/main/images/result.png)

---

## Author

Hassan Ali 

Data Scientist & Machine Learning Engineer

---

## License

This project is open-source and available under the MIT License.

---
