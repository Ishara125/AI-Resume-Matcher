
from src.resume_pipeline import evaluate_resume
from fastapi import FastAPI, UploadFile, File
import shutil
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://ai-resume-matcher-9peg.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Resume Matcher API is running"}




@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    upload_path = Path("uploads") / file.filename

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result, confidence, skills = evaluate_resume(str(upload_path))

    return {
        "filename": file.filename,
        "prediction": result,
        "confidence": f"{confidence:.2f}%",
        "skills": skills
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Resume Matcher API"
    }

@app.get("/model-info")
def model_info():
    return {
        "model": "RandomForestClassifier",
        "task": "Resume suitability prediction",
        "input_type": "PDF resume",
        "output": ["Suitable", "Not Suitable"],
        "features": [
            "python",
            "sql",
            "machine_learning",
            "power_bi",
            "excel",
            "statistics",
            "java",
            "spring_boot",
            "react",
            "node",
            "mern",
            "docker",
            "aws",
            "education_level",
            "experience_years"
        ]
    }