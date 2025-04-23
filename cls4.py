import math
class Shape:
    def __init__(self):
        self.shape=None
    def accept_data(self):
        print("Enter your choice :")
        print("1. Square ")
        print("2. Circle")
        print("3. Rectangle")
        print("4. Triangle")
        choice=int(input("Enter your chpice from above:"))
        self.shape=choice
        if choice==1:
            self.side=float(input("enter the side of square :"))
        elif choice==2:
            self.radius=float(input("Enter the radius of a circle"))
        elif choice==3:
            self.length=float(input("Enter the length of rectangle:"))
            self.breadth=float(input("Enter the breadth of rectangle : "))
        elif choice==4:
            self.s1=float(input("Enter the side 1 of triangle:"))
            self.s2=float(input("Enter the side 2 of triangle:"))
            self.s3=float(input("Enter the side 3 of triangle:"))
            self.base=float(input("Enter the base of triangle :"))
            self.height=float(input("Enter the height of triangle :"))
        else:
            print("INVALID SHAPE CHOOSEN !!")
    def perimeter(self):
        if self.shape==1:
            return self.side**2
        elif self.shape==2:
            return 2*math.pi*self.radius
        elif self.shape==3:
            return 2*(self.length+self.breadth)
            
        elif self.shape==4:
            return self.s1+self.s2+self.s3
    def area(self):
        if self.shape==1:
            return self.side**2
        elif self.shape==2:
            return math.pi*(self.radius**2)
        elif self.shape==3:
            return self.length*self.breadth
        elif self.shape==4:
            return 0.5*self.base*self.height
shape=Shape()
shape.accept_data()
print("Perimeter : ",shape.perimeter())
print("Area : ",shape.area())
