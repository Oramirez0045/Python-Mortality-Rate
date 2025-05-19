#https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def plot():

    fig = Figure(figsize = (5, 5), dpi = 100)

    y = [i for i in range(500)]

    plot1 = fig.add_subplot(111)

    plot1.plot(y)

    canvas = FigureCanvasTkAgg(fig, master = root)  
    canvas.draw()

    canvas.get_tk_widget().grid(column=2, row=5, sticky=(W, E))

    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar = False)
    toolbar.update()

    canvas.get_tk_widget().grid(column=2, row=5, sticky=(W, E))

###############################################################################################################

#https://tkdocs.com/tutorial/firstexample.html
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        age_value = float(age.get())
        sex_value = sex.get()
        smoker_value = smoker.get()
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
    except ValueError:
        pass

root = Tk()
root.title("Mortality Based on Age, Sex, and Smoking Status")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

age = StringVar()
age_entry = ttk.Entry(mainframe, width=7, textvariable=age)
age_entry.grid(column=2, row=1, sticky=(W, E))

sex = StringVar()
sex_entry = ttk.Entry(mainframe, width=7, textvariable=sex)
sex_entry.grid(column=2, row=2, sticky=(W, E))

smoker = StringVar()
smoker_entry = ttk.Entry(mainframe, width=7, textvariable=smoker)
smoker_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="Age").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Sex (M/F)").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Smoker? (Y/N)").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="You projected mortality is").grid(column=1, row=5, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

age_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
