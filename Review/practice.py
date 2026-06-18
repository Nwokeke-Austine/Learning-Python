num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

operation = input("Choose operation (+, -, *, /): ")

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

result = calculate(num1, num2, operation)

print("Result:", result)