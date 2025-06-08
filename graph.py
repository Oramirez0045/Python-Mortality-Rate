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

def plotGraph(gender = False, age = False, smoker = False, compareGender = False, compareSmoker = False):
    #makes sure user enters the correct words
    if gender not in ['Male', 'Female',False]:
        raise ValueError("Gender must be 'Male', 'Female', or left empty")
    if smoker not in ['Y','N',False]:
        raise ValueError("Smoker Status must be 'Y' for yes, 'N' for no, or left empty")
                         
    #allowing program to access files
    folder = 'cleaned_csv'
    fileList = os.listdir(folder)

    #creating graph
    figure = go.Figure()
    
    for file in fileList:
        if not file.endswith('.csv'):
            continue

        #accessing individual file and using pandas to read it
        path = os.path.join(folder, file)
        data = pd.read_csv(path, encoding = 'windows-1252')

        #control flow, if gender inputted, only allow that file to continue, else True to allow everything (same for smoker)
        genderMatch = gender in file if gender else True
        smokerMatch = (
            ('Non' in file and smoker == 'N') or 
            ('Smoker' in file and 'Non' not in file and smoker == 'Y')
        ) if smoker else True

        #comparing checkboxes in UI
        compareGenderMatch = False
        compareSmokerMatch = False

        #creates a comparison line for the compare gender checkbox
        if compareGender:
            #assures that a gender has been inputted and check mark wasnt pressed on accident
            if gender:
                #case 1: gender specified
                oppositeGender = 'Male' if gender == 'Female' else 'Female'
                compareGenderMatch = (
                    oppositeGender in file and (
                        ('Non' in file and smoker == 'N') or
                        ('Smoker' in file and 'Non' not in file and smoker == 'Y')
                    )
                )
            else:
                #case 2: gender not specified
                compareGenderMatch = ('Male' in file or 'Female' in file)

        #creates a comparison line for the compare smoker checkbox
        if compareSmoker:
            if smoker:
                if smoker == 'N':
                    compareSmokerMatch = (('Smoker' in file and 'Non' not in file) and
                                          (gender in file if gender else True))
                else:
                    compareSmokerMatch = ('Smoker' in file or 'Non' in file)

        #checking which other files to include in graph, in case compare checkboxes are marked
        include_file = (
            (genderMatch and smokerMatch) or
            compareGenderMatch or
            compareSmokerMatch)

        if include_file:
            comparing = compareGenderMatch or compareSmokerMatch
            markColor = 'gray' if comparing else 'darkblue'

            #creating traces for all data
            figure.add_trace(go.Scatter(
                x = data['Age'],
                y = data["Mortality Rate"],
                mode = 'markers' if comparing else 'lines+markers',
                marker = dict(color = markColor),
                name = file,
                showlegend = True
            ))

            #marking age if an age is inputted
            if age:
                match = data[data['Age'] == age]
                if not match.empty:
                    userRate = match.iloc[0]['Mortality Rate']
                    figure.add_trace(go.Scatter(
                        x = [age],
                        y = [userRate],
                        mode = 'markers',
                        marker = dict(color = 'red', size = 12),
                        name = 'User Age',
                        showlegend = True
                    ))

    #marking graphs details
    figure.update_layout(
    title = "Mortality Rate",
    xaxis_title = "Age",
    yaxis_title = "Mortality Rate",
    hovermode = "closest")

    #creating maximum insurance policy line
    figure.add_vline(x = 95, line = dict(color = "red", width = 2))
    pltoff.plot(figure, filename = 'Mortality_Table.html')
