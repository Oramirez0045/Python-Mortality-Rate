import matplotlib.pyplot as plt
import pandas as pd

#import all data
#Female Non Smoker
f_ns = pd.read_csv('Female_Non-Smoker_2017.csv')
f_ns.drop(f_ns.columns[2:], axis = 1, inplace = True)

#Female Smoker
f_s = pd.read_csv('Female_Smoker_2017.csv')
f_s.drop(f_s.column[2:], axis = 1, inplace = True)

#Male Non Smoker
m_ns = pd.read_csv('Male_Non-Smoker_2017.csv')
m_ns.drop(m_ns.column[2:], axis = 1, inplace = True)

#Male Smoker
m_s = pd.read_csv('Male_Smoker_2017.csv')
m_s.drop(m_s.column[2:], axis = 1, inplace = True)

#Mixed Non Smoker
ns = pd.read_csv('Mix_Non-Smoker_2017.csv')
ns.drop(ns.column[2:], axis = 1, inplace = True)

#Mixed Smoker
s = pd.read_csv('Mix_Smoker_2017.csv')
s.drop(s.column[2:], axis = 1, inplace = True)

plt.plot(f_ns['Row\Column'], f_ns['1'], color = 'Green')
plt.show()
