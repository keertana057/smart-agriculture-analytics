import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import joblib

# LOAD DATASET

df = pd.read_csv(
    "cleaned_data/clean_crop_recommendation.csv"
)

# FEATURES

X = df[
    [
        'N',
        'P',
        'K',
        'temperature',
        'humidity',
        'ph',
        'rainfall'
    ]
]

# TARGET
y = df['label']

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# MODEL
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# TRAIN MODEL
model.fit(X_train, y_train)

# PREDICTIONS
y_pred = model.predict(X_test)

# ACCURACY
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nMODEL ACCURACY:\n")
print(
    round(accuracy * 100, 2),
    "%"
)

# CLASSIFICATION REPORT
print("\nCLASSIFICATION REPORT:\n")
print(
    classification_report(
        y_test,
        y_pred
    )
)

# SAVE MODEL
joblib.dump(
    model,
    "crop_prediction_model.pkl"
)
print(
    "\nModel Saved Successfully"
)

# SAMPLE PREDICTION
sample_data = pd.DataFrame([{
    'N': 90,
    'P': 42,
    'K': 43,
    'temperature': 21.0,
    'humidity': 82.0,
    'ph': 6.5,
    'rainfall': 203.0
}])
prediction = model.predict(
    sample_data
)

print("\nPREDICTED CROP:")
print(prediction[0])