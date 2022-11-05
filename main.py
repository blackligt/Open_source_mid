# Program make a simple calculator
'''계산기 프로그램'''

# This function adds two numbers


def add(add_num1, add_num2):
    '''
    두 수를 입력받고 더하는 함수
    '''
    return add_num1 + add_num2

# This function subtracts two numbers


def subtract(sub_num1, sub_num2):
    '''
    두 수를 입력받고 빼는 함수
    '''
    return sub_num1 - sub_num2

# This function multiplies two numbers


def multiply(mul_num1, mul_num2):
    '''
    두 수를 입력받고 곱하는 함수
    '''
    return mul_num1 * mul_num2

# Need to define divide function.


def divide(div_num1, div_num2):
    '''
    두 수를 입력받고 나누는 함수
    '''
    if div_num2 == 0:
        print("divide by zero error")
        return "error"
    else:
        return div_num1/div_num2


def end_qustion():
    '''프로그램 종료 여부를 물어보는 함수'''
    next_calculation = input("Let's do next calculation? (yes/no): ")
    low_next_calculation = next_calculation.lower()
    if low_next_calculation == "no":
        return 0

    elif low_next_calculation == "yes":
        return 1

    else:
        return end_qustion()


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        status = end_qustion()
        if status == 0:
            break
        elif status == 1:
            continue

    else:
        print("Invalid Input")
