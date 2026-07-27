# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_numbers(amount):
    nums_list =[]
    for i in range(amount):
        num = int(input(f"Enter Number {i+1}: "))
        nums_list.append(num)

    return nums_list

def sum(nums):
    sum = 0
    for num in nums:
        sum += num

    return sum

def max(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num

    return max

def min(nums):
    min = nums[0]
    for num in nums:
        if num < min:
            min = num

    return min

def average(nums):
    sum = 0
    for num in nums:
        sum += num

    return sum/len(nums)

def main():
    amount_of_numbers = int(input("How many numbers? "))
    if amount_of_numbers < 1:
        print("Invalid Input")
        return
    nums = add_numbers(amount_of_numbers)

    print("Results")
    print(f"sum: {sum(nums)}")
    print(f"Average: {average(nums)}")
    print(f"Max: {max(nums)}")
    print(f"Min: {min(nums)}")


if __name__ == "__main__":
    main()