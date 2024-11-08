# model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(df):
    """
    Trains a linear regression model to predict life expectancy based on income per capita.
    """
    X = df[['income_per_capita']]
    y = df['life_expectancy']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error (MSE): {mse:.2f}')

# Usage:
if __name__ == "__main__":
    df_clean = pd.read_csv('../outputs/cleaned_data.csv')
    train_model(df_clean)
