# What is function?
# -> Function is a reusuable block of code to perform a specific task.
# You define a fucntion once and declare it anywhere.

def greet(name):
    return f"Hello World! My name is {name}!"

print(greet("Alice"))

# Types of functions
"""
1. Built-in Function: Predefined functions. Ex- len(), print(), max()
2. User-defined Function: Created by the user. Ex- def my_fucntion():
3. Lambda Functions: Anonymous Function or Single-Expression. Ex- Lambda x: x^2
"""

# Function Parameters - Default Parameters
def default(name = "World"):
    return f"Hello {name}!"

print(default())    # Gives default parameter which is "World"
print(default("Suman")) # Gives the argument which is "Suman"