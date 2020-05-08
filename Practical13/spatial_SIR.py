# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:15:19 2020

@author: joe_m
"""

# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt

β=0.3;γ=0.05 #β: infection probability ;γ: recovery probability
# make array of all susceptible population
#0 for susceptible, 1 for infected, 2 for recovered
population=np.zeros((100,100))
#randomly choose the first infected people
outbreak=np.random.choice(range(100),2) #randomly generate 2 numbers from 0 to 100 as X axis and Y axis
x=outbreak[0];y=outbreak[1]
population[x,y]=1 

def spread(x,y):
    if x!=0 and y!=0 and x!=99 and y!=99: #the infected people is in middle
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if population[xNeighbour,yNeighbour]==0: #susceptible
                    #P(infected)=0.3; P(remain susceptible)=0.7
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
                if population[xNeighbour,yNeighbour]==1: #infected
                    #P(recover)=0.05; P(remain infected)=0.95
                    population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-γ,γ])[0]
                if population[xNeighbour,yNeighbour]==2: #recovered
                    #remain recovered
                    population[xNeighbour,yNeighbour]=2
    if x==0 and y!=0 and y!=99: #top
        for xNeighbour in range(x,x+2):
            for yNeighbour in range(y-1,y+2):
                if population[xNeighbour,yNeighbour]==0: #susceptible
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
                if population[xNeighbour,yNeighbour]==1: #infected
                    population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-γ,γ])[0]
                if population[xNeighbour,yNeighbour]==2: #recovered
                    population[xNeighbour,yNeighbour]=2
    if x==0 and y==99: #top-right
        for xNeighbour in range(x,x+2):
            for yNeighbour in range(y-1,y+1):
                if population[xNeighbour,yNeighbour]==0: #susceptible
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
                if population[xNeighbour,yNeighbour]==1: #infected
                    population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-γ,γ])[0]
                if population[xNeighbour,yNeighbour]==2: #recovered
                    population[xNeighbour,yNeighbour]=2
    if x!=0 and x!=99 and y==99: #right
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+1):
                if population[xNeighbour,yNeighbour]==0: #susceptible
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
                if population[xNeighbour,yNeighbour]==1: #infected
                    population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-γ,γ])[0]
                if population[xNeighbour,yNeighbour]==2: #recovered
                    population[xNeighbour,yNeighbour]=2
    if x==99 and y==99: #bottom-right
        for xNeighbour in range(x-1,x+1):
            for yNeighbour in range(y-1,y+1):
                if population[xNeighbour,yNeighbour]==0: #susceptible
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
                if population[xNeighbour,yNeighbour]==1: #infected
                    population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-γ,γ])[0]
                if population[xNeighbour,yNeighbour]==2: #recovered
                    population[xNeighbour,yNeighbour]=2
    if x==99 and y!=0 and y!=99: #bottom
        for xNeighbour in range(x-1,x+1):
            for yNeighbour in range(y-1,y+2):
                if population[xNeighbour,yNeighbour]==0: #susceptible
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
                if population[xNeighbour,yNeighbour]==1: #infected
                    population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-γ,γ])[0]
                if population[xNeighbour,yNeighbour]==2: #recovered
                    population[xNeighbour,yNeighbour]=2
    if x==99 and y==0: #bottom-left
        for xNeighbour in range(x-1,x+1):
            for yNeighbour in range(y,y+2):
                if population[xNeighbour,yNeighbour]==0: #susceptible
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
                if population[xNeighbour,yNeighbour]==1: #infected
                    population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-γ,γ])[0]
                if population[xNeighbour,yNeighbour]==2: #recovered
                    population[xNeighbour,yNeighbour]=2
    if x!=0 and y==0 and x!=99: #left
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y,y+2):
                if population[xNeighbour,yNeighbour]==0: #susceptible
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
                if population[xNeighbour,yNeighbour]==1: #infected
                    population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-γ,γ])[0]
                if population[xNeighbour,yNeighbour]==2: #recovered
                    population[xNeighbour,yNeighbour]=2
    if x==0 and y==0: #top-left
        for xNeighbour in range(x,x+2):
            for yNeighbour in range(y,y+2):
                if population[xNeighbour,yNeighbour]==0: #susceptible
                    population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-β,β])[0]
                if population[xNeighbour,yNeighbour]==1: #infected
                    population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-γ,γ])[0]
                if population[xNeighbour,yNeighbour]==2: #recovered
                    population[xNeighbour,yNeighbour]=2
    return population
#while len(np.where(population==1)[1])!=20: #continue modelling until only 20 infected people remain
for k in range(70): #can also pecify the model time
    for j in range(len(np.where(population==1)[1])-1,-1,-1): 
        x=np.where(population==1)[0][j] #vertical axis
        y=np.where(population==1)[1][j] #horizontal axis
        spread(x,y)
    plt.figure(figsize=(6,4),dpi=150) 
    plt.imshow(population,cmap='viridis',interpolation='nearest')
