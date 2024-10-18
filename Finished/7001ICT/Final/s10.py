# Type bool and Boolean Expressions

# bool constructor bool() returns False for 0 and True for any other number
# bool(0)         =====> False
# bool(1)         =====> True
# bool("jeff")    =====> True
# bool("")        =====> False
# bool(0.0)       =====> False
# bool("False")   =====> True

# Any value can be converted to a bool,
# explicitly using the bool constructor or
# implicitly by coercion operators and their precedences

# ----------------------------------------------------------

# Range Testing with Boolean Expressions
# 0 <= x < 100

# Number
# Any zero value can be used as if it is False.
# Any non-zero value can be used as if it is True.

# String
# An empty string can be used as if it is False.
# Any non-empty string can be used as if it is True.

# is/is not operators are used to compare the identity of two objects
# == and != are used to compare the values of two objects

# Most languages would always return a Boolean value from and and or.
# But Python’s and and or always return one of their arguments.

# What will be the results of the following expressions?
# False and "Banana"     =====> False
# "Apple" and True       =====> True
# "Apple" and False      =====> False
# "Apple" and "Banana"   =====> Banana
# "Apple" and 1          =====> 1

# ----------------------------------------------------------