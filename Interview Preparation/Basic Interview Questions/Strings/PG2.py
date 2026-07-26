# Question 2: Counting Vowels
def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count

text = input("Enter your string: ")
print(f"Vowel Count: {count_vowels(text)}")