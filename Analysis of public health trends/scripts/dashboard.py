# dashboard.py
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

def create_dashboard(df):
    """
    Creates an interactive dashboard to display the data.
    """
    fig = px.scatter(df, x='income_per_capita', y='life_expectancy', title='Impact of Income Per Capita on Life Expectancy')

    app = dash.Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(children='Health Trend Analysis'),
        dcc.Graph(figure=fig)
    ])

    app.run_server(debug=True)

# Usage:
if __name__ == "__main__":
    df_clean = pd.read_csv('../outputs/cleaned_data.csv')
    create_dashboard(df_clean)
