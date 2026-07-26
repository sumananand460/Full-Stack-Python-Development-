# Q - WAP to find minimum and maximum from a list without Built-in functions
def find_max_min(arr):
    if not arr:
        return None, None
    
    max_val = arr[0]
    min_val = arr[0]

    for num in arr[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val
    
nums = [4, 1, 9, 3, 7]
maximum, minimum = find_max_min(nums)
print(f"Max: {maximum}, Min: {minimum}") # Max: 9, Min: 1