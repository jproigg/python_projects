
def suma(n1,n2):
    return n1 + n2

def resta(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

def calc():

    num1 = float(input('enter number: '))
    operations = {
        "+": suma,
        "-": resta,
        "*": multi,
        "/": division
    }
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        #num1 = first_answer
        operation_symbol = input("enter your operation: ")
        num2 = float(input('enter second number: '))
        calculator_function = operations[operation_symbol]
        first_answer = calculator_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {first_answer}')

        new_operation = input(f"type 'y' to continue with {first_answer} or 'n' to exit: " )

        if new_operation == "y":
            num1 = first_answer     
        else:
            should_continue = False
            calc()

    

calc()
