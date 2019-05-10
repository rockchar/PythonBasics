# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:55:27 2019

@author: rkumar43
"""

#             Python Data Types                
"""
The following are the data types available in python

1. Integers         - int   - whole numbers such as 200 , 300 
2. Floating point   - float - numbers with decimal point like 3.45 
3. Strings          - str   - immutable,ordered sequence of characters
4. Lists            - list  - mutable ordered sequence of objects
5. Dictionaries     - dict  - unordered key value pairs 
6. Tuples           - tup   - Ordered immutable sequence of objects
7. Sets             - set   - Unordered collection of unique objects
8. Booleans         - bool  - Logical value indicating true or false

"""

#            Let us go through the data types 

#---------------------- STRINGS -------------------------------
#print formatting with placeholders

print("I am going to insert %s here." %"something")

#print formatting using two place holders
print("I am going to insert %s here and %s here." %("string 1","string 2"))

#string formatting using variable names 
x,y = "hello","world"
print("This will print %s %s"%(x,y))

"""
format conversion methods
there are two methods for converting any python object to string %s and %r. they use two different 
methods str() and repr()
Let us see the difference between them.

%r delivers the string representation of the string including any escape characters 

"""

print("here is a text using %s"%"str()")

print("and here is a text using %r"%"repr()")

'''

Lets see the difference between %s and %r again with a tab character


'''
print("here is a string with a %s"%'\t tab')

print("here is is a string with a %r"%"\t tab")

#-----------------------------floating point and precision --------------------
'''
%s convers everything to a string %d will convert everything to an integer without 
any decimals,%f is for float

'''
print("number to string %s, number to int %d, number to float %f"%(3.45,3.45,3.45))
#--------- with some format specifier
print("number to string %s, number to int %d, number to float %10.5f"%(3.45,3.45,3.45))

'''   multiple formatting
Multiple Formatting
Nothing prohibits using more than one conversion tool in the same print statement:
In [12]:

print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))
First: hi!, Second:  3.14, Third: 'bye!'
'''

print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))

#---------------------------formatting using .format()--------------------------

