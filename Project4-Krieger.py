from math import pi
radius = float(input("Enter the radius of the sphere: "))
diameter = 2 * radius
circumference = 2 * pi * radius
surfaceArea = 4 * pi * radius ** 2
volume = 4/3 * pi * radius ** 3
print("The diameter of the sphere is", diameter, "units.")
print("The circumference of the sphere is", circumference, "units.")
print("The surface area of the sphere is", surfaceArea, "square units.")
print("The volume of the sphere is", volume, "cubic units.")
