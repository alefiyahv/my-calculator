# Basic Calculator Program

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    if y == 0:
        print("Error! Division by zero.")
        return None
    else:
        return x / y

# This is the main loop of the program
while True:
    # Take input from the user
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Perform calculation based on the operation
    if operation == '+':
        print("The result is:", add(num1, num2))
    elif operation == '-':
        print("The result is:", subtract(num1, num2))
    elif operation == '*':
        print("The result is:", multiply(num1, num2))
    elif operation == '/':
        result = divide(num1, num2)
        if result is not None:
            print("The result is:", result)
    else:
        print("Invalid operation selected!")

    # Ask the user if they want to calculate again
    next_calculation = input("Would you like to do another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break

print("Thank you for using the calculator.")
