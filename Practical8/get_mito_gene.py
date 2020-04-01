# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:25:56 2020

@author: joe_m
"""

mito_chromosome = open(r'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
genome=''
for line in mito_chromosome:
    genome=genome+line 
genomelist=genome.split('>')

import re
mito_genome=[]
#find out mito genome
for i in genomelist:
    if re.search('chromosome:R64-1-1:Mito:',i):
        mito_genome=mito_genome+[i]
mito_genome_concise=[]
for j in mito_genome:
    k=re.sub(r'\n','',j) #remove all newline characters
    genename=re.sub(r'.+gene:(\S+).+',r'\1',k) #find out gene names
    seq=re.sub(r'.+](.+)',r'\1',k) #find out gene sequences
    genelength=len(seq) #calcuate gene lengths
    mitogene=genename+'  Length: '+str(genelength)+'\n'+seq+'\n'
    mito_genome_concise=mito_genome_concise+[mitogene]

#import data to a new FASTA file
mito_gene=open(r'mito_gene.fa','w')
for gene in mito_genome_concise:
    mito_gene.write(gene+'\n')
mito_gene.close()
print ('Mitochondria Gene Sequences Have Been Found!') #indicator of completion