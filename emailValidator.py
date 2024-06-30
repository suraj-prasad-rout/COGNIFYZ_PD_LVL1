import regex  # Importing the 'regex' module for advanced regular expressions


def validEmail(email):
    # Define the regex pattern for validating email addresses
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    # Use regex.match() to check if the 'email' matches the pattern
    if regex.match(pattern, email):
        return True  # If it matches, return True (valid email)
    else:
        return False  # If it doesn't match, return False (invalid email)


# Prompt the user to enter an email addres
email = input("Enter your E-mail\n")
if validEmail(email):
    # Print confirmation if the email is valid
    print(f"{email} is a valid email")
else:
    # Print error message if the email is not valid
    print(f"{email} is not a valid email")
