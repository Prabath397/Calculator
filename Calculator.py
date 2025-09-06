# Simple Calculator Project (Non-Ending Version)

while True:
    # Get numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Keep asking until valid operation
    while True:
        print("Choose operation: +, -, *, /, ^, % (or type q to quit)")
        operation = input("Enter operation: ")

        if operation == "q":
            print("Exiting calculator. Goodbye!")
            exit()   # stops the whole program

        if operation == "+":
            print("Result:", num1 + num2)
            break
        elif operation == "-":
            print("Result:", num1 - num2)
            break
        elif operation == "*":
            print("Result:", num1 * num2)
            break
        elif operation == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero")
            break
        elif operation == "^":
            print("Result:", num1 ** num2)
            break
        elif operation == "%":
            if num2 != 0:
                print("Result:", num1 % num2)
            else:
                print("Error: Cannot take modulus by zero")
            break
        else:
            print("❌ Invalid operation. Please try again.")

    print("Calculation complete ✅\n")  # adds spacing before next loop
