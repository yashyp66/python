def triangle():
    a=float(input("enter one angle"))
    b=float(input("enter second angle"))
    c=float(input("enter third angle"))
    if a+b+c == 180:
        print("It is a valid triangle")
    else:
        print("It is not a valid triangle")
triangle()
