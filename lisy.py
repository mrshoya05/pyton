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