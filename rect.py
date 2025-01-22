def rect():
    leg=float(input("what's length?"))
    bre=float(input("what's breadth?"))
    area=leg*bre
    peri=2*(leg+bre)
    print (" area of rectangle is : ",area , "and " , "perimeter of rectangle is ",peri)
    if area > peri:
        print("area of rectangle is greater than its perimeter")
    else :
        print("area if rectangle is n0t greater than its perimeter")
rect()
