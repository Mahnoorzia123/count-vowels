# Ask the user to enter a string
text = input("Enter a string: ")

# Define the vowels
vowels = "AEIOUaeiou"

# Set counter to 0
count = 0

# Loop through each character in the string
for char in text:
    if char in vowels:
        count += 1  # Add 1 if character is a vowel

# Print the total number of vowels
print("Number of vowels:", count)
