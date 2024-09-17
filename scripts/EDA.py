import pandas as pd
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# To format the data
def format_data(df):
    # Convert object columns to string 
    object_columns = df.select_dtypes(include='object').columns
    df[object_columns] = df[object_columns].astype(str)

    # Convert TransactionMonth to datetime 
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    
    return df


# to plot the variablity of numerical columns
def plot_stats(data):
    variables = list(data.columns)
    measurements = ['Range', 'Variance', 'Standard Deviation']
    colors = ['red', 'green', 'blue']
    
    if len(variables) > len(colors):
        colors = colors * (len(variables) // len(colors) + 1)

    fig = go.Figure()

    for i, variable in enumerate(variables):
        values = data.loc[:, variable].values
        fig.add_trace(go.Bar(
            x=measurements,
            y=values,
            name=variable,
            marker_color=colors[i]
        ))

    fig.update_layout(
        title='Measurements for Variables',
        xaxis_title='Measurement',
        yaxis_title='Value'
    )
    fig.update_layout(width=800, height=600)
    fig.show()
