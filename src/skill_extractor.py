def extract_skills(cleaned_text):
    skills = {
        "python": 1 if "python" in cleaned_text else 0,
        "sql": 1 if "sql" in cleaned_text else 0,
        "machine_learning": 1 if "machine learning" in cleaned_text else 0,
        "power_bi": 1 if "power bi" in cleaned_text else 0,
        "excel": 1 if "excel" in cleaned_text else 0,
        "statistics": 1 if "statistics" in cleaned_text else 0,
        "java": 1 if "java" in cleaned_text else 0,
        "spring_boot": 1 if "spring boot" in cleaned_text else 0,
        "react": 1 if "react" in cleaned_text else 0,
        "node": 1 if "node" in cleaned_text else 0,
        "mern": 1 if "mern" in cleaned_text else 0,
        "docker": 1 if "docker" in cleaned_text else 0,
        "aws": 1 if "aws" in cleaned_text else 0,
    }

    return skills