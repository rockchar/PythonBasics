# -*- coding: utf-8 -*-

import math

"""
Created on Mon Jul 15 13:03:03 2019

@author: rkumar43
"""

'''
Write a method to calculate the radius of a sphere.

'''


def sphere_volume(radius):
    return 4 / 3 * math.pi * (radius ** 3)


'''
Write a function to check if a number is in a given range
'''


def check_range(num, low, high):
    if low <= num <= high:
        return True
    else:
        return False


'''
Write a function to check if a number is in a given range using range
'''


def check_range_with_range(num, low, high):
    return num in range(low, high + 1)


'''
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24

'''


def multiply_list(numbers):
    total = 1
    for n in numbers:
        total *= n
    return total


'''
Write a python function that takes a string and calculates the number of 
upercase and lowercase letters
'''


def check_upper_lower_case(input_string):
    count_upper = 0
    count_lower = 0
    for n in input_string:
        if n.isupper():
            count_upper += 1
        elif n.islower():
            count_lower += 1
        else:
            pass
    print("Number of uppercase %d and lowercase %d" % (count_upper, countLower))


'''
Write a Python function that takes a list and returns a new list with unique 
elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''


def unique_list_with_elements(alist):
    # using loops
    unique_list = []
    for n in alist:
        if n not in unique_list:
            unique_list.append(n)
    print(unique_list)
    # using sets
    unique_list_set = list(set(alist))
    print(unique_list_set)


'''
Write a Python function that checks whether a passed in string is palindrome or 
not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as 
forward, e.g., madam or nurses run.
'''


def CheckPalindromeUsingList(arg):
    arg = arg.replace(' ', '')
    mylist = list(arg)
    if mylist == mylist[::-1]:  # reversed(mylist)):
        return True
    else:
        return False


def CheckPalindromeUsingSlicing(arg):
    arg = arg.replace(' ', '')
    if arg == arg[::-1]:
        return True
    else:
        return False


'''
Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
Hint: Look at the string module
'''
import string


def IsPangram(arg):
    arg = arg.replace(" ", "")
    arg = arg.lower()
    listAlpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(string.ascii_lowercase)
    listArg = list(set(arg))
    listArg.sort()
    print(listArg)
    if listArg == listAlpha:
        return True
    else:
        return False


'''
Main function
'''


def main():
    print("hello world")
    print(SphereVolume(3))
    # now rounding off to the nearest integer
    print(round(SphereVolume(3), 1))
    print(CheckRange(10, 1, 10))
    print(CheckRangeWithRange(11, 1, 10))
    print(MultiplyList([1, 2, 3, -4]))
    CheckUpperLowerCase('Hello Mr. Rogers, how are you this fine Tuesday?')
    unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
    print(CheckPalindromeUsingList('helleh'))
    print(CheckPalindromeUsingSlicing('nurses runs'))
    print(IsPangram("Jived fox nymph grabs quick waltz"))


if __name__ == '__main__':
    main()
