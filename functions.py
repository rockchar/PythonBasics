#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 20:55:55 2019
@author: rockchar
"""

"""
Function practice exercises : Warmup session 
"""

"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given 
numbers if both numbers are even, but returns the greater if one or both 
numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a if a < b else b
    elif a % 2 != 0 or b % 2 != 0:
        return b if a < b else a


'''
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if 
both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
'''


def animal_crackers(s):
    str_words = s.split()
    if str_words[0][0] == str_words[1][0]:
        return True
    else:
        return False


"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""

'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
Note: The .join() method may be useful here. The .join() method allows you to 
join together strings in a list with some connector string. For example, some 
uses of the .join() method:
>>> "--".join(['a','b','c'])
>>> 'a--b--c'
This means if you had a list of words you wanted to turn back into a sentence, 
you could just join them with a single space string:
>>> " ".join(['Hello','world'])
>>> "Hello world"
'''


def master_yoda(s):
    my_list = []
    for word in s:
        my_list += word


def main():
    print(myfunc("Rohit"))
    print(lesser_of_two_evens(2, 5))
    print(animal_crackers("Dog DOG"))
    print(master_yoda("I am home"))


def myfunc(arg):
    index = 0
    ret_string = ''
    for letter in arg:
        if index % 2 == 0:
            ret_string += letter.upper()
        else:
            ret_string += letter
        index += 1
    return ret_string


if __name__ == '__main__':
    main()
