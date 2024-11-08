# data_analysis.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_data(df):
    
    correlation = df['income_per_capita'].corr(df['life_expectancy'])
    print(f"Correlation between per capita income and life expectancy: {correlation:.2f}")

    # גרף פיזור
    sns.scatterplot(x='income_per_capita', y='life_expectancy', data=df)
    plt.title('The effect of per capita income on life expectancy')
    plt.show()

if __name__ == "__main__":
    df_clean = pd.read_csv('../outputs/cleaned_data.csv')
    analyze_data(df_clean)
