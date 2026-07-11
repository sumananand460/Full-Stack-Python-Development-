# Program to create a advance level calculator using if, elif and else statements

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

operation = input("Enter Operation (+, -, *, /):  ")

sum = a + b
difference = a - b
product = a * b
quotient = a // b

if operation == "+":
    print (f"Sum of {a} and {b} is: {sum}")
elif operation == "-":
    print (f"Difference of {a} and {b} is: {difference}")
elif operation == "x*":
    print (f"Product of {a} and {b} is: {product}")
elif operation == "/":
    print (f"Quotient of {a} and {b} is: {quotient}")
else: 
    print ("Inavlid Operator")
