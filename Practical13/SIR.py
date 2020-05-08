# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:37:54 2020

@author: joe_m
"""

# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt

#deﬁne the basic variables of the model
total=10000 #population size
susceptible=9999;infected=1;recovered=0 #initial situation
β=0.3;γ=0.05 #β: infection probability ;γ: recovery probability
#Susceptible-β-Infected-γ-Recovered 
track_susceptible=np.array([9999])
track_infected=np.array([1])
track_recovered=np.array([0])
timescale=np.arange(1,1001)

for i in range(1,1000):
    #count the number of newly infected people
    infect=np.random.choice(range(2),susceptible,p=[1-β*infected/total,β*infected/total]) #0: uninfected   1:infected
    infect=list(infect)
    infect_number=infect.count(1)#count 'infected'
    #count the number of recovered people
    recover=np.random.choice(range(2),infected,p=[1-γ,γ]) #0: unrecovered   1:recovered
    recover=list(recover)
    recover_number=recover.count(1)#count 'recovered'
    #tract the change in the number of susceptible people
    track_susceptible=np.append(track_susceptible,[susceptible-infect_number])
    susceptible=susceptible-infect_number
    #tract the change in the number of infected people  
    track_infected=np.append(track_infected,[infected+infect_number-recover_number])
    infected=infected+infect_number-recover_number
    #tract the change in the number of recovered people  
    track_recovered=np.append(track_recovered,[recovered+recover_number])
    recovered=recovered+recover_number

plt.plot(timescale,track_susceptible,label='Susceptible')
plt.plot(timescale,track_infected,label='Infected')
plt.plot(timescale,track_recovered,label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()
plt.rcParams['savefig.dpi'] = 3000
plt.savefig('SIR Model.png')
plt.show()
