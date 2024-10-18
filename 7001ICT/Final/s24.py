# Dictionary
# Dictionary is a collection of key-value pairs. It is mutable and unordered.


# d.keys()
# d.values()
# d.get('cake', 'cake not found') if no default value and key is not found, it will return None
# d.items()

# d.update({'fruit': 'Mango', 'fruit': 'Kiwi'})
# d[key] = value

# d.pop('fruit')
# del d[key]
# d.popitem()
# d.clear()


d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print(d.get('namee'))
print(d)

# ----------------------------------------------------------

# Set
# set doesn't have order
# The order of elements in a set is determined by the hash values of the elements, which can lead to seemingly random ordering. 
# set doesn't have duplicate
# set is mutable but it cannot contain changeable objects such as list and dictionary.

# s.add()
# s.update()
# s.remove()
# s.discard()
# s.pop()
# s.clear()

# s | t
# s.union(t), or s | t

#s & t
# s.intersection(t)

# s-t
# s.difference(t), or s - t

# s < t
# s.issubset(t), or s <= t

# s > t
# s.issuperset(t), or s >= t 


# s = {9, 1, 7, 8, 4, 6, 6, 6}
# t = {1, 8, 6, 10}
# x = {1, 'q', 'r', 's', 't'}

# print(x)

# ----------------------------------------------------------