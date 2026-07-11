# Reverse a string without slicing
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result  # Prepend each character
    return result

# Test
print(reverse_string("Python"))  # nohtyP
print(reverse_string("hello"))   # olleh