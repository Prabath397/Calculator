4# Simple Calculator Project

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get operation
print("Choose operation: +, -, *, /, ^, %")
operation = input("Enter operation: ")

# Perform calculation
if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
elif operation == "^":
    print("Result:", num1 ** num2)
elif operation == "%":
    if num2 != 0:
        print("Result:", num1 % num2)   # <--- new feature
    else:
        print("Error: Cannot take modulus by zero")
else:
    print("Invalid operation")
