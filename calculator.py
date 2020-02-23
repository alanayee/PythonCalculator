import math
def calculate():
    operation = raw_input('''
	Please type in the math operation you would like to complete:
	+ for addition
	- for subtraction
	* for multiplication
	/ for division
    ^ for exponential value
    abs for absolute value
	''')

    if operation == '+':
        x, y = get_User_Input2()
        print('{} + {} = '.format(x, y))
        print(x + y)

    elif operation == '-':
        x, y = get_User_Input2()
        print('{} - {} = '.format(x, y))
        print(x - y)

    elif operation == '*':
        x, y = get_User_Input2()
        print('{} * {} = '.format(x, y))
        print(x * y)

    elif operation == '/':
        x, y = get_User_Input2()
        print('{} / {} = '.format(x, y))
        print(x / y)
    elif operation == '^':
        x, y = get_User_Input2()
        print (math.pow(x,y))
    elif operation == 'abs':
        x = get_User_Input1()
        # print("x is = ", x)
        print (math.fabs(x))
    else:
        print('You have not typed a valid operator, please run the program again.')

    
    
    calc_again = raw_input('''Do you want to calculate again? Please type Y for YES or N for NO.''')
    if calc_again == 'Y':
        calculate()
    elif calc_again == 'N':
        print('See you later.')
    else:
        print('Invalid input. Try again.')


def get_User_Input1():
    x = float(raw_input('Please enter a number:'))
    return x
def get_User_Input2():
    x = float(raw_input('Please enter the first number: '))
    y = float(raw_input('Please enter the second number: '))
    return x, y

def main():
    calculate()




if __name__ == "__main__":
    main()
