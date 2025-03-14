# Student Report Card Generator

# Initialize an empty list to store multiple students
students = []

while True:
    # Get student details
    name = input("\nEnter student's name: ")
    roll_number = input("Enter roll number: ")

    # Define fixed subjects
    subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
    marks = {}

    # Input subject marks with error handling
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:  # Marks should be between 0 and 100
                    marks[subject] = mark
                    break
                else:
                    print("Marks should be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    # Calculate total marks
    total_marks = sum(marks.values())

    # Calculate percentage
    percentage = (total_marks / 500) * 100  # Total possible marks = 500

    # Assign Grade based on percentage
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    # Store student data in a dictionary
    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "total_marks": total_marks,
        "percentage": percentage,
        "grade": grade
    }

    # Add student to the list
    students.append(student)

    # Confirm with the user if they want to enter more students
    while True:
        more_students = input("\nRecord inserted successfully. Do you want to insert more? (Y/N): ").strip().upper()
        if more_students in ["Y", "N"]:
            break
        else:
            print("Invalid choice! Please enter 'Y' for Yes or 'N' for No.")

    if more_students == "N":
        break  # Exit the loop if user chooses not to enter more students

# Generate and Display the Report Cards for all students
print("\n" + "=" * 40)
print("        STUDENT REPORT CARDS")
print("=" * 40)

for student in students:
    print("\n" + "-" * 40)
    print(f"Student Name : {student['name']}")
    print(f"Roll Number  : {student['roll_number']}")
    print("-" * 40)

    print("Subjects      Marks")
    print("-" * 40)

    # Loop through the subjects to display marks
    for subject, marks in student["marks"].items():
        print(f"{subject:<12} {marks:.2f}")  # Aligns subject names properly

    print("-" * 40)
    print(f"Total Marks  : {student['total_marks']:.2f}")
    print(f"Percentage   : {student['percentage']:.2f}%")
    print(f"Grade        : {student['grade']}")
    print("-" * 40)

print("\nAll report cards generated successfully!")

