try:
    a = input("enter number")
    for i in range(0,11):
     print(f'{int(a)} X {i} = {int(a)*i}')
except:
    print("Invalid input")

#another example
try:
    a = input("enter an interger !")
    print(int(a))
except:
    print("not an integer !")
    
#we can print multiple except  cases :