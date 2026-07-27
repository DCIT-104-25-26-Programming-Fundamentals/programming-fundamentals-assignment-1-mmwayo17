# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def create_matrix(row_number, column_number):
    column = []
    matrix = []

    for i in range(row_number):
        row = input(f"Enter row {i + 1}: ").split()
        for j in range(column_number):
            column.append(int(row[j]))

        matrix.append(column)
        column = []

    return matrix

def print_matrix(matrix):
    if matrix:
        for row in range(len(matrix)):
            print(matrix[row])
        
        print("-------------")


def transpose(matrix):
    transpose_matrix = []
    for _ in range(len(matrix[0])):
        transpose_matrix.append([])

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transpose_matrix[i].append(matrix[j][i])

    return transpose_matrix

def add_matrix(matrix1, matrix2):
    added_matrix = []

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2):
        return print("Matrix Size do not match. Must be of equal size(MxN)")

    for _ in range(len(matrix1)):
        added_matrix.append([])

    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            added_matrix[i].append(matrix1[i][j] + matrix2[i][j])

    return added_matrix

def multiply_matrix(matrix1, matrix2):
    multiplied_matrix = []

    if len(matrix1[0]) != len(matrix2):
        return print("Both matrices cannot multipy.Size of Row 1 of matrix 1 must match size of column 1 of matrix 2")

    for _ in range(len(matrix1)):
        multiplied_matrix.append([])

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix1[0])):
                sum += matrix1[i][k] * matrix2[k][j]

            multiplied_matrix[i].append(sum)
            sum = 0

    return multiplied_matrix

def main():
    row_number = int(input("Enter number of rows: "))
    column_number = int(input("Enter number of columns: "))

    #These are my test cases for the functions. Try for yourself.
    matrix = create_matrix(row_number, column_number)
    transpose_matrix = transpose(matrix)
    added_matrix = add_matrix(matrix, transpose_matrix)
    multiplied_matrix = multiply_matrix(matrix, transpose_matrix)

    print_matrix(matrix)
    print_matrix(transpose_matrix)
    print_matrix(added_matrix)
    print_matrix(multiplied_matrix)

if __name__ == "__main__":
    main()