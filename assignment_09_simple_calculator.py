# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
from time import sleep #I'm importing it just to make sure you see the goodbye message.

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Second Number cannot be zero"
    return round(num1/num2, 2)

def modulus(num1, num2):
    if num2 == 0: return "Second Number cannot be zero"
    return num1 % num2

def expo(num1, num2):
    return num1 ** num2

def main():
    while True:
        print(
            """
    ============================
         SIMPLE CALCULATOR
    ============================
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulus
    6. Exponentiation
    7. Quit
    """
        )
        try:
            choice = int(input("Select an operation (1-7):"))
            if choice == 7:
                print("Goodbye!✌️")
                sleep(2)
                return False

            if choice not in range(8):
                print("Out of range. Must be between 1 - 7")
                continue

            number1 = int(input("Enter first number: "))
            number2 = int(input("Enter second number: "))

            if choice == 1:
                print(addition(number1, number2))
            elif choice == 2:
                print(subtraction(number1, number2))
            elif choice == 3:
                print(multiplication(number1, number2))
            elif choice == 4:
                print(division(number1, number2))
            elif choice == 5:
                print(modulus(number1, number2))
            elif choice == 6:
                print(expo(number1, number2))
        except ValueError:
            print("Invalid Input must be an integer.")
        

if __name__ == "__main__":
    main()