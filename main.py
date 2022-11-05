# Program make a simple calculator
'''계산기 프로그램'''

import logging
formatter = logging.Formatter('%(asctime)s %(message)s')

logger_1 = logging.getLogger('normal_log')
logger_1.setLevel(logging.INFO)
logger_2 = logging.getLogger('erroer_log')
logger_2.setLevel(logging.ERROR)


file_handler_1 = logging.FileHandler('./normal.log')
file_handler_1.setFormatter(formatter)
file_handler_2 = logging.FileHandler('./error.log')
file_handler_2.setFormatter(formatter)

logger_1.addHandler(file_handler_1)
logger_2.addHandler(file_handler_2)

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
    return div_num1/div_num2


def end_qustion():
    '''프로그램 종료 여부를 물어보는 함수'''
    next_calculation = input("Let's do next calculation? (yes/no): ")
    low_next_calculation = next_calculation.lower()
    if low_next_calculation == "no":
        end_answer = input("Are you sure? (yes/no): ")
        low_end_answer = end_answer.lower()
        if low_end_answer == "yes":
            return 0

        else:
            return 1

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
            answer = add(num1, num2)
            print(num1, "+", num2, "=", answer)
            logger_1.info("%d + %d = %d calculated", num1, num2, answer)

        elif choice == '2':
            answer = subtract(num1, num2)
            print(num1, "-", num2, "=", answer)
            logger_1.info("%d - %d = %d calculated", num1, num2, answer)

        elif choice == '3':
            answer = multiply(num1, num2)
            print(num1, "*", num2, "=", answer)
            logger_1.info("%d * %d = %d calculated", num1, num2, answer)

        elif choice == '4':
            if num2 == 0:
                print("divide zero error")
                logger_2.error("divide zero error")
            else:
                answer = divide(num1, num2)
                print(num1, "/", num2, "=", answer)
                logger_1.info("%d / %d = %d calculated", num1, num2, answer)

        # check if user wants another calculation
        # break the while loop if answer is no
        status = end_qustion()
        if status == 0:
            break
        elif status == 1:
            continue

    else:
        print("Invalid Input")
        logger_2.error("Invalid Input error")
