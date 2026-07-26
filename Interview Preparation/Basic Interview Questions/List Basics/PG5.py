# WAP to remove the duplicates from the list
def remove_duplicates(arr):
    seen = []
    result = []
    for item in arr:
        if item not in seen:
            seen.append(item)
            result.append(item)
    return result

nums = [1,2,3,4,5,1,2,2,4,3,5]
print(remove_duplicates(nums))