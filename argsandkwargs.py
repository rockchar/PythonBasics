# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:34:32 2019

@author: rkumar43
"""


def main():
    print('hello world')
    sum_three_numbers(1, 2, 3)
    sum_many_numbers(1, 2, 3)
    print(sum(a))
    print(sum(a, 1))
    sum_using_args(1, 2, 3)


'''
Sum method in python reference
Syntax:
sum(iterable, start)  
iterable : iterable can be anything list , tuples or dictionaries ,
 but most importantly it should be numbers.
start : this start is added to the sum of 
numbers in the iterable. 
If start is not given in the syntax , it is assumed to be 0.
'''
a = [1, 2, 3]

'''
The following function demos a method that prints the sum of three integers 

'''


def sum_three_numbers(a, b, c):
    print(a + b + c)


'''
what if we want to pass more than three or variable number of params functions 
then we need to define a function that takes many parameters and initialise 
each parameter with a default value
We can see that this is not a very efficient solution so we will use *args


It is worth noting that the word "args" is itself arbitrary - any word will do 
so long as it's preceded by an asterisk. To demonstrate this:

def myfunc(*spam):
    return sum(spam)*.05
​
myfunc(40,60,20)
'''


def sum_using_args(*args):
    print(sum(args))
    print((args))


def sum_many_numbers(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0):
    print(sum((a, b, c, d, e, f, g, h)))


'''
when we have variable number of arguements 
'''
if __name__ == '__main__':
    main()
