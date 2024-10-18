# Standard Library
# reference:
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/library/stdtypes.html

# Some Common Used Modules
# os
# sys
# math
# random
# time
# datetime
# json
# re
# urllib

# ----------------------------------------------------------

# String Methods

# Case Conversions: capitalize, lower, upper.
# Removing Whitespace: lstrip, rstrip, strip.
# Formatting: center, format, ljust, rjust.
# Testing: endswith, isalnum, isalpha, isdigit, islower, isspace,
# Checking: isupper, startswith.
# Searching: count, find, index, rfind, rindex.
# Parsing: partition, rpartition, split, splitlines.
# Modifying: replace, translate.

# ----------------------------------------------------------

# String.format()
# The format() method is called on a string, and placeholders {} inside the string are replaced by values passed to format().

# Basic Example:
# print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Kevin and I am 20 years old.

# Numbered Placeholders:
# print("I have {0} apples and {1} oranges.".format(5, 10))
# Output: I have 5 apples and 10 oranges.

# Numbered Placeholders:
# print("{0} is from {1}, and {0} likes {2}".format("Kevin", "California", "coding"))
# Output: Kevin is from California, and Kevin likes coding.

# Named Placeholders
# print("My name is {name} and I am {age} years old.".format(name="Kevin", age=20))
# Output: My name is Kevin and I am 20 years old.

# Formatting Numbers:
# print("Pi rounded to two decimal places: {:.2f}".format(pi))
# Output: Pi rounded to two decimal places: 3.14


# ----------------------------------------------------------

# 3 ways to import a module

# import math
# from math import *
# from math import sqrt, pi, e, sin, cos, tan, log, log10, exp, ceil, floor

# ----------------------------------------------------------

# Math Module
# ceil()
# fabs() only works with math module with float values
# floor()
# sin()
# asin()
# cos()
# acos()
# tan()
# log()
# log10()

# ----------------------------------------------------------

# print()
# len()
# type()
# input()
# int()
# str()
# float()
# sum()
# round()
# abs()

# upper()
# lower()
# split()
# dist()
# sqrt()


# print(print(-42))