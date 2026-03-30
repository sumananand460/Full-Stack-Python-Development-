# ==================================
# STRINGS IN PYTHON - QUICK NOTES
# ==================================

# 1. String = text data (must be inside quotes)
name = "Suman"
city = 'Bhubaneswar'

# 2. Both single (' ') and double (" ") quotes work
msg1 = "Hello"
msg2 = 'Hello'

# 3. Use different quotes if text contains quotes
text = "He said, 'Hello'"

# 4. Strings are immutable (cannot change directly)
# Example:
name = "Suman"
# name[0] = "R" ❌ (Error)

# 5. Access characters using index
name = "Suman"
print(name[0])   # S
print(name[-1])  # n (last character)

# 6. Slicing strings (get part of string)
text = "Python"
print(text[0:3])   # Pyt
print(text[:4])    # Pyth
print(text[2:])    # thon

# ==================================
# STRING METHODS
# ==================================

# 7. upper() → convert to uppercase
name = "suman"
print(name.upper())   # SUMAN

# 8. lower() → convert to lowercase
name = "SUMAN"
print(name.lower())   # suman

# 9. strip() → remove extra spaces
text = "  hello  "
print(text.strip())   # hello

# 10. replace() → replace part of string
text = "Hello World"
print(text.replace("World", "Suman"))

# 11. split() → convert string to list
text = "apple banana mango"
print(text.split())   # ['apple', 'banana', 'mango']

# ==================================
# JOINING STRINGS
# ==================================

# 12. join() → combine list into string
words = ["I", "love", "Python"]
result = " ".join(words)
print(result)   # I love Python

# ==================================
# STRING FORMATTING (f-strings)
# ==================================

# 13. f-strings → best way to format strings
name = "Suman"
age = 21

print(f"My name is {name} and I am {age} years old")

# 14. You can also do calculations inside f-string
a = 5
b = 10
print(f"Sum is {a + b}")   # Sum is 15

# ==================================
# IMPORTANT RULES
# ==================================

# 15. Strings + Strings = Concatenation
print("Hello " + "World")   # Hello World

# 16. String * number = repetition
print("Hi " * 3)   # Hi Hi Hi

# 17. "10" is string, 10 is integer
# Always check type when needed
print(type("10"))  # str
print(type(10))    # int

# ==================================
# REAL-LIFE USAGE
# ==================================

# - User names
# - Emails
# - Messages
# - Form inputs
# - Chat applications