# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:23:24 2021

@author: N0ur
"""

import pandas as pd 
# making data frame from csv file
dataset=pd.read_csv("Wuzzuf_jobs.csv")
#describe data
dataset.describe(include='all')
dataset.info()
#display some of dataset
dataset.head()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import pandas as pd 
dataset.sort_values("Company", inplace = True)
dataset.drop_duplicates(subset = ["Title","Company","Location","Type","Level","YearsExp","Country","Skills"],keep = "first", inplace = True)

dataset





#to know if dataset has null value 
print(dataset.isnull().sum())           
dataset.isnull().values.any()    

  
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv("Wuzzuf_jobs.csv")
dataset.sort_values(by=["Company", "Title"], inplace=True)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

from sklearn.impute import SimpleImputer

imp_mean = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp_mean = imp_mean.fit(x[:, 0:3])
x[:, 0:3] = imp_mean.transform(x[:, 0:3])      
print(x)


#>>>>>>>>>>>>>>>>>>>>>
#count jobs for each company 

x=dataset['Company'].value_counts()
x
import matplotlib.pyplot as plt

plt.pie(x)
plt.show() 



#most job title 
x=dataset['Title'].value_counts()
x
list(x.keys())[0]





keys = list(x.keys())
values = list(x)
keys
values
# creating the bar plot
plt.bar(keys, values, color ='maroon',width = 0.6)

plt.xlabel("Jobs")
plt.ylabel("number of Job ")
plt.title("Most popular job ")



#most popular area
popular_area=dataset['Country'].value_count()
popular_area





keys = list(popular_area.keys())
values = list(popular_area)
keys
values
# creating the bar plot
plt.bar(keys, values, color ='maroon',width = 0.6)

plt.xlabel("Countries")
plt.ylabel("No. of employees in country")
plt.title("employees working in different countries")
plt.show()







