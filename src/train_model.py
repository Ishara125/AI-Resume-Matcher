import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
# Load the dataset
df = pd.read_csv("dataset/resume_dataset.csv")

# Input features
X = df.drop("suitable", axis=1)

# Target column
y = df["suitable"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create the model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")
joblib.dump(model, "model.pkl")
print("Model saved successfully!")