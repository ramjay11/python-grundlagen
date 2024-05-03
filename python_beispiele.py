import sys
import math
import random
import threading
import time
from functools import reduce

'''
name = input("Wie heißt du?")
print("Hallo", name)
'''
# name = 11

'''
v1 = (
    1 + 2
    + 3
)

v1 = 5
v1 = v1 - 1
print(v1)
'''

# 5 Main Datatypes - Numbers, Strings, Lists, Tuples, and Dictionaries

# Datatypes in python are dynamically typed and all objects
'''
    Numeric Types:
        int: Integer type, e.g., x = 5
        float: Floating-point type, e.g., y = 3.14
        complex: Complex number type, e.g., z = 2 + 3j

    Sequence Types:
        str: String type, e.g., s = "Hello, World!"
        list: List type, e.g., my_list = [1, 2, 3]
        tuple: Tuple type, e.g., my_tuple = (4, 5, 6)

    Set Types:
        set: Set type, e.g., my_set = {1, 2, 3}

    Mapping Type:
        dict: Dictionary type (key-value pairs), e.g., my_dict = {'name': 'John', 'age': 25}

    Boolean Type:
        bool: Boolean type, either True or False

    None Type:
        None: Represents the absence of a value or a null value
'''

# print(type(11))
# print(sys.maxsize)
# print(sys.float_info)

# List
grocery_list = ['Celery', 'Carrots', 'Tomatoes', 'Lemon']
print('First Item is', grocery_list[0])
grocery_list[0] = 'Pineapple'
print('First Item is', grocery_list[0])

print(grocery_list[1:3])  # Subset of a list
# List inside a list
other_events = ['Play Guitar', 'Play Bass', 'Play Drums']
todo_list = [other_events, grocery_list]
print(todo_list)
print((todo_list[1][1]))
grocery_list.append('Parsley')
print(todo_list)

grocery_list.insert(1, "Cabbage")  # Particular index
print(todo_list)
grocery_list.remove("Cabbage")
grocery_list.sort()
grocery_list.reverse()
del grocery_list[4]
print(todo_list)

todo_list2 = other_events + grocery_list
print(len(todo_list2))
print(max(todo_list2))
print(min(todo_list2))

# Tuples, unlike Lists, can't be changed after it is created
# A Tuple is a built-in data type in Python that is used to store an ordered, immutable sequence of elements
# Tuples are surrounded by () lika a ball
pi_tuple = (3, 1, 4, 1, 5, 9)
new_tuple = list(pi_tuple)  # Converts to a list
new_list = tuple(new_tuple)  # Converts to a a tuple
len(tuple)

#  Dictionaries or Maps. A dictionary is going to be made up of values with a unique key
