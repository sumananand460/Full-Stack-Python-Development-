# Program to print the multiplication table of a number

num = int(input("Enter your number: "))

for i in range(1, 11):
    product = num * i

    print(f"{num} x {i} = {product}")