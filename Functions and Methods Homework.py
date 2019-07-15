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
Main function
'''    
def main():
    print("hello world")
    print(SphereVolume(3))
    #now rounding off to the nearest integer
    print(round(SphereVolume(3),1))
    print(CheckRange(10,1,10))
    
if __name__ == '__main__':
    main()
    