# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 18:36:43 2025

@author: Philip Tan
"""

from tkinter import font
from graph import plotGraph

#https://tkdocs.com/tutorial/firstexample.html
#https://www.geeksforgeeks.org/setting-the-position-of-tkinter-labels/
import tkinter as tk

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
        
    if (smoker_value_check == 'Y' or smoker_value_check == 'N' or smoker_value_check == '') and (gender_value_check == 'Male' or gender_value_check == 'Female' or gender_value_check == '') and ((age_value >= 18 and age_value <=120) or age_value_check == ''):
        plotGraph(
                gender = gender_value,
                smoker = smoker_value,
                age = age_value,
                compareGender = compareGenderValue,
                compareSmoker = compareSmokerValue
            )
        
        #https://www.tutorialspoint.com/how-to-change-tkinter-label-text-on-button-press
        
    else:
        mortality_label.config(text="Please enter age between 18 and 120 or leave blank, gender as Male/Female or leave blank, and smoker as Y/N or leave blank")

def display_premium(*args):
    premium_label.config(text=" ")
    
    #age with default value = False for control flow
    age_value = age.get()
    age_value = int(age_value) if age_value else False

    #age with default value = False for control flow
    gender_value = gender.get()
    gender_value = gender_value if gender_value else False

    #smoker with default value = False for control flow
    smoker_value = smoker.get()
    smoker_value_check = smoker.get()
    smoker_value = smoker_value if smoker_value else False
    
    #https://www.selectquote.com/life-insurance/articles/life-insurance-classifications
    #https://www.investopedia.com/terms/i/insurance-risk-class.asp
    #https://www.quotacy.com/what-are-life-insurance-risk-classifications/
    #https://www.ethos.com/life/life-insurance-rates-by-age/
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

#chatgpt "how to space apart all preexisting items in tkinter after using grid manager" June 8 2025
#chatgpt "how to increase text size for every preexisting label tkinter" June 8 
#chatgpt "how to change font style for every preexisting label tkinter" June 8 2025
#"how to change button color tkinter"
#https://mockuuups.studio/blog/post/best-fonts-for-apps/
for widget in root.grid_slaves():
    widget.grid_configure(padx=10, pady=10)
    if isinstance(widget, tk.Label):
        current_font = font.nametofont(widget.cget("font"))
        current_font.configure(size=current_font.cget("size") + 1)
        current_font.configure(family="Inter")
        widget.config(font=current_font)

root.mainloop()
