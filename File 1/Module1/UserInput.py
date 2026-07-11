# Taking user-input in python


# ================================
# USER INPUT IN PYTHON - NOTES
# ================================

# 1. input() is used to take input from user
name = input("Enter your name: ")

# 2. input() always returns data as STRING by default
age = input("Enter your age: ")
print(type(age))   # Output: <class 'str'>

# 3. To use numbers, we must convert (type casting)

# Convert to integer
age = int(input("Enter your age: "))

# Convert to float
price = float(input("Enter price: "))

# 4. Without conversion, operations may behave differently

# Example (Wrong way)
num = input("Enter number: ")
print(num + num)   # If input = 5 → Output: 55 (string concatenation)

# Example (Correct way)
num = int(input("Enter number: "))
print(num + num)   # If input = 5 → Output: 10

# 5. Multiple inputs
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# 6. Using f-strings with input (recommended)
name = input("Enter your name: ")
print(f"Hello {name}")

# 7. Always give clear message inside input()
# Bad: input()
# Good:
email = input("Enter your email: ")

# 8. Common errors:
# - Forgetting int() or float()
# - Using wrong data type
# - Typing letters when int() is expected (causes error)

# 9. Real-life usage:
# - Login forms
# - ATM systems
# - Registration forms
# - Calculators

# 10. Shortcut tip:
# You can write input + conversion in one line
num = int(input("Enter number: "))
