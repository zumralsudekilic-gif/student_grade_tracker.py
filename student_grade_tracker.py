students = []

while True:
    print("\n---- Student Grade Tracker ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Find Highest Grade")
    print("5. Check Pass/Fail Status")
    print("6. Exit")

    choice = input("Chooese an option (1-6):  ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))

        student = {
            "name": name,
            "grade": grade
        }

        students.append(student)

        print("Student successfully added!") 

elif choice == "2":
    if len(students) == 0:
        print("No students have been added yet.")
    else:
        print("\n--- Student List ---")

        for student in students:
            print(student["name"], "-", student["grade"])

elif choice == "3":
    if len(students) == 0:
        print("No students have been added yet.")
    else:
        total = 0

        for student in students:
            total += student["grade"]

        average = total / len(students)

        print("Class average:", average)

elif choice == "4":
    if len (students) == 0:
        print("No students have been added yet.")
    else:
        highest_student = students[0]

        for student in students:
            if student["grade"] > highest_student["grade"]:
                highest_student = student

        print(
            "Highest grade:",
            highest_student["name"],
            "-",
            highest_student["grade"]
        )

elif choice == "5":
    if len(students) == 0:
        print("No students have been added yet.")
    else:
        print("/n--- Pass/Fail Status ---")

        for student in students:
            if student["grade"] >= 50:
                print(student["name"], "- Passed")
            else:
                print(student["name"], "- Failed")

elif choice == "6":
    print("Thank you for using Student Grade Tracker!")
    break
else:
    print("Invalid choice. Please select a number between 1 and 6.")

      
  
