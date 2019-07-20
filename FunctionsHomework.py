#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:39:44 2019

@author: rockchar
"""

'''
Q1 . Write a function that computes the volume of a sphere given its radius.
     The volume of a sphere is given as 4/3 * pi * radiusˆ3
 
'''
#import math for the value of pi
import math

def SphereVolume(radius):
    return 4/3*math.pi*(radius**3)


'''
Q2  . Write a function that checks whether a number is in a given range 
      (inclusive of high and low)
'''
#using range function
def InRange(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False
    

#using range function without using booleans
def InRangeWB(num,low,high):
    return num in range(low,high+1)


#using comparison operators
def InRangeComp(num,low,high):
    if low <= num <= high:
        return True
    else:
        return False

'''
Q3 . Write a Python function that accepts a string and calculates the number of
     upper case letters and lower case letters.
'''
#using variables to store the values
def CountCases(inputStr):
    uc = 0
    lc = 0
    for letter in inputStr:
        if letter.isupper():
            uc+=1
        elif letter.islower():
            lc+=1
        else:
            pass
    print("{} uppercase and {} lowercase".format(uc,lc))

#using dictionary to store the values 
def CountCasesDict(inputStr):
    d = {"upper":0 , "lower":0}
    for letter in inputStr:
        if letter.isupper():         
            d['upper']+=1
        elif letter.islower():
            d['lower']+=1
        else:
            pass
    print("{} uppercase and {} lowercase".format(d['upper'], d['lower']))
    

#driver code 
def main():
    print(SphereVolume(3))
    print(InRange(2,1,10))
    print(InRangeComp(2,1,10))
    print(InRangeWB(22,1,10))
    CountCases('Hello Mr. Rogers, how are you this fine Tuesday?')
    CountCasesDict('Hello Mr. Rogers, how are you this fine Tuesday?')

if __name__=="__main__":
    main()
    