# Tuples and Lists
# Tuple
# Immutable: After creating a tuple, you can't change its contents (no adding, removing, or modifying elements).
# Ordered: Tuples maintain the order of elements. This means that once the elements are assigned in a certain order, they stay in that order.
# Heterogeneous: Tuples can contain elements of different data types, such as strings, integers, floats, and even other tuples.
# Indexable: Like lists, you can access tuple elements using their index, starting from 0.
# Faster: Tuples can be more efficient than lists when you have a fixed set of values because their immutability allows for some performance optimizations.
    
# Unpacking example
# a, b, c = (1, 2, 3)
# print(a)  # Output: 1
# print(b)  # Output: 2
# print(c)  # Output: 3

# my_tuple = (1, 2, 3, "hello", 5.5)
# print(my_tuple[0]) 

# ----------------------------------------------------------

# List
# List is a sequence of values, mutable
# List can be nested
# List can be empty
# List can be sliced
# List can be concatenated
# List can be repeated
# List can be compared
# List can be indexed

# List Slice
# List Slice is a subsequence of a list
# List Slice is a new list
# List Slice is a shallow copy
# List Slice is a view of the original list
# List Slice is a sequence of values

# Comparison
# Comparisons are performed lexicographically, and not based on length
# x = [1, 1, 3]
# y = [1, 0, 3, 4, 5]
# x < y ===> False

# Catenation
# x = [1, 2, 3]
# y = [4, 5, 6]
# z = x + y
# z = [1, 2, 3, 4, 5, 6]

# Repetition
# x = [1, 2, 3]
# y = x * 3
# y = [1, 2, 3, 1, 2, 3, 1, 2, 3]


# The sequence types may be compared with all of the relational operators.
# Comparisons are performed lexicographically, and not based on length
# [1, 2, 3] < [3] ===> True

# max()
# min()
# l.index(x)
# l.count(x)

# Methods can modify a list
# l.append(x)
# l.insert(index, x)

# l.reverse()

# l.remove(x)
# l.pop()
# l.pop(index)
# l.clear()
# del

# l.sort()
# sorted(l) will return a new list containing all items from the iterable in ascending order.

# ----------------------------------------------------------