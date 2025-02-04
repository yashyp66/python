import math
radius=int(input("Enter the radius of the circle:"))
p1=float(input("enter the x co-ordinate of the point you want to test:"))
p2=float(input("enter the y co-ordinate of the point you want to test:"))
c1=float(input("enter the center point x cordinate of the circle:"))
c2=float(input("enter the center point y cordinate of the circle:"))
if math.sqrt((p1-c1)**2 + (p2-c2)**2)==radius:
    print("the points lies on the circle")
elif math.sqrt((p1-c1)**2 + (p2-c2)**2)>radius:
    print ("the points lies outside the circle")
else:
    print("the points lies inside the circle")
    
