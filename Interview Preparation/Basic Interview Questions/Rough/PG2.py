# WAP to check if a word or number is palindrome or not

user_input = input("Enter your word or number: ")

cleaned_input = user_input.lower()

if cleaned_input == cleaned_input[::-1]:
    print("Yes it is palindrome.")
else:
    print("No its not palindrome.")