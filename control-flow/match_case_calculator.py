# match_case_calculator.py

# Prompt the user for input
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the inputs to float numbers and handle invalid inputs
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Please enter valid numbers.")
    exit()

# Prompt the user for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")
