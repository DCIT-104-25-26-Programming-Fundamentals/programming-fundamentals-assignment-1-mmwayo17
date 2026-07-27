# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_single_table(n):
    if n < 0:
        return None
    
    for i in range(12):
        print(f"{n} x {i + 1} = {n * (i +1)}")

def generate_multiple_tables(n):
    if n < 0:
        return None
    
    for i in range(n):
        for j in range(12):
            print(f"{i+1} x {j + 1} = {(i + 1) * (j +1)}")

        print("-------------------------------")

def main():
    number = int(input("Enter Number: "))
    if number > 0:
        generate_single_table(number)
    else:
        print("Invalid Input")
        return

    number2 = int(input("Enter Number For Multiple Tables: "))
    if number2 > 0:
        generate_multiple_tables(number2)
    else:
        print("Invalid Input")
        return


if __name__ == "__main__":
    main()