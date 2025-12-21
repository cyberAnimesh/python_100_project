def calculator():
    print("Simple Calculator")
    print("Operators: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                print("Result:", num1 + num2)
            elif op == '-':
                print("Result:", num1 - num2)
            elif op == '*':
                print("Result:", num1 * num2)
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed")
                else:
                    print("Result:", num1 / num2)
            else:
                print("Invalid operator")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        choice = input("Do you want to continue (y/n): ")
        if choice.lower() != 'y':
            break

calculator()
