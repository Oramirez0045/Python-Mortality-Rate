import pandas as pd
import plotly.graph_objects as go
import os

def rename(s):
    self = s
    self = self.replace('.csv', '')
    self = self.replace('_', ' ')
    return self

folder = 'csv'
fileList = os.listdir(folder)

figure = go.Figure()

for file in fileList:
    if file.endswith('.csv'):
        path = os.path.join(folder, file)
        data = pd.read_csv(path)
        data.drop(data.columns[2:], axis=1, inplace=True)
        data.columns = ['Age', 'Mortality Rate']

        figure.add_trace(go.Scatter(
            x = data['Age'],
            y = data['Mortality Rate'],
            mode = 'markers',
            marker = dict(color='darkblue'),
            name = rename(file),
            showlegend = False
        ))

figure.update_layout(
    title = "Mortality Rate",
    xaxis_title = "Age",
    yaxis_title = "Mortality Rate",
    hovermode = "closest"
)
figure.add_vline(
    x = 95,
    line = dict(color="red", width=2),
)
figure.show()
