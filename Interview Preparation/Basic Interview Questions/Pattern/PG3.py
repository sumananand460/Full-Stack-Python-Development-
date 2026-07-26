def number_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        nums = ""
        for j in range(1, i + 1):
            nums += str(j) + " "
        print(spaces + nums)

number_pyramid(5)