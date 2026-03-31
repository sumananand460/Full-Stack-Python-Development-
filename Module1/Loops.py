"""
===============================================================================
                    PYTHON LOOPS: COMPREHENSIVE NOTES
===============================================================================

This file contains detailed notes on loops in Python, including definitions,
examples, important points, tricks, and tips. Code examples are provided with
their expected outputs shown as comments.

Feel free to run this file to see the outputs. Comments explain each concept.
===============================================================================
"""

# =============================================================================
# 1. INTRODUCTION TO LOOPS
# =============================================================================
"""
A loop is a programming construct that repeats a block of code as long as a
condition is true or for each item in a sequence.

Python provides two primary loop types:
    - for loop: Iterates over a sequence (list, tuple, string, etc.)
    - while loop: Repeats as long as a boolean condition is True.

Additionally, there are control statements: break, continue, and pass.
"""

# =============================================================================
# 2. FOR LOOP
# =============================================================================
"""
Definition:
    The for loop is used to iterate over items of any sequence (such as a list,
    tuple, string, dictionary, set, or range) in the order they appear.

Syntax:
    for variable in iterable:
        # code block to execute for each item

Common iterables: list, tuple, string, dict, set, range, file objects.
"""

# ------------------------ Example 1: Iterating a list ------------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)          # Output: apple    (each on new line)
# Expected output:
# apple
# banana
# cherry

# ------------------------ Example 2: Iterating a string ------------------------
for char in "hello":
    print(char)           # Output: h e l l o (each on new line)
# Expected output:
# h
# e
# l
# l
# o

# ------------------------ Example 3: Iterating a tuple ------------------------
coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)          # Output: 10 20 30 (each on new line)
# Expected output:
# 10
# 20
# 30

# ------------------------ Example 4: Iterating a dictionary ------------------------
person = {"name": "Alice", "age": 30, "city": "New York"}
# Iterating over keys
for key in person:
    print(key)            # Output: name age city (order may vary)
# Expected output (order may differ):
# name
# age
# city

# Iterating over values
for value in person.values():
    print(value)          # Output: Alice 30 New York
# Expected output:
# Alice
# 30
# New York

# Iterating over key-value pairs
for key, value in person.items():
    print(key, "->", value)   # Output: name -> Alice, etc.
# Expected output:
# name -> Alice
# age -> 30
# city -> New York

# ------------------------ Example 5: Using range() ------------------------
"""
range(start, stop, step) generates a sequence of numbers.
- start: optional, default 0
- stop: required, up to but not including
- step: optional, default 1
"""
for i in range(5):        # 0,1,2,3,4
    print(i, end=" ")     # Output: 0 1 2 3 4
print()   # newline

for i in range(2, 8):     # 2,3,4,5,6,7
    print(i, end=" ")     # Output: 2 3 4 5 6 7
print()

for i in range(0, 10, 2): # 0,2,4,6,8
    print(i, end=" ")     # Output: 0 2 4 6 8
print()

# ------------------------ Example 6: enumerate() for index and value ---------
"""
enumerate(iterable, start=0) returns pairs of (index, value). Useful when you
need both the position and the item.
"""
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")   # Output: 0: red, 1: green, 2: blue
# Expected output:
# 0: red
# 1: green
# 2: blue

# Starting from a custom index
for index, color in enumerate(colors, start=1):
    print(f"{index}: {color}")   # Output: 1: red, 2: green, 3: blue
# Expected output:
# 1: red
# 2: green
# 3: blue

# ------------------------ Example 7: zip() for parallel iteration ------------
"""
zip() aggregates elements from multiple iterables. Stops at the shortest.
"""
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
# Expected output:
# Alice is 25 years old and lives in NYC
# Bob is 30 years old and lives in LA
# Charlie is 35 years old and lives in Chicago

# ------------------------ Example 8: for-else clause -------------------------
"""
The else block executes after the loop finishes normally (i.e., no break).
Commonly used for searching: if the loop didn't break, do something.
"""
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 6:
        print("Found 6!")
        break
else:
    print("6 not found")   # This executes because break never occurred
# Expected output: 6 not found

# With break
for n in numbers:
    if n == 3:
        print("Found 3!")
        break
else:
    print("3 not found")   # Not executed
# Expected output: Found 3!

# =============================================================================
# 3. WHILE LOOP
# =============================================================================
"""
Definition:
    The while loop repeatedly executes a block of code as long as a given
    condition is True.

Syntax:
    while condition:
        # code block
    # code after loop

Important: Ensure the condition eventually becomes False to avoid infinite loop.
"""

# ------------------------ Example 1: Basic while loop ------------------------
count = 0
while count < 5:
    print(count, end=" ")   # Output: 0 1 2 3 4
    count += 1
print()

# ------------------------ Example 2: Infinite loop with break ----------------
"""
Sometimes you want a loop that runs indefinitely until a certain event occurs.
Use break to exit.
"""
x = 0
while True:
    print(x, end=" ")       # Output: 0 1 2 3 4
    x += 1
    if x == 5:
        break
print()

# ------------------------ Example 3: while-else clause -----------------------
"""
The else block executes if the loop condition becomes False (i.e., normal exit),
not if the loop is terminated by break.
"""
num = 0
while num < 5:
    print(num, end=" ")
    num += 1
else:
    print("\nLoop finished normally")   # This executes
# Expected output: 0 1 2 3 4
# Loop finished normally

# With break
num = 0
while num < 5:
    if num == 3:
        break
    print(num, end=" ")
    num += 1
else:
    print("\nLoop finished normally")   # This does NOT execute
print("\nBreak occurred")

# =============================================================================
# 4. LOOP CONTROL STATEMENTS
# =============================================================================
"""
break: Terminates the loop entirely.
continue: Skips the rest of the current iteration and moves to the next.
pass: Does nothing; acts as a placeholder.
"""

# ------------------------ Example: break and continue ------------------------
for i in range(1, 10):
    if i == 3:
        continue   # skip printing 3
    if i == 7:
        break      # stop loop when i reaches 7
    print(i, end=" ")   # Output: 1 2 4 5 6
print()

# ------------------------ Example: pass (placeholder) ------------------------
# Often used in stubs or when syntax requires a block but you want to do nothing.
for i in range(3):
    pass   # Does nothing; loop runs but no action
print("Loop with pass completed")

# =============================================================================
# 5. NESTED LOOPS
# =============================================================================
"""
Loops can be placed inside other loops. The inner loop executes fully for each
iteration of the outer loop.
"""

# ------------------------ Example: Multiplication table ----------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}*{j}={i*j:2}", end="  ")
    print()   # newline after each row
# Expected output:
# 1*1=1   1*2=2   1*3=3
# 2*1=2   2*2=4   2*3=6
# 3*1=3   3*2=6   3*3=9

# ------------------------ Example: Using break in nested loops --------------
# break only exits the innermost loop
for i in range(3):
    for j in range(5):
        if j == 2:
            break   # exits inner loop only
        print(f"({i},{j})", end=" ")
    print()
# Expected output:
# (0,0) (0,1)
# (1,0) (1,1)
# (2,0) (2,1)

# To exit both loops, use a flag or wrap in a function
found = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
        print(f"({i},{j})", end=" ")
    if found:
        break
print("\nBoth loops exited")

# =============================================================================
# 6. LIST COMPREHENSIONS (Concise Loops)
# =============================================================================
"""
List comprehensions provide a concise way to create lists using a loop inside
square brackets. They are often more readable and faster than traditional loops
for simple transformations.

Syntax: [expression for item in iterable if condition]
"""

# ------------------------ Example 1: Squares of numbers ----------------------
squares = [x**2 for x in range(10)]
print(squares)   # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Equivalent for loop:
squares_loop = []
for x in range(10):
    squares_loop.append(x**2)
print(squares_loop)

# ------------------------ Example 2: With condition (filter) ----------------
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)   # Output: [0, 4, 16, 36, 64]

# ------------------------ Example 3: Nested loops in comprehension ----------
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)   # Output: [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1)]

# ------------------------ Example 4: Dictionary comprehension ---------------
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)   # Output: {0:0, 1:1, 2:4, 3:9, 4:16}

# =============================================================================
# 7. IMPORTANT POINTS, TRICKS, AND TIPS
# =============================================================================
"""
1. Avoid modifying a list while iterating over it. This can cause unexpected
   behavior. Instead, iterate over a copy or use list comprehension.

   Bad:
       for item in my_list:
           if condition:
               my_list.remove(item)

   Good:
       my_list = [item for item in my_list if not condition]

2. Use enumerate() instead of manually managing an index counter.

3. The else clause in loops is not widely known but is useful for search
   scenarios (e.g., checking if an item was found without a flag).

4. Use range() for numeric loops; it's memory efficient in Python 3 (generates
   numbers on the fly).

5. For large loops, consider using local variable caching to speed up attribute
   lookups. For example, store list.append in a local variable.

6. The underscore _ is often used as a throwaway variable when you don't need
   the value.

7. Use itertools for advanced iteration patterns (e.g., cycle, repeat, product).

8. While loops are better when the number of iterations is unknown beforehand.

9. Pass is a placeholder; use it when defining functions/classes/loops that are
   not yet implemented.

10. List comprehensions are faster than for loops for building lists, but avoid
    overly complex comprehensions that sacrifice readability.

11. The `iter()` function can convert an iterable into an iterator, and `next()`
    retrieves items manually. Useful for custom iteration control.

12. Use `for ... else` to detect if a loop completed without break, reducing
    the need for a separate flag variable.
"""

# ------------------------ Example: Using underscore for unused variable ----
# When you only need to run a loop a certain number of times
for _ in range(3):
    print("Hello")   # Output: Hello (3 times)

# ------------------------ Example: Local variable caching --------------------
# Without caching
my_list = []
for i in range(1000000):
    my_list.append(i)   # attribute lookup on each iteration

# With caching (slightly faster)
my_list = []
append = my_list.append   # local reference
for i in range(1000000):
    append(i)

# ------------------------ Example: Manual iteration with iter() and next() ----
my_iter = iter([1, 2, 3])
print(next(my_iter))   # 1
print(next(my_iter))   # 2
print(next(my_iter))   # 3
# print(next(my_iter))   # would raise StopIteration

# ------------------------ Example: Using for-else for search without flag ----
# Traditional approach
found = False
for item in [1, 2, 3, 4]:
    if item == 5:
        found = True
        break
if not found:
    print("Not found")   # Output: Not found

# Using for-else (cleaner)
for item in [1, 2, 3, 4]:
    if item == 5:
        print("Found")
        break
else:
    print("Not found")   # Output: Not found

# =============================================================================
# 8. COMMON PITFALLS
# =============================================================================
"""
- Infinite loops: Forgetting to update the loop variable in while loops.
- Off-by-one errors: Especially with range(stop) where stop is exclusive.
- Modifying a list while iterating over it leading to skipped items or errors.
- Using mutable default arguments in functions that are modified inside loops.
- Not understanding that break/continue only affect the innermost loop.
- Confusing = (assignment) with == (comparison) in while conditions.
- Overusing list comprehensions when a simple loop is clearer.
"""

# ------------------------ Example: Modifying list while iterating ------------
# Problem:
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)   # Output: [1, 3, 5] but may behave unpredictably with bigger lists

# Better approach:
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)   # Output: [1, 3, 5]

# =============================================================================
# END OF NOTES
# =============================================================================
""" 
The above examples cover the essential aspects of loops in Python.
Experiment with them, modify the code, and see how the outputs change.
Happy coding!
"""