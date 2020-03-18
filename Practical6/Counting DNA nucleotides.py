# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:02:19 2020

@author: joe_m
"""
#import matplotlib.pyplot
import matplotlib.pyplot as plt
# import DNA sequence
DNA=['A','T','G','C','T','T','C','A','G','A','A','A','G','G','T','C','T','T','A','C','G']
total=len (DNA)
A=0
T=0
G=0
C=0
#Count number of ATGC in the sequence
for i in DNA:
    if i=='A':
        A=A+1
    if i=='T':
        T=T+1
    if i=='G':
        G=G+1
    if i=='C':
        C=C+1
#Creat a frequency dictionary (FD) contaning these information
FD={'A':str(A*100/total)+'%','T':str(T*100/total)+'%','G':str(G*100/total)+'%','C':str(C*100/total)+'%'}
#Plot a pie chart of the 4 DNA nucleotides
labels=['A','T','G','C']
size=[A,T,G,C]
explode=(0,0,0,0)
colors=['khaki','lightgreen','paleturquoise','pink']
plt.pie(size,explode=explode,colors=colors,labels=labels,autopct='%1.2f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('pie of the four DNA nucleotides')
plt.show()
print (FD)