# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:03:03 2019

@author: rkumar43
"""

'''
Write a method to calculate the radius of a sphere.

'''
import math
def SphereVolume(radius):
    return 4/3*math.pi*(radius**3)

'''
Write a function to check if a number is in a given range
'''
def CheckRange(num,low,high):
    if low <= num <= high:
        return True
    else:
        return False

'''
Write a function to check if a number is in a given range using range
'''
def CheckRangeWithRange(num,low,high):
    return num in range(low,high+1)

'''
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24

'''

def MultiplyList(numbers):
    total = 1
    for n in numbers:
        total *= n
    return total
'''
Write a python function that takes a string and calculates the number of 
upercase and lowercase letters
'''
def CheckUpperLowerCase(inputstring):
    countUpper = 0
    countLower = 0
    for n in inputstring:
        if n.isupper() == True:
            countUpper+=1
        elif n.islower() == True:
            countLower+=1
        else:
            pass
    print("Number of uppercase %d and lowercase %d"%(countUpper,countLower))
            
'''
Write a Python function that takes a list and returns a new list with unique 
elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''
def UniqueList(alist):
    #using loops
    uniqueList = []
    for n in alist:
        if n not in uniqueList:
            uniqueList.append(n)
    print(uniqueList)
    #using sets 
    uniqueListSet = list(set(alist))
    print(uniqueListSet)

'''
Write a Python function that checks whether a passed in string is palindrome or 
not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as 
forward, e.g., madam or nurses run.
'''

def CheckPalindromeUsingList(arg):
    arg = arg.replace(' ','')
    mylist = list(arg)
    if mylist == mylist[::-1]:#reversed(mylist)):
        return True
    else:
        return False
    
def CheckPalindromeUsingSlicing(arg):
    arg = arg.replace(' ','')
    if arg == arg[::-1]:
        return True
    else:
        return False
    
    
'''
Main function
'''    
def main():
    print("hello world")
    print(SphereVolume(3))
    #now rounding off to the nearest integer
    print(round(SphereVolume(3),1))
    print(CheckRange(10,1,10))
    print(CheckRangeWithRange(11,1,10))
    print(MultiplyList([1, 2, 3, -4]))
    CheckUpperLowerCase('Hello Mr. Rogers, how are you this fine Tuesday?')
    UniqueList([1,1,1,1,2,2,3,3,3,3,4,5])
    print(CheckPalindromeUsingList('helleh'))
    print(CheckPalindromeUsingSlicing('nurses runs'))
    
if __name__ == '__main__':
    main()
    