# #are immuteable we can not change them 
# tup = (1,2,3)
# tup1 = (4,5,6)

# tup3 = tup + tup1

# print(tup3)
# print(type(tup3))

#another method is first converting then into list then manuplate 

tuple = (2, 3, 5)

list = list(tuple)
list.append(3)
final = tuple(list)
print(final)
print(type(final))