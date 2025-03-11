def compute(n):
    sum=0
    for i in range(1,5):
        print(n**i)
        sum +=n**i
    print(sum ,'is the sum of all above')
def main():
    n=int(input("Enter the value of n : "))
    compute(n)
    #for checking 4 to 7 according to question!!
    for i in range(4,8):
        compute(i)
main()