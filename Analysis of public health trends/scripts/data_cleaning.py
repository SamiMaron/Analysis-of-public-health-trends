
import pandas as pd

def load_data(file_path):
    
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    
    df = df.dropna() 
    df['income_per_capita'] = pd.to_numeric(df['income_per_capita'], errors='coerce')
    df['life_expectancy'] = pd.to_numeric(df['life_expectancy'], errors='coerce')
    return df


if __name__ == "__main__":
    df = load_data('../data/who_life_exp.csv')
    df_clean = clean_data(df)
    df_clean.to_csv('../outputs/cleaned_data.csv', index=False)
