# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 19:43:38 2025

@author: suave
"""

'''
the idea behind the control flow would be to create different destinctions behind
each data that is imported
1. Checks for Smoker status
    - this is to create a distinction between mixed data sets and gender-specific
      data
2. Check for Gender Status
    - if gender remains null but smoker isnt, program assumes you only want to
      see smoker data in which case itll only show mixed data sets
    - if gender isnt empty, it moves on to verify which type of gender to show
      specific data
3. Checks for age
    - if age is empty, entire data is outline to make it stand out
    - if age is not empty, one data point will be highlighed
'''

from data_cleaning import cleanData
import plotly.graph_objects as go
import pandas as pd
import os
import plotly.offline as pltoff

def keyword(word, dataName):
    return word in dataName

cleanData('unclean_csv') #input folder name with UNCLEANED csv files to become clean

def plotGraph(gender = False, age = False, smoke = False, printAll = False, printGenders = False):
    folder = 'cleaned_csv' #make sure to change this into the folder name that your CLEAN csv files are in
    fileList = os.listdir(folder)
    figure = go.Figure()
    
    for file in fileList:
        #setting default values that could be changed if conditions are met
        markColor = 'darkblue'
        modeType = 'markers'
        
        if file.endswith('.csv'):
            path = os.path.join(folder, file)
            data = pd.read_csv(path, encoding = 'windows-1252')
            
            if smoke != False:
                if gender != False:
                    if gender == 'F':
                        if keyword('Female', file):
                            modeType = 'lines+markers'
                            figure.add_trace(go.Scatter(
                                x = data['Age'],
                                y = data['Mortality Rate'],
                                mode = modeType,
                                marker = dict(color = markColor),
                                name = file,
                                showlegend = True))
                else:
                    if keyword('Mix',file):
                        modeType = 'lines+markers'
                        figure.add_trace(go.Scatter(
                            x = data['Age'],
                            y = data['Mortality Rate'],
                            mode = modeType,
                            marker = dict(color = markColor),
                            name = file,
                            showlegend = True
                        ))
            else:
                figure.add_trace(go.Scatter(
                    x = data['Age'],
                    y = data['Mortality Rate'],
                    mode = modeType,
                    marker = dict(color = markColor),
                    name = file,
                    showlegend = True))
                
            if printAll:
                figure.add_trace(go.Scatter(
                    x = data['Age'],
                    y = data['Mortality Rate'],
                    mode = modeType,
                    marker = dict(color = markColor),
                    name = file,
                    showlegend = True))
            
    figure.update_layout(
    title = "Mortality Rate",
    xaxis_title = "Age",
    yaxis_title = "Mortality Rate",
    hovermode = "closest")
    
    figure.add_vline(x = 95, line = dict(color = "red", width = 2))
    pltoff.plot(figure, filename = 'Mortality_Table.html')
    
plotGraph(gender = 'F', smoke = 'N', printAll = True)
