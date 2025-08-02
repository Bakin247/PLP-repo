def calculator():
    print("Simple Python Calculator")
    print("Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division)")

    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: You can't divide by zero!")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation! Please use +, -, *, or /.")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    calculator()