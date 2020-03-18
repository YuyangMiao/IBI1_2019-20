# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:50:38 2020

@author: joe_m
"""
#import matplotlib.pyplot
import matplotlib.pyplot as plt
#import gene lengths
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths.sort() #sort lengths of genes in ascending order
del(gene_lengths[0]) #remove the shortest gene length
gene_lengths.pop() #remove the longest gene length
#boxplot
plt.boxplot(gene_lengths,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
              )
plt.show()
print (gene_lengths)