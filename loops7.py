def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact
def ncr(n,r):
    ncr = factorial(n)/factorial(r)*factorial(n-r)
    return ncr
def npr(n,r):
    npr=factorial(n)/factorial(n-r)
    return npr
n=int(input("Enter the value of n : "))
r=int(input("Enter the value of r : "))
print(ncr(n,r), 'is the value of ncr')
print(npr(n,r),'is the value of npr')