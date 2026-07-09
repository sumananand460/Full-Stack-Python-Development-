# WAP to reverse a string without using the slicing concept
# --- DEFINING THE THREE METHODS ---

# Method 1: Using a Loop
def reverse_with_loop(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


# Method 2: Using the built-in reversed() function
def reverse_with_builtin(text):
    return "".join(reversed(text))


# Method 3: Using Recursion
def reverse_recursive(text):
    if len(text) <= 1:
        return text
    # Take the last character and pass the rest back into the function
    return text[-1] + reverse_recursive(text[:-1])


# --- GETTING USER INPUT ---

# The program pauses here to let you type your string
user_string = input("Enter a string to reverse: ")

print("\n--- RESULTS ---")
print(f"Original String: {user_string}\n")

# Calling and printing each method
print(f"Method 1 (Loop) Result:      {reverse_with_loop(user_string)}")
print(f"Method 2 (Built-in) Result:  {reverse_with_builtin(user_string)}")
print(f"Method 3 (Recursion) Result: {reverse_recursive(user_string)}")
