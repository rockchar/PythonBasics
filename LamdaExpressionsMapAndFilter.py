#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:12:03 2019

@author: rockchar
"""


'''
map function
The map function allows you to "map" a function to an iterable object. 
That is to say you can quickly call the same function to every item in an 
iterable, such as a list. For example:
'''

def square(num):
    return num**2

mylist=[1,2,3,4]
for item in map(square,mylist):
    print(item)
    
square_list = list(map(square,mylist))

print(square_list)
print(list(map(square,mylist)))

#lets try some complex function
def splicer(name):
    if len(name)%2==0:
        return True
    else:
        return name[0]
    
name_list = ["Rohit","EVAN","MEAW"]
splice_list = list(map(splicer,name_list))
print(splice_list)

'''
Filter functions:
Filter functions can be applied on an iterable but here the method filters
the results based on only the inputs that return true for the given condition

'''

#example to filter all the even numbers in a list

my_list = [1,2,3,4,5,6,7,8]

def myEvenfilter(num):
    return num%2==0    # evaluates to True or False

even_list = list(filter(myEvenfilter,my_list))
print(even_list)


'''
Lamda expression is a quick one time use function and also known as ananomys 
function. They are one time function and used just once and never referenced 
again.

'''
