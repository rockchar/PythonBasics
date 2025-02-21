"""
Problem1: Handle the exception thrown by the following code

for i in ['a','b','c']:
    print(i**2)

"""
import traceback

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("Power takes only integers")
else:
    print("All ok!")
finally:
    print("Completed")

"""
Problem 2:




"""


def ask():
    while True:
        try:
            n = int(input("Please Enter a number"))
            print(n ** 2)
        except ValueError:
            print("Not an Integer")
            continue
        else:
            print("Thanks")
            break


ask()
