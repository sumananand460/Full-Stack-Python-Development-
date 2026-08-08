# WAP to check if a number is armstrong number or not
def is_armstrong(num):
    # Convert the number to string to get the number of digits
    num_str = str(num)
    num_digits = len(num_str)

    # Calculate the sum of the digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum of powers is equal to the original number
    return sum_of_powers == num

# Test the function
number = 153
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

"""
Working principle:
1. The function `is_armstrong` takes an integer `num` as input.
2. It converts the number to a string to determine the number of digits.
3. It calculates the sum of each digit raised to the power of the number of digits.
4. It checks if this sum is equal to the original number and returns the result.
"""
    