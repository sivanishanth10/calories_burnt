import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

def train_model(df):
    df = df.copy()
    
    # Encode Gender
    df['Gender'] = LabelEncoder().fit_transform(df['Gender'])
    
    X = df[['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']]
    y = df['Calories']
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    joblib.dump(model, 'model.pkl')
    return model

def predict_calories(gender, age, weight, height, walk_km, run_km, exercise_hr):
    import numpy as np
    model = joblib.load('model.pkl')
    
    gender = 1 if gender == 'Male' else 0
    duration = exercise_hr * 60  # in minutes
    avg_heart_rate = 100 + (run_km * 5) + (walk_km * 2)
    temp = 36.5 + (run_km * 0.1)

    features = np.array([[gender, age, height, weight, duration, avg_heart_rate, temp]])
    prediction = model.predict(features)[0]
    
    return prediction, avg_heart_rate
