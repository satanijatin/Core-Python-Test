num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


finalnumber = num1 + num2 + num3


if num1 == num2 == num3:
    result = 3 * finalnumber
    print("The numbers are equal. Three times their sum is: ",result)
else:
    print("The sum of the three numbers is: ",finalnumber)
