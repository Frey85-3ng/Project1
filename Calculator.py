# Simple Calculator

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for operation
print("Choose an operation: +  -  *  /")
operation = input("Enter operation: ")

# Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Show result
print("Result:", result)
