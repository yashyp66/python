def fibonacci(n):
    sum=0
    for i in range(1,n+1):
        x=sum+i
        sum=x
        print(sum)
n=int(input("enter n :"))
fibonacci(n)