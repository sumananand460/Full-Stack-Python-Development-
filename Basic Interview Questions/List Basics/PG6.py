# WAP to find the second largest number from the list

def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num!= largest:
            second = num

    return second if second!= float('-inf') else None

nums = [12, 35, 1, 10, 34, 1]
print(second_largest(nums)) # 