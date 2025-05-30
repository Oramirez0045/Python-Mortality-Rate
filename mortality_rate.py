import pandas as pd
import plotly.graph_objects as go
import plotly.offline as plt
import os

#function looks through csv files, collecting information on how to name the files
def naming(df):
    gender = df.astype(str).apply(lambda col: col.str.contains('Female')).any().any()
    if gender:
        gender = 'Female'
    else:
        genderBlend = df.astype(str).apply(lambda col: col.str.contains('Gender-Blended')).any().any()
        gender = 'Mix' if genderBlend else 'Male'

    smokingStatus = df.astype(str).apply(lambda col: col.str.contains('Nonsmoker')).any().any()
    smokingStatus = 'Non-Smoker' if smokingStatus else 'Smoker'
    
    return gender + ' ' + smokingStatus

folder = 'csv'  #folder with uncleaned csv files (make sure to name this to the folder that contains the csv files)
fileList = os.listdir(folder)

figure = go.Figure()

for file in fileList:
    if file.endswith('.csv'): #only takes in csv files, just in case the folder isnt completely clean
        path = os.path.join(folder, file)
        data = pd.read_csv(path, encoding='windows-1252') #if encoding error, change encoding but i found that this one works

        #uses function to name file
        dfName = naming(data)

        #cleaning data (only gets the second table)
        data = data.iloc[111:, :2].reset_index(drop=True)
        data.columns = ['Age', 'Mortality Rate']

        #conver columns into numeric data (plotly seems to get confused if this isnt true)
        data['Age'] = pd.to_numeric(data['Age'])
        data['Mortality Rate'] = pd.to_numeric(data['Mortality Rate'])

        #adds data to graph
        figure.add_trace(go.Scatter(
            x = data['Age'],
            y = data['Mortality Rate'],
            mode = 'markers',
            marker = dict(color='darkblue'),
            name = dfName,
            showlegend = True
        ))

        #saves info, this could be helpful for user interface so its able to interact and change
        #note this line will save the clean data onto clean_data, either change name or create folder
        data.to_csv(f'clean_data/{dfName}.csv', index=False)

#title and show plot
figure.update_layout(
    title = "Mortality Rate",
    xaxis_title = "Age",
    yaxis_title = "Mortality Rate",
    hovermode = "closest"
)
figure.add_vline(x = 95, line = dict(color = "red", width = 2))
plt.plot(figure, filename = 'Mortality_Table_Plot.html')
