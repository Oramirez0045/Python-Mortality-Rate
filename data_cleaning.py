# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 18:51:34 2025

@author: 
"""

#%% Imports
import pandas as pd
import os

#%% Naming function for organization
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

#%% Data Cleaning Function
def cleanData(folderName):
    fileList = os.listdir(folderName)
    

    newpath = r'cleaned_csv' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for file in fileList:
        if file.endswith('.csv'): #only takes in csv files, just in case the folder isnt completely clean
            path = os.path.join(folderName, file)
            data = pd.read_csv(path, encoding='windows-1252') #if encoding error, change encoding but i found that this one works

            #uses function to name file
            dfName = naming(data)

            #cleaning data (only gets the second table)
            data = data.iloc[111:, :2].reset_index(drop=True)
            data.columns = ['Age', 'Mortality Rate']

            #conver columns into numeric data (plotly seems to get confused if this isnt true)
            data['Age'] = pd.to_numeric(data['Age'])
            data['Mortality Rate'] = pd.to_numeric(data['Mortality Rate'])
            
            if 'Mix' in dfName:
                data = data.loc[data['Age'] <= 95]

            #saves info, this could be helpful for user interface so its able to interact and change
            #note this line will save the clean data onto clean_data, either change name or create folder
            data.to_csv(f'cleaned_csv/{dfName}.csv', index=False)
