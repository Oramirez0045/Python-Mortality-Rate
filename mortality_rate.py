import pandas as pd
import matplotlib.pyplot as plt

#dictionary with files already set, hopefully we find a way to not write all of this to make the code shorter
files = {
    'Female_Non-Smoker' : 'Female_Non-Smoker_2017.csv',
    'Female_Smoker' : 'Female_Smoker_2017.csv',
    'Male_Non-Smoker' : 'Male_Non-Smoker_2017.csv',
    'Male_Smoker' : 'Male_Smoker_2017.csv',
    'Mix_Non-Smoker' : 'Mix_Non-Smoker_2017.csv',
    'Mix_Smoker' : 'Mix_Smoker_2017.csv'
}

#for loop that iterates through the dictionary to repeat the process of cleaning the data and exporting the plot as a jpg
for name, dataFile in files.items():
  #this ensures the error of not having the files already cleaned from stopping the program
  #so if one file is cleaned it'll keep running and another isnt, it'll remind you to clean it
    try:
        print(name)
        data = pd.read_csv(dataFile)
        data.drop(data.columns[2:], axis=1, inplace=True)
        print(data.head())

        plt.figure()
        plt.plot(data[r'Row\Column'], data['1'], color = "Green")
        plt.title("Mortality Rates: " + name)
        plt.savefig(name + '.jpg') #this will download the plot onto your computer
    except:
        print("Error loading ", name, " make sure files are cleaned")
