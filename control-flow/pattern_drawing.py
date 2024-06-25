# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Generate and print the pattern using nested loops
while row < size:
    # Use a for loop to print asterisks side by side without advancing to a new line
    for col in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Increment the row counter
    row += 1
