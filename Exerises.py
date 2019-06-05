# -*- coding: utf-8 -*-

"""
Numbers: Floating Point, integers whole numbers and decimal point numbers

Strings: immutable ordered sequence of characters

Lists: mutable ordered sequence of objects

Tuples:immutable ordered sequence of objects

Dictionaries:unordered pair of key value

sets : unordered collection of unique objects 
"""

#------------------------- String Slicing -------------------------------
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

#----------------------------- lists -------------------------------------

# Build this list [0,0,0] two separate ways.
# Method 1:
mylist=[]
#using append
mylist.append(0)
mylist.append(0)
mylist.append(0)

print(mylist)

# Method 2:
#using assignment
mylist1 = [0,0,0]
print(mylist1)

# Method 3:
#using concatenation
mylist2 = []
mylist2 = mylist2 + mylist #only a list can concatenate with a list
print(mylist2)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
print(list3)

list3[2][2] = "goodbye"

print(list3)

#Sort the list below
list4 = [5,3,4,6,1]

list4.sort()
print(list4)

#----------------------------------- DICTIONARIES --------------------------




