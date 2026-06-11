from fastapi import FastAPI
from src.resume_pipeline import result, confidence

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Resume Matcher API is running"}


@app.get("/predict")
def predict():
    return {
        "prediction": result,
        "confidence": f"{confidence:.2f}%"
    }