import pandas as pd
import matplotlib.pyplot as plt

def rename(s):
    self = s
    self = self.replace('.csv', '')
    self = self.replace('_', ' ')
    return self

files = [
    "Female_Non-Smoker_2017.csv",
    "Female_Smoker_2017.csv",
    "Male_Non-Smoker_2017.csv",
    "Male_Smoker_2017.csv",
    "Mix_Non-Smoker_2017.csv",
    "Mix_Smoker_2017.csv",
]

for dataFile in files:
    try:
        #assiging values to variables
        data = pd.read_csv(dataFile)
        name = rename(dataFile)

        #remove empty columns
        data.drop(data.columns[2:], axis = 1, inplace = True)
        print(name)
        print(data.head())

        plt.figure()
        plt.plot(data[r'Row\Column'], data['1'], color = 'Green')
        plt.title('Mortality Rate: ' + name)
    except:
        print("Error loading plot for" , name , "make sure file is cleaned")
