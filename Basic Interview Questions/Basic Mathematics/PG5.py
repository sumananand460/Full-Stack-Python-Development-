# Q - WAP to calculate the power

def power_loop(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

x, n = 2, 5
print(power_loop(x, n))  # 32
print(x ** n)             # 32, using operator
print(pow(x, n))          # 32, using built in function

# For negative power
print(pow(2, -2))  # 0.25