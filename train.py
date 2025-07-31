from preprocess import load_and_merge_data
from model import train_model

df = load_and_merge_data('calories.csv', 'exercise.csv')
train_model(df)
print("✅ Model trained and saved as model.pkl")
