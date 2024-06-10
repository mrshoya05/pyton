a = int(input("enter your age :"))
print("your age is :", a)

    #for more then 2 conditions 
if a <= 10:
    print("under age:")
elif a <= 16:
    print("teenager :")
elif a <= 18:
    print("adult")
elif a <= 50:
    print("middle-aged")
elif a > 50:
    print("senior citizen !")
else:
    print("invalid entry :")

    #nested

num = int(input())
if(num<0):
    print("number is ngativre ")
elif(num>0):
    print("number is possitive")
    if(num <= 10):
        print("between 1-10")
    elif(num > 10 and num <=20):
        print("number is between 11-20")
    else:
        print("greater then 20")
else:
    print("number is zero !")

