import os
import math
os.system('cls')


answer = 'yes'

while answer == 'yes':

    print('\nList the operation this Calculation has: ')
    print('1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Square to Root\n6. Raise to Power')
    operator = int(input('Input the number from the list: '))

    if operator == 1:
        first_number = int(input('Input the first number: '))
        second_number = int(input('Input the second number: '))
        print(f'The result is: {first_number + second_number}')
    elif operator == 2:
        first_number = int(input('Input the first number: '))
        second_number = int(input('Input the second number: '))
        print(f'The result is: {first_number - second_number}')
    elif operator == 3:
        first_number = int(input('Input the first number: '))
        second_number = int(input('Input the second number: '))
        print(f'The result is: {first_number * second_number}')
    elif operator == 4:
        first_number = int(input('Input the first number: '))
        second_number = int(input('Input the second number: '))
        print(f'The result is: {first_number / second_number}')
    elif operator == 5:
        first_number = int(input('Input the number: '))
        print(f'The result is: {math.sqrt(first_number)}')
    elif operator == 6:
        first_number = int(input('Input the first number: '))
        second_number = int(input('Input the power number: '))
        print(f'The result is: {first_number ** second_number}')
    else:
        print('your Input is not in list! ')
    
    ask = input('Do you still use this calculation (yes/no): ').lower()
    answer = ask
    