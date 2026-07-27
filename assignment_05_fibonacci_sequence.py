# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_fibonacci_numbers(n):
    nums = [0, 1]
    if n < 0:
        return None

    if n == 1:
        return [nums[0]]
    
    for i in range(n - 2):
        fibonacci_number = nums[i] + nums[i + 1]
        nums.append(fibonacci_number)
    
    return nums

def check_fibonacci_number(n):
    nums = generate_fibonacci_numbers(n + 1)
    if n in nums:
        return True
    else:
        return False

def main():
    number_of_terms = int(input("How many terms? "))
    fibonacci_numbers = generate_fibonacci_numbers(number_of_terms)

    if fibonacci_numbers:
        print(fibonacci_numbers)
    else:
        print("Invalid Input")

    check_number = int(input("Enter a number to check: "))
    if check_fibonacci_number(check_number):
        print(f"{check_number} is a fibonacci number")
    else:
        print(f"{check_number} is not a fibonacci number")


if __name__ == "__main__":
    main()