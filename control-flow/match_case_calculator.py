#prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

#perform the operation using match case
result = 0
match operation:
    case '+':
         result = num1 + num2
    case '-':
         result = num1 - num2
    case '*':
         result = num1 * num2
    case '/':
        if num2 != 0:
         result = num1 / num2
        else:
         print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")

#Displaying the result
if operation in ['+', '-', '*', '/']:
    print(f"The result is {result}.")

