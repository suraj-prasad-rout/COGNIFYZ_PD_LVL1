string = input("Enter a string\n")  # Prompt the user to enter a string
reversedString = string[::-1]  # Reverse the string using slicing

if (string == reversedString):  # Check if the original string is equal to the reversed string
    # If they are equal, print that the string is a palindrome
    print(f"{string} is a palindrome string")
else:
    # If they are not equal, print that the string is not a palindrome
    print(f"{string} is not a palindrome string")
