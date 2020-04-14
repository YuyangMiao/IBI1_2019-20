# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:54:34 2020

@author: joe_m
"""

#import an integer n
n=7
#Judge if n=1
#If yes: print n and stop
#If no:
#    print n
#    Repeat:
#        If n is even: n=n/2, print n
#        If n is odd: n=3n+1, print n
#        If n==1, stop
if n==1:
    print (n)
else:
    print (n)
    while n!=1:
        if n%2==0:
            n=n/2
            print (n)
        else:
            n=3*n+1
            print (n)
        if n==1:
            break