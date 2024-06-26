print("Welcome to the calculator")


def Addition(a, b):
    return a + b


def Subtraction(a, b):
    return a - b


def Multiplication(a, b):
    return a * b


def Division(a, b):
    return a / b


operations = {
    "+": Addition,
    "-": Subtraction,
    "*": Multiplication,
    "/": Division
}
num1=float(input("What is your first number? "))

for operation in operations:
      print(operation)
should_continue = True
while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False