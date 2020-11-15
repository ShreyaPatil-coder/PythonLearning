from math import pi


class Area:
    def area_of_circle(self, radius):
        # r = float(input("Input the radius of the circle : "))
        print("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius ** 2))

    def area_of_square(self,side):
        print("area of square with side " + str(side) + " is: " + str(side ** 2))