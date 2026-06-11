
from src.resume_pipeline import evaluate_resume
from fastapi import FastAPI, UploadFile, File
import shutil
from pathlib import Path
app = FastAPI()


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