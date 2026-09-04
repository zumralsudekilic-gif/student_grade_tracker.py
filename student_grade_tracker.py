students = []

while True:
    print("\n---- Student Grade Tracker ----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Find Highest Grade")
    print("5. Check Pass/Fail Status")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()
        try:
            grade = float(input("Enter student grade: "))
        except ValueError:
            print("Please enter a valid numeric grade.")
            continue

        students.append({"name": name, "grade": grade})
        print("Student successfully added!")

    elif choice == "2":
        if not students:
            print("No students have been added yet.")
        else:
            print("\n--- Student List ---")
            for student in students:
                print(student["name"], "-", student["grade"])

    elif choice == "3":
        if not students:
            print("No students have been added yet.")
        else:
            average = sum(student["grade"] for student in students) / len(students)
            print("Class average:", average)

    elif choice == "4":
        if not students:
            print("No students have been added yet.")
        else:
            highest_student = max(students, key=lambda student: student["grade"])
            print(
                "Highest grade:",
                highest_student["name"],
                "-",
                highest_student["grade"],
            )

    elif choice == "5":
        if not students:
            print("No students have been added yet.")
        else:
            print("\n--- Pass/Fail Status ---")
            for student in students:
                status = "Passed" if student["grade"] >= 50 else "Failed"
                print(student["name"], "-", status)

    elif choice == "6":
        print("Thank you for using Student Grade Tracker!")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 6.")
