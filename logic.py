#factorial 

def fac(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fac(n-1)
    
print(fac(5))

#fionacco series 

def fibo(n):
 if(n==0):
  return 0
 elif(n==1):
  return 1
 else:
  return fibo(n-1)+fibo(n-2)
n = input("enter value")
for i in range(0, int(n)):
    print(fibo(i), end=" ")
 