
# pylint: disable=W0123

'''
DOCSTRING: This script contains all necessary functions
SOURCE OF INFORMATION: https://towardsdatascience.com/python-eval-built-in-function-601f87db191
                       https://regex101.com/
'''

import os # --> Used for clean the terminal after run the calculator again
import sys # --> Used for finish the process and exit the script
import re # --> Regex used to evaluate the user input inside the program


def welcome():
    """"Welcome message"""
    print("Welcome to Wonderfull World of Calculating!!")

def print_operations():
    """"Print all operations"""
    print("""
        For operations, just type:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        ** for power
        % for modulo
    """)


def calculate():
    """Primary calculate function"""

    # Clear the screen
    os.system('cls||clear')

    # Call info functions
    welcome()
    print_operations()

    # Variables definition
    first = None
    second = None
    operation = None

    # User operation input
    operation = input("Please enter the operation: ")
    while bool(re.match(r"^[\-\+\*\/\%]{1}[\*]?$",operation)) is False:
        print("\nYou haven't typed a valid operator! Please, try again\n")
        operation = input("Please enter the operation: ")

    # User first input
    first = input("Please enter the first number: ")
    while bool(re.match(r"^-?\d+\.?\d*$",first)) is False:
        print("\nYou have not typed a valid number! Please, try again\n")
        first = input("Please enter the first number: ")

    # User second input
    second = input('Please enter the second number: ')
    while bool(re.match(r"^-?\d+\.?\d*$",second)) is False:
        print("\nYou have not typed a valid number! Please, try again\n")
        second = input("Please enter the second number: ")

    # Build the full operation
    full_operation = first+operation+second

    # Try -- Except block
    try:
        expression = eval(full_operation)
        print("\nThe results is: {}\n".format(expression))
        run_again()
    except ZeroDivisionError:
        print("\nError: Can't divide by 0!!\n")
        run_again()
    except SyntaxError:
        print("\nError: You entered a wrong operator!!\n")
        run_again()


def run_again():
    """"Run the script again"""
    keep_calculating = input("""To calculate again, please type Y/y for Yes or N/n for No: """)

    if keep_calculating.upper() in ('Y','N'):
        # The input can be 'y' or 'Y'
        if keep_calculating.upper() == 'Y':
            calculate()
        # The input can be 'n' or 'N'
        elif keep_calculating.upper() == 'N':
            print()
            sys.exit("Bye Bye! See you later.")
        else:
            run_again()
    else:
        print("\nYou have not typed a valid answer! Please, type Y/y ou N/n.\n")
        run_again()


# Execute the Calculator
calculate()
