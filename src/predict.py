import joblib
import pandas as pd

model = joblib.load("model.pkl")

candidate = {
    "python": 1,
    "sql": 1,
    "machine_learning": 1,
    "power_bi": 1,
    "excel": 1,
    "statistics": 1,
    "java": 0,
    "spring_boot": 0,
    "react": 0,
    "node": 0,
    "mern": 0,
    "docker": 0,
    "aws": 0,
    "education_level": 3,
    "experience_years": 0
}

candidate_df = pd.DataFrame([candidate])

prediction = model.predict(candidate_df)

print("Prediction:", prediction[0])