import matplotlib.pyplot as plt
import pandas as pd

f_ns = pd.read_csv('Female_Non-Smoker_2017.csv')
f_ns.drop(f_ns.columns[2:], axis = 1, inplace = True)
