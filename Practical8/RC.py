# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:03:51 2020

@author: joe_m
"""

seq = 'ATGCGACTACGATCGAGGGCCAT' 
cDNA=[]
# Find complementary bases for every bases in 'gene'
for item in seq:
    if item=='A':
        cDNA=cDNA+['T']
    if item=='T':
        cDNA=cDNA+['A']
    if item=='G':
        cDNA=cDNA+['C']
    if item=='C':
        cDNA=cDNA+['G']
#convert the direction to "5’ to 3’"
cDNA.reverse()
#convert list to string
output=''.join(cDNA)
print ('The  Reverse complementary sequence is: ' + output)