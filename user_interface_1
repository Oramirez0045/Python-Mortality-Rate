# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 18:36:43 2025

@author: Philip Tan
"""

import numpy as np
from graph import plotGraph
import webbrowser

#https://tkdocs.com/tutorial/firstexample.html
#https://www.geeksforgeeks.org/setting-the-position-of-tkinter-labels/
import tkinter as tk

root = tk.Tk()

#Labels to let the user know how to use the app
age_label = tk.Label(root, text="Age")
age_label.grid(row = 0, column = 0)

sex_label = tk.Label(root, text="Sex (Male/Female)")
sex_label.grid(row = 1, column = 0)

smoker_label = tk.Label(root, text="Smoker? (Y/N)")
smoker_label.grid(row = 2, column = 0)

#User input variables
age = tk.StringVar()
age_entry = tk.Entry(root, textvariable=age)
age_entry.grid(row = 0, column = 5)

sex = tk.StringVar()
sex_entry = tk.Entry(root, textvariable=sex)
sex_entry.grid(row = 1, column = 5)

smoker = tk.StringVar()
smoker_entry = tk.Entry(root, textvariable=smoker)
smoker_entry.grid(row = 2, column = 5)

label = tk.Label(root, text="")
label.grid(row = 6, column = 5)

# Opening html plotly graph with Tkinter (Google Gemini 3 June 2025)
def display_mortality(*args):
    age_value = int(age.get())
    sex_value = sex.get()
    smoker_value = smoker.get()
        
    if (smoker_value == 'Y' or smoker_value == 'N') and (sex_value == 'Male' or sex_value == 'Female') and (age_value >= 18):
        figure = plotGraph(gender = sex_value, smoker = smoker_value)
        html_file = "Mortality_Table.html"
        figure.write_html(html_file)
        
        #"how to locate the y value given x value for a scatter plot you created with plotly.graph_objects" (Google Gemini 7 June 2025)
        #"ndarray how to search for element" (Google Gemini 7 June 2025)
        #https://www.tutorialspoint.com/how-to-change-tkinter-label-text-on-button-press
        #"how to wait in tkinter" (Google Gemini 7 June 2025)
        data = figure.data[0]
        x_values = data.x
        y_values = data.y
        
        target_x = age_value
        
        index_tuple = np.where(x_values == target_x)
        index = index_tuple[0][0]
        y_value = y_values[index]
        label.config(text=f"Your mortality is {y_value}")
        root.after(3000, webbrowser.open, html_file)
        
        #https://www.selectquote.com/life-insurance/articles/life-insurance-classifications
        #https://www.investopedia.com/terms/i/insurance-risk-class.asp
        if age_value < 25 and smoker_value == 'N':
            print("Preferred Plus")
            
        elif age_value < 35 and smoker_value == 'N':
            print("Preferred")
            
        elif age_value < 42 and smoker_value == 'N':
            print("Standard Plus")
            
        elif age_value < 46 and smoker_value == 'N':
            print("Standard")
            
        elif age_value < 25 and smoker_value == 'Y':
            print("Preferred Smoker")
            
        elif age_value < 42 and smoker_value == 'Y':
            print("Standard Smoker")
            
        else:
            print("Rated")

    else:
        label.config(text="Please enter age between 18 and 120, sex as Male/Female, and smoker as Y/N")
        
        
    

button = tk.Button(root, text="Display My Mortality", command=display_mortality)
button.grid(row = 5, column = 0)

root.mainloop()
