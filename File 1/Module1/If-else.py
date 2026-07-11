# ==================================
# IF-ELSE IN PYTHON - DETAILED NOTES
# ==================================

# 1. if-else is used for decision making
# It allows the program to execute different code based on conditions

# Basic Syntax:
# if condition:
#     code runs if condition is True
# else:
#     code runs if condition is False

# ==================================
# 2. SIMPLE IF-ELSE
# ==================================

age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# ==================================
# 3. IF STATEMENT (WITHOUT ELSE)
# ==================================

num = 10

if num > 0:
    print("Positive number")

# Note: If condition is False, nothing happens

# ==================================
# 4. MULTIPLE CONDITIONS (elif)
# ==================================

marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

# elif = "else if" (used for multiple conditions)

# ==================================
# 5. USING COMPARISON OPERATORS
# ==================================

x = 5
y = 10

if x < y:
    print("x is smaller than y")

# Operators used:
# == (equal)
# != (not equal)
# >  (greater than)
# <  (less than)
# >= (greater or equal)
# <= (less or equal)

# ==================================
# 6. USING LOGICAL OPERATORS
# ==================================

age = 20

# and → both conditions must be True
if age > 18 and age < 25:
    print("Young adult")

# or → at least one condition must be True
if age > 18 or age < 10:
    print("Condition satisfied")

# not → reverses the condition
if not(age > 18):
    print("Age is not greater than 18")

# ==================================
# 7. NESTED IF (IF INSIDE IF)
# ==================================

age = 20

if age >= 18:
    if age < 25:
        print("Young adult")

# Used when one condition depends on another

# ==================================
# 8. USER INPUT WITH IF-ELSE
# ==================================

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ==================================
# 9. REAL-LIFE EXAMPLES
# ==================================

# Login system
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# ==================================
# 10. IMPORTANT RULES
# ==================================

# 1. Indentation is mandatory (use spaces or tab)
# Wrong:
# if True:
# print("Hello")  ❌

# Correct:
# if True:
#     print("Hello")  ✅

# 2. Colon (:) is required after condition
# if age > 18:  ✅

# 3. Use == for comparison, not =
# if x == 5   ✅
# if x = 5    ❌

# ==================================
# 11. SHORT HAND (TERNARY OPERATOR)
# ==================================

age = 20

result = "Adult" if age >= 18 else "Minor"
print(result)

# Same as:
# if age >= 18:
#     result = "Adult"
# else:
#     result = "Minor"

# ==================================
# 12. COMMON MISTAKES
# ==================================

# - Forgetting indentation
# - Using = instead of ==
# - Missing colon (:)
# - Wrong logical condition

# ==================================
# 13. INTERVIEW IMPORTANT POINTS
# ==================================

# - Used in almost every problem
# - Combined with loops and functions
# - Used for validation, filtering, decision making

# ==================================
# 14. QUICK REVISION
# ==================================

# if → condition check
# elif → multiple conditions
# else → default case
# indentation → very important