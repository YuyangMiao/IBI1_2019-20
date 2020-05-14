# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:37:54 2020

@author: joe_m
"""


# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm

#deﬁne the basic variables of the model
total=10000 #population size
β=0.3;γ=0.05 #β: infection probability ;γ: recovery probability
#Susceptible-β-Infected-γ-Recovered 
timescale=np.arange(1,1001)

for i in range(0,11):
    infected=1;recovered=0 #initial situation
    vaccinated=int(total*i/10)
    susceptible=9999-vaccinated
    track_infected=np.array([1])
    if susceptible>0:
        for j in range(1,1000):
            #count the number of newly infected people
            infect=np.random.choice(range(2),susceptible,p=[1-β*infected/total,β*infected/total]) #0: uninfected   1:infected
            infect=list(infect)
            infect_number=infect.count(1)#count 'infected'
            #count the number of recovered people
            recover=np.random.choice(range(2),infected,p=[1-γ,γ]) #0: unrecovered   1:recovered
            recover=list(recover)
            recover_number=recover.count(1)#count 'recovered'
            susceptible=susceptible-infect_number
            #tract the change in the number of infected people  
            track_infected=np.append(track_infected,[infected+infect_number-recover_number])
            infected=infected+infect_number-recover_number
            recovered=recovered+recover_number
        plt.plot(timescale,track_infected,label=str(i*10)+'%',color=cm.viridis(20*i))
        plt.xlabel('Time')
        plt.ylabel('Number of People')
        plt.title('SIR Model')
        plt.legend()
    else:
        track_infected=np.array([1]*1000)
        plt.plot(timescale,track_infected,label=str(i*10)+'%',color=cm.viridis(20*i))
        plt.xlabel('Time')
        plt.ylabel('Number of People')
        plt.title('SIR Model with Different Vaccinate Rates')
        plt.legend()
plt.rcParams['savefig.dpi'] = 3000
plt.savefig('SIR Model with Different Vaccinate Rates.png')
plt.show()

