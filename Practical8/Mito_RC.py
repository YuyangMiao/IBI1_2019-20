# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:01:02 2020

@author: joe_m
"""

filename=input('Please type in a FASTA file name here: ')
mito_chromosome = open(filename)
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
    #convert to reverse complementary sequences
    cDNA=[]
    for item in seq:
        if item=='A':
            cDNA=cDNA+['T']
        if item=='T':
            cDNA=cDNA+['A']
        if item=='G':
            cDNA=cDNA+['C']
        if item=='C':
            cDNA=cDNA+['G']
    cDNA.reverse()
    c_seq=''.join(cDNA)
    mitogene=genename+'  Length: '+str(genelength)+'\n'+c_seq+'\n'
    mito_genome_concise=mito_genome_concise+[mitogene]

#import data to a new FASTA file
mito_gene=open(r'mito_complementary_gene_sequences.fa','w')
for gene in mito_genome_concise:
    mito_gene.write(gene+'\n')
mito_gene.close()
print ('Reverse Complementary Sequences of Mitochondria Genes Are Available Now!') #indicator of completion
