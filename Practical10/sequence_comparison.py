# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:52:26 2020

@author: joe_m
"""

import re
a=open(r'SOD2_human.fa')
b=open(r'SOD2_mouse.fa')
c=open(r'RandomSeq.fa')
human=''
mouse=''
random=''
for line in a:
    human+=line
for line in b:
    mouse+=line
for line in c:
    random+=line
#remove descriptions
human_SOD2=re.sub('(.+\)\n)','',human)
human_SOD2=re.sub('\n','',human_SOD2)
mouse_SOD2=re.sub('(.+\)\n)','',mouse)
mouse_SOD2=re.sub('\n','',mouse_SOD2)
random_seq=re.sub('(>.+\n)','',random)
random_seq=re.sub('\n','',random_seq)
import pandas as pd
BLOSUM62=pd.read_excel('BLOSUM62.xlsx',index_col=0) #import BLOSUM62 matrix

#set initial distances to 0
distance_hm=0 #hm=huamn vs mouse
distance_hr=0 #hr=human vs random
distance_mr=0 #mr=mouse vs random
#huamn vs mouse
for i in range(0,len(human_SOD2)):
    col_name=human_SOD2[i]
    index_name=mouse_SOD2[i]
    distance_hm+=BLOSUM62[col_name][index_name]
#human vs random
for i in range(0,len(human_SOD2)):
    col_name=human_SOD2[i]
    index_name=random_seq[i]
    distance_hr+=BLOSUM62[col_name][index_name]
#mouse vs random
for i in range(0,len(mouse_SOD2)):
    col_name=mouse_SOD2[i]
    index_name=random_seq[i]
    distance_mr+=BLOSUM62[col_name][index_name]

#huamn vs mouse
central_hm=''
for i in range(0,len(human_SOD2)):
    col_name=human_SOD2[i]
    index_name=mouse_SOD2[i]
    if human_SOD2[i]==mouse_SOD2[i]: #indicate alignment with the same amino acid if there is a perfect match
        central_hm+=mouse_SOD2[i]
    elif BLOSUM62[col_name][index_name]>0: #any nonidentical letters that align with a positive score are indicated by '+'
        central_hm+='+'
    else:
        central_hm+=' '
output_hm='Human SOD2 Sequence: '+human_SOD2+'\n                                        '+central_hm+'\nMouse SOD2 Sequence:  '+mouse_SOD2+'\nScore: '+str(distance_hm)
#human vs random
central_hr=''
for i in range(0,len(human_SOD2)):
    col_name=human_SOD2[i]
    index_name=random_seq[i]
    if human_SOD2[i]==random_seq[i]: #indicate alignment with the same amino acid if there is a perfect match
        central_hr+=random_seq[i]
    elif BLOSUM62[col_name][index_name]>0: #any nonidentical letters that align with a positive score are indicated by '+'
        central_hr+='+'
    else:
        central_hr+=' '
output_hr='Human SOD2 Sequence: '+human_SOD2+'\n                                                 '+central_hr+'\nRandom         Sequence: '+random_seq+'\nScore: '+str(distance_hr)
#mouse vs random
central_mr=''
for i in range(0,len(mouse_SOD2)):
    col_name=mouse_SOD2[i]
    index_name=random_seq[i]
    if mouse_SOD2[i]==random_seq[i]: #indicate alignment with the same amino acid if there is a perfect match
        central_mr+=random_seq[i]
    elif BLOSUM62[col_name][index_name]>0: #any nonidentical letters that align with a positive score are indicated by '+'
        central_mr+='+'
    else:
        central_mr+=' '
output_mr='Mouse SOD2 Sequence: '+mouse_SOD2+'\n                                                '+central_mr+'\nRandom         Sequence: '+random_seq+'\nScore: '+str(distance_mr)
summary=open(r'Summary.txt','w')
summary.write(output_hm+'\n \n')
summary.write(output_hr+'\n \n')
summary.write(output_mr+'\n \n')
Sum='''It is found that the BLOSUM62 score of human SOD2 sequence vs mouse SOD2 sequence is significantly higher 
than the scores of random sequence vs human SOD2 sequence and random sequence vs mouse SOD2 sequence. 
That means human SOD2 sequence shares much more similarity with mouse SOD2 sequence than the random 
sequence. SOD plays an important role in antioxidation, which is vital for the survivalfor all organisms. Human and 
mice share the same ancestors. During the evolution, SOD was never elimitated due to its important function. 
Only few mutations occured in SOD sequence. That's why SOD in human and mice have similar amino acid sequence.'''
summary.write('Summary: \n')
summary.write(Sum)
summary.close()