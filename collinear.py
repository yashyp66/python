def collinear():
    x1=float(input("enter first point's x cordinate : "))
    y1=float(input("enter first point's y cordinate : "))
    x2=float(input("enter second point's x cordinate : "))
    y2=float(input("enter second point's y cordinate : "))
    x3=float(input("enter third point's x cordinate : "))
    y3=float(input("enter third point's y cordinate : "))
    if (y2-y1)*(x3-x2)==(y3-y2)*(x2-x1):
        print("they lie on a straight line ")
    else:
        print("they doesn't lie on a line")
collinear()
    
