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