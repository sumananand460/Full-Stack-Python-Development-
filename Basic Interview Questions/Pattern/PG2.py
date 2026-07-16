# Star pyramid
def star_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i  # use "*"* (2*i-1) for compact pyramid
        # For compact version: stars = "*" * (2*i - 1)
        print(spaces + stars)

star_pyramid(5)