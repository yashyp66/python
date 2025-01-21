def threeno():
    a=int(input("enter the no. 1 :"))
    b=int(input("enter the no. 2 :"))
    c=int(input("enter the no. 3:"))
    largest = a
    if b>largest:
        largest = b
    if c>largest:
        largest = c
        
    smallest = a
    if b<smallest:
        smallest = b
    if c<smallest:
        smallest = c
        
    if largest == smallest:
        print("all three are equal")
    print("largest is ",largest)
    print("smallest is ",smallest)
threeno()
