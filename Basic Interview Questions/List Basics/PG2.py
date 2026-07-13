# WAP to print the sum of all the elements

def sum_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total

nums = [10, 20, 30, 40]
print(sum_elements(nums)) # 100