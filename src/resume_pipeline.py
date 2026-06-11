import joblib
import pandas as pd

from src.pdf_reader import extract_text_from_pdf
from src.text_preprocessing import clean_text
from src.skill_extractor import extract_skills


# Step 1: Read PDF
pdf_path = "resumes/sample_resume.pdf"
raw_text = extract_text_from_pdf(pdf_path)

# Step 2: Clean text
cleaned_text = clean_text(raw_text)

# Step 3: Extract skills
skills = extract_skills(cleaned_text)

# Step 4: Add remaining features
skills["education_level"] = 3
skills["experience_years"] = 0

# Step 5: Convert to DataFrame
candidate_df = pd.DataFrame([skills])

# Step 6: Load trained model
model = joblib.load("model.pkl")

# Step 7: Predict
prediction = model.predict(candidate_df)
probability = model.predict_proba(candidate_df)

# Step 8: Display result
if prediction[0] == 1:
    result = "Suitable"
    confidence = probability[0][1] * 100
else:
    result = "Not Suitable"
    confidence = probability[0][0] * 100

print("Candidate Evaluation")
print("--------------------")
print("Prediction :", result)
print(f"Confidence : {confidence:.2f}%")