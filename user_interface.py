# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 18:36:43 2025

@author: Philip Tan
"""

from tkinter import font
from graph import plotGraph
import tkinter as tk

#https://tkdocs.com/tutorial/firstexample.html
#https://www.geeksforgeeks.org/setting-the-position-of-tkinter-labels/

root = tk.Tk()

#Labels to let the user know how to use the app
age_label = tk.Label(root, text="Age")
age_label.grid(row = 0, column = 0)

gender_label = tk.Label(root, text="Gender (Male/Female)")
gender_label.grid(row = 1, column = 0)

smoker_label = tk.Label(root, text="Smoker? (Y/N)")
smoker_label.grid(row = 2, column = 0)

#User input variables
age = tk.StringVar()
age_entry = tk.Entry(root, textvariable=age)
age_entry.grid(row = 0, column = 1)

gender = tk.StringVar()
gender_entry = tk.Entry(root, textvariable=gender)
gender_entry.grid(row = 1, column = 1)

smoker = tk.StringVar()
smoker_entry = tk.Entry(root, textvariable=smoker)
smoker_entry.grid(row = 2, column = 1)

mortality_label = tk.Label(root, text="")
mortality_label.grid(row = 5, column = 1)

premium_label = tk.Label(root, text="")
premium_label.grid(row = 6, column = 1)

compareGender = tk.BooleanVar()
compareSmoker = tk.BooleanVar()

tk.Checkbutton(root, text = "Compare Gender", variable = compareGender).grid(row = 3, column = 0)
tk.Checkbutton(root, text = "Compare Smoker Status", variable = compareSmoker).grid(row = 4, column = 0)

# Opening html plotly graph with Tkinter (Google Gemini 3 June 2025)
#This function takes in the user's inputs and calls the plotGraph function to show the HTML file in the user's browser
#It doesn't return anything explicitly
def display_mortality(*args):
    
    #age with default value = False for control flow
    age_value = age.get()
    age_value_check = age.get()
    age_value = int(age_value) if age_value else False

    #age with default value = False for control flow
    gender_value = gender.get()
    gender_value_check = gender.get()
    gender_value = gender_value if gender_value else False

    #smoker with default value = False for control flow
    smoker_value = smoker.get()
    smoker_value_check = smoker.get()
    smoker_value = smoker_value if smoker_value else False
    
    compareGenderValue = compareGender.get()
    compareSmokerValue = compareSmoker.get()
    
    #This if statement checks if the user made some valid inputs
    if (smoker_value_check == 'Y' or smoker_value_check == 'N' or smoker_value_check == '') and (gender_value_check == 'Male' or gender_value_check == 'Female' or gender_value_check == '') and ((age_value >= 18 and age_value <=120) or age_value_check == ''):
        plotGraph(
                gender = gender_value,
                smoker = smoker_value,
                age = age_value,
                compareGender = compareGenderValue,
                compareSmoker = compareSmokerValue
            )
    
    #I used this to figure out why my labels weren't updating correctly https://www.tutorialspoint.com/how-to-change-tkinter-label-text-on-button-press
    else:
        #This serves as an error message to let the user know they need to change some inputs
        mortality_label.config(text="Please enter age between 18 and 120 or leave blank, gender as Male/Female or leave blank, and smoker as Y/N or leave blank")

#This function takes in the user's inputs from the GUI and then uses that to output the premium
#It doesn't return anything explicitly and just displays labels
def display_premium(*args):
    premium_label.config(text=" ")
    
    #age with default value = False for control flow
    age_value = age.get()
    #The age_value needs to be converted into an int before it can be compared to other ints in the if statement
    age_value = int(age_value) if age_value else False

    #age with default value = False for control flow
    gender_value = gender.get()
    gender_value = gender_value if gender_value else False

    #smoker with default value = False for control flow
    smoker_value = smoker.get()
    smoker_value_check = smoker.get()
    smoker_value = smoker_value if smoker_value else False
    
    #I used these websites to learn about premiums and for sample premium data.
    #https://www.selectquote.com/life-insurance/articles/life-insurance-classifications
    #https://www.investopedia.com/terms/i/insurance-risk-class.asp
    #https://www.quotacy.com/what-are-life-insurance-risk-classifications/
    #The numbers inside monthly_premiums dictionary were taken from https://www.ethos.com/life/life-insurance-rates-by-age/
    #I used this series of if statements to output the corresponding expected premium based on the user's age and smoking status
    #Since the data only provides age values of every 10 years, I had to infer that ages between those values would have premiums also in between those values.
    monthly_premiums = {'Age': [25,35,45,55,65], 'Non-smoker': [58,65,135,316,790], 'Smoker': [123,137,332,982,2540]}
    if (smoker_value_check == 'Y' or smoker_value_check == 'N') and ((age_value >= 18 and age_value <=120)):
        if (smoker_value == 'N'):
            if age_value < monthly_premiums['Age'][0]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be at most ${monthly_premiums['Non-smoker'][0]}")
            elif age_value < monthly_premiums['Age'][1]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be between ${monthly_premiums['Non-smoker'][0]} and ${monthly_premiums['Non-smoker'][1]}")
            elif age_value < monthly_premiums['Age'][2]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be between ${monthly_premiums['Non-smoker'][1]} and ${monthly_premiums['Non-smoker'][2]}")
            elif age_value < monthly_premiums['Age'][3]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be between ${monthly_premiums['Non-smoker'][2]} and ${monthly_premiums['Non-smoker'][3]}")
            elif age_value < monthly_premiums['Age'][4]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be between ${monthly_premiums['Non-smoker'][3]} and ${monthly_premiums['Non-smoker'][4]}")
            else:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be greater than ${monthly_premiums['Non-smoker'][4]}")
        if (smoker_value == 'Y'):
            if age_value < monthly_premiums['Age'][0]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be at most ${monthly_premiums['Smoker'][0]}")
            elif age_value < monthly_premiums['Age'][1]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be between ${monthly_premiums['Smoker'][0]} and ${monthly_premiums['Smoker'][1]}")
            elif age_value < monthly_premiums['Age'][2]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be between ${monthly_premiums['Smoker'][1]} and ${monthly_premiums['Smoker'][2]}")
            elif age_value < monthly_premiums['Age'][3]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be between ${monthly_premiums['Smoker'][2]} and ${monthly_premiums['Smoker'][3]}")
            elif age_value < monthly_premiums['Age'][4]:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be between ${monthly_premiums['Smoker'][3]} and ${monthly_premiums['Smoker'][4]}")
            else:
                premium_label.config(text=f"For a $1,000,000 death benefit & 10-year term policy, your approximate monthly premium will be greater than ${monthly_premiums['Smoker'][4]}")
    else:
        premium_label.config(text="Please enter age between 18 and 120 and smoker as Y/N for premium calculation")

mortality_button = tk.Button(root, text="Display My Mortality", command=display_mortality, bg = "light green")
mortality_button.grid(row = 5, column = 0)

premium_button = tk.Button(root, text="Calculate My Premium", command=display_premium, bg = "light green")
premium_button.grid(row = 6, column = 0)

#Spacing apart widgets (ChatGPT 8 June 2025)
#Increasing text size (ChatGPT 8 June 2025)
#Changing font styles (ChatGPT 8 June 2025)
#Changing button colors (ChatGPT 8 June 2025)
#I used this to explore fonts: https://mockuuups.studio/blog/post/best-fonts-for-apps/
#This for loop selects all of the widgets I created, since I used the grid manager in Tkinter
#Then it creates some spacing between each one and modifies all of the labels to change their font size and style
for widget in root.grid_slaves():
    widget.grid_configure(padx = 10, pady = 10)
    if isinstance(widget, tk.Label):
        current_font = font.nametofont(widget.cget("font"))
        current_font.configure(size = current_font.cget("size") + 1, family = "Inter")
        widget.config(font = current_font)

root.mainloop()
