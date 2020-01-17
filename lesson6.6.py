# dictionaries, or map

# dictionary
map = {'a': [34,34], 'b': [45,23], 'c': [22, 0]}

# access value from key
print(map['a'])

# edit the value using key
# map['a'] = 23, # works # no type, but will fail on operations performed
# print(map)
map['b'] = [54,23];
print(map)

# delete the key value pair
del map['c']
print (map)

# add an entry
map['d'] = [99,98]
print(map)
