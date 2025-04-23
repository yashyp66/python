import math

class Solid:
    def __init__(self):
        self.shape = None

    def accept_data(self):
        print("Choose the solid type:")
        print("1. Cube")
        print("2. Cuboid")
        print("3. Sphere")
        print("4. Cylinder")
        choice = int(input("Enter your choice (1-4): "))
        self.shape = choice

        if choice == 1:
            self.side = float(input("Enter side of the cube: "))
        elif choice == 2:
            self.length = float(input("Enter length of the cuboid: "))
            self.breadth = float(input("Enter breadth of the cuboid: "))
            self.height = float(input("Enter height of the cuboid: "))
        elif choice == 3:
            self.radius = float(input("Enter radius of the sphere: "))
        elif choice == 4:
            self.radius = float(input("Enter radius of the cylinder: "))
            self.height = float(input("Enter height of the cylinder: "))
        else:
            print("Invalid choice.")

    def calculate_surface_area(self):
        if self.shape == 1:
            return 6 * self.side ** 2
        elif self.shape == 2:
            return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)
        elif self.shape == 3:
            return 4 * math.pi * self.radius ** 2
        elif self.shape == 4:
            return 2 * math.pi * self.radius * (self.radius + self.height)
        else:
            return 0

    def calculate_volume(self):
        if self.shape == 1:
            return self.side ** 3
        elif self.shape == 2:
            return self.length * self.breadth * self.height
        elif self.shape == 3:
            return (4/3) * math.pi * self.radius ** 3
        elif self.shape == 4:
            return math.pi * self.radius ** 2 * self.height
        else:
            return 0

# Using the class
solid = Solid()
solid.accept_data()

area = solid.calculate_surface_area()
volume = solid.calculate_volume()

print(f"Surface Area = {area:.2f}")
print(f"Volume = {volume:.2f}")
