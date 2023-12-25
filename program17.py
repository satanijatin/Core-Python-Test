
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))


s = (side1 + side2 + side3) / 2


area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print("The area of the triangle is: ",area)
