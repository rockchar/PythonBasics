# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:37:27 2019

@author: rkumar43
"""

'''
print a string in reverse using slicing

'''

a = "Hello World"

#print the 3rd character from the start

print(a[2])

#print the 3rd character from the end -3 last character is 

print(a[-3])

#print all chars with step of 2

print(a[0:11:2])

#print all the chars with a step of 2 from the end

print(a[::-2])


#print all the chars in reverse 

print(a[::-1])

#LIST SLICING

myList = [1,2,3,4,5,6]

print(myList)


print(myList[0:7:2])

print(myList[::-1])

print(myList[::-2])