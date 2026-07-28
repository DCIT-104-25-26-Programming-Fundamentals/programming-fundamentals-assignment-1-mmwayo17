# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def add():
    student_record = {}
    try:
        name = input("Student Name: ")
        id = int(input("Student Id: "))
        scores = []
        number = int(input("How many scores? "))

        for i in range(number):
            score = float(input(f"Enter Score {i + 1}: "))
            scores.append(score)

        student_record["name"] = name
        student_record["id"] = id
        student_record["Scores"] = scores
    except ValueError:
        print("Invalid Input")
        return None

    return student_record

def average(scores):
    sum = 0
    for score in scores:
        sum += score

    return sum/len(scores)


def display(records):
    views = []
    for record in records:
        views.append(f"""
    --------------------------------------------------
    {record["name"]}         {record["id"]}          {record["Scores"]}         {round(average(record["Scores"]))}
    --------------------------------------------------
        """)

    return views    
    

def main():
    student_records = []
    while True:
        print(
            """
            ================================
               STUDENT RECORD SYSTEM MENU
            ================================
            1. Add student
            2. Display all students
            3. Calculate average score
            4. Quit
            """
        )
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid Input must be a number")
            continue

        if choice == 1:
            record = add()
            if record:
                student_records.append(record)
            else:
                continue

        elif choice == 2:
            display_students = display(student_records)
            print("""--------------------------------------------------
    Name           ID          Scores         Average""" )

            for student in display_students:
                print(f"{student}")

        elif choice ==3:
            id = int(input("Enter Student Id: "))
            for student in student_records:
                if student["id"] == id:
                    print(round(average(student["Scores"]), 2))

        elif choice == 4:
            return False
        
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()