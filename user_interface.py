#https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
#https://matplotlib.org/stable/api/figure_api.html
#https://matplotlib.org/stable/users/explain/axes/axes_intro.html
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def plot():
    fig, ax = plt.subplots(figsize=(6, 6))
    x = [3,2,95,24,235,0]
    y = [1,4,3,2,3,5]
    ax.plot(x, y)

    canvas = FigureCanvasTkAgg(fig, master = root)  
    canvas.draw()
    canvas.get_tk_widget().grid()

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

#This function will be run when the user clicks the button
#It decides which graph to display based on the user's inputs
def display_mortality(*args):
    age_value = int(age.get())
    sex_value = sex.get()
    smoker_value = smoker.get()
    if age_value > 0:
        if sex_value == "M":
            if smoker_value == "Y":
                plot()
            elif smoker_value == "N":
                plot()
        elif sex_value == "F":
            if smoker_value == "Y":
                plot()
            elif smoker_value == "N":
                plot()

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

#Button
button = tk.Button(root, text="Display my mortality (old), need to fill in all 3 text boxes above before clicking", command=display_mortality)
button.grid(row = 5, column = 0)

#https://stackoverflow.com/questions/78282970/how-do-i-put-a-html-file-inside-a-python-tkinter-window
def load_website():
    frame.load_website('https://www.google.com')

button = tk.Button(master=root, text='Display my mortality (new), loading random website for now', command=load_website)
button.grid(row = 7, column = 0)

frame = tkinterweb.HtmlFrame(master=root)
frame.grid(row = 8, column = 0)

root.mainloop()
