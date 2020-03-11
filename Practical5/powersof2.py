# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:44:02 2020

@author: joe_m
"""

#Import x, import math
x=1
#Repeat while x!=0:
#    Find logarithm of x based on 2, defined as a
#    Find the biggset integer smaller than a, defined as b
#    x=x-2**b
#    if x==0:
#        break
import math
print (str(x)+" is ",end='')
while x!=0:
    a=math.log(x)/math.log(2)
    b=math.floor(a)
    x=x-2**b
    print ("2**"+str(b),end='')
    if x!=0:
        print ("+",end='')
    if x==0:
        break