# Question 3: Find the length of the string without the len()
def find_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

text = "Python"
print(find_length(text))


# with len()
a = "Elephant"
print(len(a))