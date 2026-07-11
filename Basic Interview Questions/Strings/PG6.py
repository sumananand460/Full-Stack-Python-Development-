# Question 6: Checking if string contains only digits

def is_only_digits(s):
    return s.isdigit()

print(is_only_digits("12345"))
print(is_only_digits("123dsd"))
print(is_only_digits("12.4"))
print(is_only_digits("0.ad"))