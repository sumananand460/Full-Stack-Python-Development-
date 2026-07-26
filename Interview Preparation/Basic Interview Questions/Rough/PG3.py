# WAP to check if a number is prime or not
number = int(input("Enter a number: "))

if number <= 1:
    print("Not Prime")

else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")