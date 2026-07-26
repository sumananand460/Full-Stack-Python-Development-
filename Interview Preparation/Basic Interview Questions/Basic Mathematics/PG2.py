# Q - Choose the largest number from the three
a, b, c = 101, 20, 360
print(max(a, b, c))

# Method 2:
# Using manual method to call out the largest number
def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(f"Largest number is: {largest_number(12, 56, 70)}")
