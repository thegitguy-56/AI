# Program to sort words in a sentence alphabetically

# Take sentence input from user
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Sort words alphabetically (case-insensitive)
words.sort(key=str.lower)

# Join sorted words back into a sentence
sorted_sentence = " ".join(words)

# Display the result
print("Sorted sentence:", sorted_sentence)
