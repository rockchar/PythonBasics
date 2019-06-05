#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:23:02 2019

@author: rockchar
"""

#Use for, .split(), and if to create a Statement that will print out words that 
#start with 's':

st = 'Print only the words that start with s in this sentence'
split_string = st.split()
print(split_string)
for words in split_string:
    index = 0
    if words[0]=="s":
        print(words)
        
        

#use split to make a list of comma separated values
        
st1 = 'this,is,a,comma,separated,thing'
split_csv = st1.split(",")
print(split_csv)

#Use range() to print all the even numbers from 0 to 10.

print([n for n in range(0,11) if n%2==0])
#print([n if n%2==0 else '' for n in range(0,11)])


#Use a List Comprehension to create a list of all numbers between 1 and 50 that 
#are divisible by 3.
div3=[]
div3=[n for n in range(1,51) if n%3==0 ]
print(div3)