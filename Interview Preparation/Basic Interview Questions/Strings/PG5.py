# Question 5: Count Words

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "  Python is very powerful   "
print(f"Word count: {(count_words(sentence))}") # Counts the number of words in the sentence. Which is 4 here...