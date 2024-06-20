#list in python, here list is datatype and provide muteability feature ! , here we can access values by indexing , values sapreated by commas !
# provide mutable feature we can change elements or vlalues inside list, here we can store multiple data types such as str, bool, int, float.

mylist = [3,4,5, True, "shoya"]
# print(mylist)
# print(type(mylist))
# print(mylist[4])
print(mylist[:])

if "5" in mylist:
    print("yes")
else:
    print("no")

if "ho" in "shoya":
    print("ehhh....")
#list compreshesion 

x = [ i*2 for i in range(10)]
print(x)

tup = (1,2,3)
list1 = list(tup)
res = tup.count(1)

list1.pop(2)
print(list1)
tup = (2,3,4,3,5,6,7,88,9,9, 3, 2,9)
res = tup.index(3)
print(res)