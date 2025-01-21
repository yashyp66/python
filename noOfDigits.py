def digits():
    a=int(input("what's your number?"))
    count = 0
    while a !=0:
        a//=10
        count +=1
    print(count,"digits are there")
digits()
