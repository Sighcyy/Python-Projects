import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


calculator_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}



def calculator():
    print(art.logo)
    main_num = float(input("What's the first number?: "))


    cont = True

    while cont:
        next_num = float(input("What's the next number?: "))
        print("+")
        print("-")
        print('*')
        print('/')
        operation = str(input("Pick an operation: "))
        answer = calculator_dict[operation](main_num, next_num)
        print(str(main_num), operation, next_num, "=", answer)
        choice = input("Type 'y' to continue current calculation or 'n' to do a new calculation: ")
        if choice == "y":
            main_num = answer
        else:
            cont = False
            print("\n" * 40)
            calculator()


calculator()
