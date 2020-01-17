# tuple and list

# tuple: immutable
# sicnce tuple is immutable its fast in traversal and other operations
def example():
    # this is called sequence packing
    return 13,13
# this is sequence unpacking
a,b = example()
print(a)

# list
ll = [2,4,1,7,3,9,3,8,6,4,0]

# list size
print ("original length:", len(ll))

# list append, add to the end
# ll.append('Hello') # adding str is possible but some operations will not be supported ll.sort()
ll.append(67)

# list access
print(ll[len(ll) - 1])

# list sort
ll.sort() # return 'None', similar to 'void' in java
print(ll) # this will print the sorted instance

# list insert, for inserting ta index
ll.insert(5,23)
print (ll);

# list index, find the index of element
try:
    print(ll.index(3)) # returns the first index
    print(ll.index(43)) # return 'ValueError' if value not found
except ValueError as e:
    print(str(e))

# list count, count the frequnecy
print(ll.count(3))
print(ll.count(55)) # returns expcected 0

# list remove, remove the first occurence
print("before removing", ll)
ll.remove(3) # removes first '3'
print ("after removing",ll)


# list reverse;
# THIS IS NOT REVERSE SORTING,
# ONLY REVERING THE EXISTING LIST
ll.reverse();
print ("reverse ll", ll)
