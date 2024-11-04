set_1 = {1,2,3,4,5,5}

print(set_1) # {1, 2, 3, 4, 5} #duplicates are removed

set_1.add(6)
print(set_1) # {1, 2, 3, 4, 5, 6}

set_1.remove(2)
print(set_1) # {1, 3, 4, 5, 6}

set_1.discard(3)
print(set_1) # {1, 4, 5, 6}


set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

print(set_a.union(set_b)) # {1, 2, 3, 4, 5, 6, 7, 8} #all elements from both sets
print(set_a | set_b) # {1, 2, 3, 4, 5, 6, 7, 8} #all elements from both sets

print(set_a.intersection(set_b)) # {4, 5} #common elements
print(set_a & set_b) # {4, 5} #common elements

print(set_a.difference(set_b)) # {1, 2, 3} #elements in set_a but not in set_b
print(set_a - set_b) # {1, 2, 3} #elements in set_a but not in set_b

print(set_a.symmetric_difference(set_b)) # {1, 2, 3, 6, 7, 8} #elements in set_a and set_b but not in both
print(set_a ^ set_b) # {1, 2, 3, 6, 7, 8} #elements in set_a and set_b but not in both

print(set_a[1]) # TypeError: 'set' object is not subscriptable #sets are unordered and unindexed