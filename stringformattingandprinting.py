"""
formatting string using the .format method

"""

print("the {} brown {} fox {}".format("quick","brown","jumps"))

"""
.format using indexes

"""

print('The {1} brown {0} jumps {2}'.format("brown", "quick", "fox"))

"""
formatting using keywords

"""

print('The {a} brown {b} jumps {c}'.format(a='quick',b='fox',c='over'))