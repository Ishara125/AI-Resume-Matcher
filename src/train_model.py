import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix
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

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Confusion Matrix:")
print(matrix)

print("Model trained successfully!")
joblib.dump(model, "model.pkl")
print("Model saved successfully!")