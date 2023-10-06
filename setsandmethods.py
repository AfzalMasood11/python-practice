# it does not duplicate item
a = {4, 5, 6, 6, 6}
print(a) # its output: {4, 5, 6}

a2 = {6, 6,2, 8}
#union
print(a.union(a2))
#intersection
print(a.intersection(a2))
print(a)
