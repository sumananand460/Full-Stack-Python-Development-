def print_1_to_n(n):
    for i in range(1, n + 1):
        print(i, end=" ")

print_1_to_n(10)  # 1 2 3 4 5 6 7 8 9 10

# Using while loop
def print_1_to_n_while(n):
    i = 1
    while i <= n:
        print(i)
        i += 1