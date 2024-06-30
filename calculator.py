# Prompt the user to enter the first number and convert it to an integer
num1 = int(input("Enter the first number\n"))

# Prompt the user to enter the second number and convert it to an integer
num2 = int(input("Enter the second number\n"))

# Prompt the user to enter an operator from the list of supported operators
operator = input("Enter an operator in between +, -, *, /, %\n")

# Use a match-case statement to perform the corresponding operation based on the operator entered
match operator:
    case '+':  # If the operator is '+', perform addition
        print(f"{num1} + {num2} = {num1 + num2}")

    case '-':  # If the operator is '-', perform subtraction
        print(f"{num1} - {num2} = {num1 - num2}")

    case '*':  # If the operator is '*', perform multiplication
        print(f"{num1} * {num2} = {num1 * num2}")

    case '/':  # If the operator is '/', perform division and format the result to 2 decimal places
        print(f"{num1} / {num2} = {num1 / num2 :.2f}")

    case '%':  # If the operator is '%', perform modulo operation
        print(f"{num1} % {num2} = {num1 % num2}")
