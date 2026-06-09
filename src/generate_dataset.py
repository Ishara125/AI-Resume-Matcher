import random
import pandas as pd

data = []

for i in range(200):

    python = random.randint(0, 1)
    sql = random.randint(0, 1)
    machine_learning = random.randint(0, 1)
    power_bi = random.randint(0, 1)
    excel = random.randint(0, 1)
    statistics = random.randint(0, 1)
    java = random.randint(0, 1)
    spring_boot = random.randint(0, 1)
    react = random.randint(0, 1)
    node = random.randint(0, 1)
    mern = random.randint(0, 1)
    docker = random.randint(0, 1)
    aws = random.randint(0, 1)

    education_level = random.randint(1, 4)
    experience_years = random.randint(0, 5)

    suitable = 1 if (
        python +
        sql +
        machine_learning +
        statistics +
        power_bi
    ) >= 3 else 0

    data.append([
        python,
        sql,
        machine_learning,
        power_bi,
        excel,
        statistics,
        java,
        spring_boot,
        react,
        node,
        mern,
        docker,
        aws,
        education_level,
        experience_years,
        suitable
    ])

columns = [
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
    "experience_years",
    "suitable"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("dataset/resume_dataset.csv", index=False)

print("Dataset created successfully!")