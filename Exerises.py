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
#Using keys and indexing, grab the 'hello' from the following dictionary
d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key']) #using key

print(d['simple_key'][0:])#indexing

#this is a dictionary in a dictionary
d2 = {'k1':{'k2':'hello'}}
# Grab 'hello'

print(d2['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#Can you sort a dictionary? Why or why not?
'''
Dictionaries can't be sorted -- a mapping has no ordering! -- so, when you 
feel the need to sort one, you no doubt want to sort its keys 
(in a separate list). Sorting (key,value) pairs (items) is simplest, 
but not fastest.

The concept of 'sort' applies only to a collection which has _order_ -- 
a sequence; a mapping (e.g. a dictionary) has NO order, thus it cannot be 
sorted. Still, its keys can be extracted as a list, which can then be sorted. 
The example functions return the values in order of sorted key, which just 
happens to be the single most frequent actual need corresponding to user 
questions such as "how do I sort a dictionary":-)

The implementation choices are interesting. Since we are sorting key-value 
pairs by the key field, then returning the list of value fields, it seems 
clearest (conceptually simplest) to architect the solution as in the first 
example: .items, .sort, then a list comprehension to pick the value fields.

# (IMHO) the simplest approach:
def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

# an alternative implementation, which
# happens to run a bit faster for large
# dictionaries on my machine:
def sortedDictValues2(adict):
    keys = adict.keys()
    keys.sort()
    return [dict[key] for key in keys]

# a further slight speed-up on my box
# is to map a bound-method:
def sortedDictValues3(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)


However (at least on my machine) this turns out not to be fastest: extracting 
just the keys, sorting them, then accessing the dictionary for each key in the 
resulting list comprehension, as in the second example, appears to be speedier.

'''

#-------------------------- TUPLES----------------------------------------
#What is the major difference between tuples and lists?
# Lists are mutable, tuples are immutable

#How do you create a tuple?
# using round brackets
tuple_1 = (1,2,3,4)
tuple_2 = 1,2,3,4,5,6


print(tuple_1)

tuple_1 = (3,4,5)+tuple_1
print(tuple_1)

print(tuple_1*4)

#------------------------- SETS ------------------------------------------
#What is unique about a set?
#sets do not have any duplicate value

#Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(list5)

my_set = set(list5)
print(my_set)
my_set.add("Hello")
print(my_set)
