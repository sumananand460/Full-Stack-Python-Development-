def print_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")

print_table(7)

# One line version with list comprehension for quick display
# [print(f"7 x {i} = {7*i}") for i in range(1, 11)]