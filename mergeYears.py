import pandas as pd
import numpy as np 
import os

pd.set_option('display.max_columns', None)

os.chdir('/Users/monroefarris/Desktop')
data2014 = pd.read_csv('cleaned2014_15.csv')
data2015 = pd.read_csv('cleaned2015_16.csv')
data2016 = pd.read_csv('cleaned2016_17.csv')
data2017 = pd.read_csv('cleaned2017_18.csv')
data2018 = pd.read_csv('cleaned2018_19.csv')
data2019 = pd.read_csv('cleaned2019_20.csv')

finalData = pd.concat([data2014, data2015, data2016, data2017, data2018, data2019], ignore_index=True)

finalData.to_csv('finalCleanedData.csv')