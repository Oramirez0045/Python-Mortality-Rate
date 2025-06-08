from graph import plotGraph

#https://tkdocs.com/tutorial/firstexample.html
#https://www.geeksforgeeks.org/setting-the-position-of-tkinter-labels/
import tkinter as tk
from tkinter import *
from tkinterweb import HtmlFrame
import os

#main window setup
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

compareGender = tk.BooleanVar()
compareSmoker = tk.BooleanVar()

tk.Checkbutton(root, text = "Compare Gender", variable = compareGender).grid(row = 3, column = 0)
tk.Checkbutton(root, text = "Compare Smoker Status", variable = compareSmoker).grid(row = 4, column = 0)

# Opening html plotly graph with Tkinter (Google Gemini 3 June 2025)
def display_mortality():
    #age with default value = False for control flow
    age_value = age.get()
    age_value = int(age_value) if age_value else False

    #age with default value = False for control flow
    sex_value = sex.get()
    sex_value = sex_value if sex_value else False

    #smoker with default value = False for control flow
    smoker_value = smoker.get()
    smoker_value = smoker_value if smoker_value else False

    compareGenderValue = compareGender.get()
    compareSmokerValue = compareSmoker.get()

    plotGraph(
        gender = sex_value,
        smoker = smoker_value,
        age = age_value,
        compareGender = compareGenderValue,
        compareSmoker = compareSmokerValue
    )
    
    html_file = os.path.abspath("Mortality_Table.html").replace('\\','/')
    frame.load_website(f'file:///{html_file}')

button = tk.Button(root, text="Display My Mortality", command=display_mortality)
button.grid(row = 5, column = 0)

root.mainloop()
