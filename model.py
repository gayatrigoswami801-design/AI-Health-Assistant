import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("symptoms.csv")

# Features
X = data[["fever", "cough", "headache"]]

# Output
y = data["disease"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction function
def predict_disease(symptoms):

    prediction = model.predict([symptoms])

    return prediction[0]