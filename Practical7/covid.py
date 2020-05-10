# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:27:25 2020

@author: joe_m
"""

import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
os.chdir(r"C:\Users\joe_m\IBI1_2019-20\Practical7") 
covid_data = pd.read_csv("full_data.csv")

#code for showing all columns, and every third row between (and including) 0 and 15 
a=covid_data.iloc[0:16:3,:]
print('All columns and every third row between (and including) 0 and 15:')
print(a)
print('')

#a Boolean to show “total cases” for all rows corresponding to Afghanistan. 
location=covid_data.iloc[:,1] #get all locations from the .csv file
#A Boolean that only equals to "True" when the location is Afghanistan
my_location1=[]
for i in location:
    if i=='Afghanistan':
        my_location1+=[True]
    else:
        my_location1+=[False]
Afghanistan_total_cases=covid_data.loc[my_location1,"total_cases"] #only total cases of Afghanistan
print('Total cases in Afghanistan everyday:')
print(Afghanistan_total_cases)
print('')

# the mean and median of new cases for the entire world
#A Boolean that only equals to "True" when the location is World
my_location2=[]
for i in location:
    if i=='World':
        my_location2+=[True]
    else:
        my_location2+=[False]
world_new_cases=covid_data.loc[my_location2,"new_cases"]
mean=np.mean(world_new_cases)
median=np.median(world_new_cases)
print('The mean of new cases for the entire world is '+str(mean))
print('The median of new cases for the entire world is '+str(median))

#a boxplot of new cases worldwide
plt.boxplot(world_new_cases,vert=True,whis=1.5,patch_artist=True,meanline=True,
            showbox=True,showcaps=True,showfliers=True,notch=False)
plt.title('Boxplot of New Cases Worldwide')
plt.show()

# plot both new cases and new deaths worldwide
world_deaths=covid_data.loc[my_location2,"total_deaths"]
world_dates=covid_data.loc[my_location2,"date"]
plt.plot(world_dates, world_new_cases, 'b+-',world_dates, world_deaths, 'r+-')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90) #every four days
plt.xlabel('Date')
plt.ylabel('Numbers of people')
plt.legend(['Cases','Deaths'])
plt.title('Total Cases of COVID-19 and Deaths in World')
plt.show()

#Question and answer
questiontxt=open('question.txt', 'w',encoding='utf-8')
question='Question: How have new cases and total cases developed over time in Spain?\n'
questiontxt.write(question)
questiontxt.write('\n')
##A Boolean that only equals to "True" when the location is Spain
my_location3=[]
for i in location:
    if i=='Spain':
        my_location3+=[True]
    else:
        my_location3+=[False]
Spain_new_cases=covid_data.loc[my_location3,"new_cases"]
Spain_total_cases=covid_data.loc[my_location3,"total_cases"]
Spain_dates=covid_data.loc[my_location3,"date"]
plt.plot(Spain_dates, Spain_new_cases, 'b+-',Spain_dates, Spain_total_cases, 'r+-')
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-90)
plt.xlabel('Date')
plt.ylabel('Numbers of people')
plt.legend(['New Cases','Total Cases'])
plt.title('Total Cases and New cases of COVID-19 in Spain')
plt.show()
code='The question is addressed from line 72 to line 87 in the covid.py ﬁle.\n'
questiontxt.write(code)
questiontxt.write('\n')
discussion='''Discussion: The result met my expectations. On the early stage of COVID-19 
                   outbreak, people are neglectful of taking precautions. One infected 
                   person can pass the virus to other persons, and the process will 
                   keep going. Consequently, total cases grow rapidly at these days.'''
questiontxt.write(discussion)
questiontxt.close()