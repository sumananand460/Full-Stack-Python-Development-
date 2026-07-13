# Q - WAP to swap two numbers
a = 5
b = 10

# Method 1: using temporary variable
temp = a
a = b
b = temp
print(a, b)  # 10 5

# Reset
a, b = 5, 10

# Method 2: without temp, using tuple unpacking (recommended in Python)
a, b = b, a
print(a, b)  # 10 5

# Method 3: without temp, using arithmetic
a, b = 5, 10
a = a + b  # a becomes 15
b = a - b  # b becomes 5
a = a - b  # a becomes 10
print(a, b)  # 10 5