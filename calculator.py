def main():
    operation = get_nums()
    result = calculator(operation[0], operation[1], operation[2])
    print(f"Result: {result}")


def get_nums():
    print("This is a calculator. Enter two numbers and a operand.")
    num1 = input("Enter number 1: ")
    operand = input("Enter operand (/, *, +, -): ")
    num2 = input("Enter number 2: ")
    return num1, operand, num2


def checker(num1, num2, operand):
    operands = ['+', '-', '/', '*']
    if num1.isdigit() and num2.isdigit() and operand in operands:
        num1 = int(num1)
        num2 = int(num2)
        return True
    else:
        return False


def calculator(num1, operand, num2):
    check = checker(num1, num2, operand)
    if check == True:
        num1, num2 = int(num1), int(num2)
        if operand == '+':
            return num1 + num2
        elif operand == '-':
            return num1 - num2
        elif operand == '/':
            return num1 / num2
        elif operand == '*':
            return num1 * num2
    elif check == False:
        print("Invalid input")
        quit()


main()