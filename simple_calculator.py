import math

def calculator(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return 'Error: can not divide by zero'
        else:
            return num1 / num2
    elif op == 'sqrt':
        if num1 <0:
            return 'negative number is not allowed'
        else:
            return math.sqrt(num1)
    elif op == 'power':
        return pow(num1, num2)
    else:
        return 'Error: invalid operator'

def main():
    op = input('Enter an arithmetic operator (+, -, *, /, power, sqrt): ')
    #if the operation is sqrt, only recieve one non negative number
    if op == 'sqrt':
        num1 = float(input('Enter the number(non negative only): '))
        result = calculator(num1, 0, 'sqrt')
    #else recieve 2 numbers
    else:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        result = calculator(num1, num2, op)
    print('Result:', result)

#forever loop to do the calculation
while 1:
    main()

#ขอยืนยันว่าทำด้วยตนเอง 100% มโนภัทร ชาญกล้้า