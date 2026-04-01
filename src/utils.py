import PyPDF2

# PDF reader
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Skill extraction
SKILLS = ["python","sql","machine learning","deep learning",
          "tensorflow","react","java","c++","excel","power bi"]

def extract_skills(text):
    text = text.lower()
    found = [skill for skill in SKILLS if skill in text]
    return found