# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:29:40 2020

@author: joe_m
"""
a=598
b=598598
print (b%7)
c=b/7
d=c/11
e=d/13
if a==e:
    print("a=e")
X=True
Y=False
W=(X and not Y)or(Y and not X)
Z=X!=Y
if Z==W:
    print('Z and W are the same')