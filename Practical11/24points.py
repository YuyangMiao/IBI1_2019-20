# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:10:52 2020

@author: joe_m
"""

import itertools
x=input('''Please input numbers to compute 24 (use ',' to devide them): ''')
numbers=x.split(',')
numbers_int = [int(x) for x in numbers]
numbers_int.sort()
numbers_int.reverse() #list the inputted numbers in descending order
N=len(numbers_int)

if int(numbers_int[0])>23:
    print('The input number must be integers from 1 to 23')
else:
    #Permutation of inputted numbers
    all_sequence=list(itertools.permutations(numbers_int))
    def compute(m,n): 
        '''
        operation of +,-,*,/
        If one of the numbers is o, it will not be divided.
        '''
        if m!=0 and n!=0:
            z=[m+n,abs(n-m),m*n,m/n,n/m]
        if m==0 and n!=0:
            z=[m+n,abs(n-m),m*n,m/n]
        if m!=0 and n==0:
            z=[m+n,abs(n-m),m*n,n/m]
        if m==0 and n==0:
            z=[m+n,abs(n-m),m*n]
        return z
    def enumeration(i):
        '''
        For a given order of numbers, all possible operation is performed
        Operation results are stored in 'y'
        '''
        sequence=list(all_sequence[i]) #convert tuple into list
        y=compute(sequence[0],sequence[1])
        del sequence[0:2] #delete the two numbers that complete the 'compute' function
        while sequence!=[]:
            y_copy=y
            y=[]
            for j in y_copy:
                y+=compute(j,sequence[0])
            del sequence[0] #delete the number in 'sequence' that complete the 'compute' function
        #repeat until every number in 'sequence' is deleted ('computed')
        return y
    
    list1=[]
    for i in range(len(all_sequence)): #repeat 'enumeration' for every possible order of inputted numbers
        list1+=enumeration(i) 
    if 24 in list1:
        print('Yes')
    else:
        print('No')
    
    recursion_time=(N-1)*len(list1) #every number undergo N-1 times of operation
    print('recursion times: '+ str(recursion_time))