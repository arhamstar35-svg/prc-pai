import json

# Initial data
students = [
    {"id": 1, "name": "Ali", "marks": 85},
    {"id": 2, "name": "Ahmed", "marks": 45},
    {"id": 3, "name": "Sara", "marks": 92}
]

# Create JSON file and write data
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)


while True:
    print("\n--- Student Management System ---")
    print("1. Display all students")
    print("2. Add a student")
    print("3. Search for a student")
    print("4. Update student marks")
    print("5. Delete a student")
    print("6. Display students who passed")
    print("7. Find student with highest marks")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # Read data from JSON file
    with open("students.json", "r") as file:
        students = json.load(file)

    if choice == "1":
        for student in students:
            print(student)

    elif choice == "2":
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        students.append({
            "id": student_id,
            "name": name,
            "marks": marks
        })

        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Student added successfully!")

    elif choice == "3":
        student_id = int(input("Enter ID to search: "))
        found = False

        for student in students:
            if student["id"] == student_id:
                print(student)
                found = True

        if found == False:
            print("Student not found.")

    elif choice == "4":
        student_id = int(input("Enter ID to update: "))
        found = False

        for student in students:
            if student["id"] == student_id:
                new_marks = int(input("Enter new marks: "))
                student["marks"] = new_marks
                found = True

        if found:
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            print("Marks updated successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        student_id = int(input("Enter ID to delete: "))
        found = False
        new_students = []

        for student in students:
            if student["id"] != student_id:
                new_students.append(student)
            else:
                found = True

        if found:
            with open("students.json", "w") as file:
                json.dump(new_students, file, indent=4)

            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "6":
        for student in students:
            if student["marks"] >= 50:
                print(student)

    elif choice == "7":
        if len(students) > 0:
            highest = students[0]

            for student in students:
                if student["marks"] > highest["marks"]:
                    highest = student

            print("Highest-scoring student:", highest)
        else:
            print("No students available.")

    elif choice == "8":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")