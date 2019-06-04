# -*- coding: utf-8 -*-

"""
Numbers: Floating Point, integers whole numbers and decimal point numbers

Strings: immutable ordered sequence of characters

Lists: mutable ordered sequence of objects

Tuples:immutable ordered sequence of objects

Dictionaries:unordered pair of key value

sets : unordered collection of unique objects 
"""

#s = 'hello'
# Print out 'e' using indexing

s = "hello"
print(s[1])

#s ='hello'
# Reverse the string using slicing

print(s[::-1])

#join

print("-".join(s))

# Print out the 'o'

# Method 1:

print(s[4])

# Method 2:
print(s[-1])

# Build this list [0,0,0] two separate ways.
# Method 1:
mylist=[]
mylist.append(0)
mylist.append(0)
mylist.append(0)

print(mylist)

# Method 2:
mylist1 = [0,0,0]
print(mylist1)

# Method 3:
mylist2 = []
mylist2 = mylist2 + mylist #only a list can concatenate with a list
print(mylist2)