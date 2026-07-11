# ==================================
# OPERATORS IN PYTHON - QUICK NOTES
# ==================================

# Operators are used to perform operations on variables and values

# ==================================
# 1. ARITHMETIC OPERATORS
# ==================================

# Used for mathematical calculations

a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.33 (always returns float)
print(a // b)  # Floor Division → 3 (removes decimal part)
print(a % b)   # Modulus → 1 (remainder)
print(a ** b)  # Power → 1000 (10^3)

# ==================================
# 2. COMPARISON OPERATORS
# ==================================

# Used to compare values → result is always True or False

x = 5
y = 10

print(x == y)   # Equal → False
print(x != y)   # Not Equal → True
print(x > y)    # Greater than → False
print(x < y)    # Less than → True
print(x >= y)   # Greater or equal → False
print(x <= y)   # Less or equal → True

# ==================================
# 3. LOGICAL OPERATORS
# ==================================

# Used to combine multiple conditions

age = 20

print(age > 18 and age < 25)  # True (both conditions must be True)
print(age > 18 or age < 10)   # True (at least one condition True)
print(not(age > 18))          # False (reverses result)

# ==================================
# 4. ASSIGNMENT OPERATORS
# ==================================

# Used to assign and update values

x = 5

x += 3   # x = x + 3 → 8
x -= 2   # x = x - 2 → 6
x *= 2   # x = x * 2 → 12
x /= 2   # x = x / 2 → 6.0
x %= 2   # x = x % 2 → remainder

# ==================================
# IMPORTANT NOTES
# ==================================

# 1. "=" is assignment, "==" is comparison
x = 5      # Assign value
print(x == 5)   # Compare value → True

# 2. Division (/) always returns float
print(10 / 2)   # 5.0

# 3. Modulus (%) is useful for even/odd
num = 4
print(num % 2)  # 0 → even number

# 4. Logical operators are used in conditions (if-else)

# ==================================
# REAL-LIFE USAGE
# ==================================

# - Calculator → +, -, *, /
# - Login system → ==
# - Age validation → >, <
# - Even/Odd check → %
# - Eligibility check → and, or