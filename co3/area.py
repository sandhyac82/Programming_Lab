from graphics import rectangle
from graphics import circle
from graphics import cuboid
from graphics import sphere


l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area=",rectangle.area(l,b))
print("Perimeter=",rectangle.perimeter(l,b))


r=int(input("\nEnter the radius of circle:"))
print("Area=",circle.area(r))
print("Perimeter=",circle.perimeter(r))


l=int(input("\nEnter the length of cuboid:"))
w=int(input("Enter the width of cuboid:"))
h=int(input("Enter the height of cuboid:"))
b=int(input("Enter the breadth of cuboid:"))
print("Area=",cuboid.area(l,w,h))
print("perimeter=",cuboid.perimeter(l,b,h))


r=int(input("\nEnter the radius of sphere:"))
print("Area=",sphere.area(r))
print("perimeter=",sphere.perimeter(r))

