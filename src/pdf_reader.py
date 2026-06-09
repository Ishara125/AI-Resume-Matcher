import pdfplumber

pdf_path = "resumes/sample_resume.pdf"

with pdfplumber.open(pdf_path) as pdf:
    text = ""

    for page in pdf.pages:
        text += page.extract_text()

print(text)