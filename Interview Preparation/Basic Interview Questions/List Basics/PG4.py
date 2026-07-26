# WAP to check if the element exists
def element_exists(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

# Manual way
nums = [1,2,3,44,24,445]
print(element_exists(nums, 34)) # False

# Pythonic Way
print(44 in nums) # True