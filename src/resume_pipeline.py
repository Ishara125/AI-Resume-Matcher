import joblib
import pandas as pd

from src.pdf_reader import extract_text_from_pdf
from src.text_preprocessing import clean_text
from src.skill_extractor import extract_skills


def evaluate_resume(pdf_path):
    raw_text = extract_text_from_pdf(pdf_path)

    cleaned_text = clean_text(raw_text)

    skills = extract_skills(cleaned_text)

    skills["education_level"] = 3
    skills["experience_years"] = 0

    candidate_df = pd.DataFrame([skills])

    model = joblib.load("model.pkl")

    prediction = model.predict(candidate_df)
    probability = model.predict_proba(candidate_df)

    if prediction[0] == 1:
        result = "Suitable"
        confidence = probability[0][1] * 100
    else:
        result = "Not Suitable"
        confidence = probability[0][0] * 100

    return result, confidence, skills


# Test
if __name__ == "__main__":
    result, confidence, skills = evaluate_resume("resumes/sample_resume.pdf")

    print("Candidate Evaluation")
    print("--------------------")
    print("Prediction :", result)
    print(f"Confidence : {confidence:.2f}%")
    print("Extracted Skills:", skills)