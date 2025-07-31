import pandas as pd

def load_and_merge_data(calories_path, exercise_path):
    df_calories = pd.read_csv(calories_path)
    df_exercise = pd.read_csv(exercise_path)
    
    # Merge on 'User_ID' if that's the key (adjust based on actual file columns)
    df = pd.merge(df_exercise, df_calories, on='User_ID')
    
    return df
