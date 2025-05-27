import pandas as pd
import plotly.graph_objects as go
import os

#function will look through csv file to find information on how to name a variable 
def naming(df):
    gender = df.astype(str).apply(lambda col: col.str.contains('Female', case=False, na=False)).any().any()
    if gender == True:
        gender = 'Female'
    else:
        gender = df.astype(str).apply(lambda col: col.str.contains('Gender-Blended', case=False, na=False)).any().any()
        if gender == True:
            gender = 'Mix'
        if gender != 'Mix':
            gender = 'Male'
            
    smokingStatus = df.astype(str).apply(lambda col: col.str.contains('Nonsmoker', case=False, na=False)).any().any()
    if smokingStatus:
        smokingStatus = 'Non-Smoker'
    else:
        smokingStatus = 'Smoker'
    return gender + ' ' + smokingStatus

folder = 'unclean_csv' #make sure to change this into the folder name that your csv files are in
fileList = os.listdir(folder)

figure = go.Figure()

for file in fileList:
    if file.endswith('.csv'):
        #code to navigate towards csv folder
        path = os.path.join(folder, file)
        data = pd.read_csv(path, encoding = 'windows-1252')
        
        #uses function to find information within the file to create a name
        name = naming(data)
        
        #data cleaning
        data = data.iloc[111:, :2].reset_index(drop = True)  # Keep only the first two columns
        data.columns = ['Age', 'Mortality Rate']
        
        #columns are originally objects and confuses plotly
        data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
        data['Mortality Rate'] = pd.to_numeric(data['Mortality Rate'], errors='coerce')

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
