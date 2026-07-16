# WAP to print right angled triangle using *
def right_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end = " ")
        print() # New line after each row

right_triangle(5)

def right_aligned_triangle(n):
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)

right_aligned_triangle(5)