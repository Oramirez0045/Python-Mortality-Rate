from graph import plotGraph
import webbrowser

#https://tkdocs.com/tutorial/firstexample.html
#https://www.geeksforgeeks.org/setting-the-position-of-tkinter-labels/
import tkinter as tk
from tkinter import *
import tkinterweb

root = tk.Tk()

#Labels to let the user know how to use the app
age_label = tk.Label(root, text="Age")
age_label.grid(row = 0, column = 0)

sex_label = tk.Label(root, text="Sex (M/F)")
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


# Opening html plotly graph with Tkinter (Google Gemini 3 June 2025)
def display_mortality(*args):
    age_value = int(age.get())
    sex_value = sex.get()
    smoker_value = smoker.get()
    
    a = plotGraph(gender = sex_value, smoke = smoker_value, printAll = True)
    
    html_file = "Mortality_Table.html"
    a.write_html(html_file)
    webbrowser.open(html_file)

button = tk.Button(root, text="Display My Mortality", command=display_mortality)
button.grid(row = 5, column = 0)

root.mainloop()
