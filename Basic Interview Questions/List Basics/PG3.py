# WAP to count the number of occurence in the list
def count_occurence(arr, target):
    count = 0
    for item in arr:
        if item == target:
            count += 1
    return count

nums = [1,2,2,2,3,4,5,6]
print(count_occurence(nums, 2)) 

# Shortcut version using built in method
print(nums.count(2))