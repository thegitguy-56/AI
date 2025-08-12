# Program to remove punctuations from a given string

# List of punctuations
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Take input from user
text = input("Enter a string: ")

# Remove punctuations
result = ""
for char in text:
    if char not in punctuations:
        result += char

# Display result
print("String without punctuations:", result)
