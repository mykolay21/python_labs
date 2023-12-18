import art


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add, "-": subtract, "*": multiply, "/": divide
}


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    for k in operations:
        print(k)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick operation symbol from the line above:")
        num2 = (input("What's the next number?: "))
        f = operations[operation_symbol]
        answer = f(num1, num2)

        print(f"{num1}  {operation_symbol} {num2}  = {answer}")

        if input(f"Type   'y' to continue calculation with {answer} , or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
