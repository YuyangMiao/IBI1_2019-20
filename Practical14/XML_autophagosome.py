# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:37:00 2020

@author: joe_m
"""

#import necessary libraries
import xml.dom.minidom
import re
import pandas as pd

print('The running time of this programme may be longer than 1 mintue, please be patient.^_^')

DOMTree=xml.dom.minidom.parse('go_obo.xml') #open the document
collection=DOMTree.documentElement #find the root element of the document
terms=collection.getElementsByTagName("term") #search for all elements named 'term' under the root element
IDs_excel=[]
definitions_excel=[]
names_excel=[]
childnodes_excel=[]
def count_childnodes(ID):
    '''
    find the number of childNodes for each 'autophagosome'
    related gene ontology term with its ID (GO:XXXXXXX)
    '''
    childnodes_number=0
    ID_list=[ID]
    while ID_list!=[]: #stop when reach the most inferior ID
        ID_list_copy=ID_list
        ID_list=[]
        for i in ID_list_copy: #repeat for every ID given
            for term in terms: #search in every element called 'term'
                is_as=term.getElementsByTagName("is_a") 
                #search for all elements named 'is_a' under 'term'
                #is_a contains the superior IDs of its the given ID
                for is_a in is_as: 
                    if is_a.childNodes[0].data==i: #if the ID belongs to a certain superior ID
                        childnodes_number+=1 #number of childnodes + 1
                        childnodes_ID=term.getElementsByTagName("id")[0]
                        ID_list.append(childnodes_ID.childNodes[0].data) 
                        #add the superior IDs to 'ID_list', the next loop will find their superior IDs
    return childnodes_number
for term in terms:
    defs=term.getElementsByTagName("def") 
    #search for all elements named 'def' under 'term'
    #def contains definition string of the 'term'
    for DEF in defs:
        definition_string=DEF.getElementsByTagName("defstr")[0]
        #search for all elements named 'defstr' under 'def'
        #defstr contains definition of the 'term'
        if re.search(r'.+autophagosome.+',definition_string.childNodes[0].data):
        #find 'term's that have 'autophagosome' in their defenition strings
            #extract definition strings and store them as list in 'definitions_excel'
            definitions=definition_string.childNodes[0].data
            definitions_excel.append(definitions)
            #extract IDs and store them as list in 'IDs_excel'
            IDs=term.getElementsByTagName("id")[0]
            IDs=IDs.childNodes[0].data
            IDs_excel.append(IDs)
            #extract names and store them as list in 'names_excel'
            names=term.getElementsByTagName("name")[0]
            names=names.childNodes[0].data
            names_excel.append(names)
            #count numbers of childnides and store them as list in 'childnodes_excel'
            childnodes_excel.append(count_childnodes(IDs))
#import these data into an Excel
data=pd.DataFrame({'id':IDs_excel,'name':names_excel,'definition':definitions_excel,'childnodes':childnodes_excel})
writer = pd.ExcelWriter('autophagosome.xlsx')
data.to_excel(writer,index=False)
writer.save()
print(data)