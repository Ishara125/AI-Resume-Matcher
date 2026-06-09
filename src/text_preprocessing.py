import re


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text


sample_text = "Python, SQL, Machine Learning!!!"

cleaned = clean_text(sample_text)

print(cleaned)