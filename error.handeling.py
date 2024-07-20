try:
    l = [1,4,5]
    i = int(input('enter value of index:'))
    print(l[i])
except: 
    print("error")
finally:
    print("i am king")

#finally return in every situation ! even thoug after returnig value inside function....

# manuall error 
  #use rto stop unecpeced result by using raise keyword !

a = int(input("enter value between 5-9 \n"))
if(a<5 or a>9):
    raise ValueError("invalid entry")