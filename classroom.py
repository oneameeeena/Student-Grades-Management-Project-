# 1. Subjects list
subjects = ["Math", "Science", "History", "Language"]

# 2. Students list
students = []  # Each student will be a dictionary: {"id": 1, "name": "Alice", "grades": {"Math": 90, ...}}

# 3. Class reports list
class_reports = []  # Each report: {"student_id": 1, "subjects": ["Math", "Science"], "grades": [90, 85]}


# ------------------ STUDENT FUNCTIONS ------------------

def add_student(student_id, name):
    student = {"id": student_id, "name": name, "grades": {}}
    students.append(student)
    print(f"Student {name} added successfully.")


def remove_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    print(f"Student with ID {student_id} removed successfully.")


def show_student(student_id):
    for student in students:
        if student["id"] == student_id:
            print(f"ID: {student['id']}, Name: {student['name']}, Grades: {student['grades']}")
            return
    print("Student not found.")


def display_all_students():
    if not students:
        print("No students in the list.")
        return
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Grades: {student['grades']}")


def search_student_by_name(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


def add_or_update_grade(student_id, subject, grade):
    if subject not in subjects:
        print(f"{subject} is not a valid subject.")
        return
    for student in students:
        if student["id"] == student_id:
            student["grades"][subject] = grade
            print(f"Grade {grade} added/updated for {subject}.")
            return
    print("Student not found.")


def remove_grade(student_id, subject):
    for student in students:
        if student["id"] == student_id:
            if subject in student["grades"]:
                del student["grades"][subject]
                print(f"Grade for {subject} removed.")
            else:
                print(f"{subject} grade not found for student.")
            return
    print("Student not found.")


# ------------------ CLASS REPORT FUNCTIONS ------------------

def add_student_to_report(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        print("Student not found.")
        return
    report = {"student_id": student_id,
              "subjects": list(student["grades"].keys()),
              "grades": list(student["grades"].values())}
    class_reports.append(report)
    print(f"Report for student ID {student_id} added.")


def remove_student_from_report(student_id):
    global class_reports
    class_reports = [r for r in class_reports if r["student_id"] != student_id]
    print(f"Report for student ID {student_id} removed.")


def show_student_report(student_id):
    report = next((r for r in class_reports if r["student_id"] == student_id), None)
    if report:
        print(f"Student ID: {student_id}")
        for subj, grade in zip(report["subjects"], report["grades"]):
            print(f"{subj}: {grade}")
    else:
        print("Report not found.")


def calculate_average(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student and student["grades"]:
        avg = sum(student["grades"].values()) / len(student["grades"])
        print(f"Total average for {student['name']}: {avg:.2f}")
        return avg
    print("No grades available for this student.")
    return None


def display_all_reports():
    if not class_reports:
        print("No reports available.")
        return
    for report in class_reports:
        print(f"Student ID: {report['student_id']}")
        for subj, grade in zip(report["subjects"], report["grades"]):
            print(f"{subj}: {grade}")
        print("-" * 20)


# ------------------ MENU ------------------

def menu():
    while True:
        print("\n--- Classroom Management Menu ---")
        print("1. Add student")
        print("2. Remove student")
        print("3. Show student details")
        print("4. Display all students")
        print("5. Search student by name")
        print("6. Add/Update student grade")
        print("7. Remove student grade")
        print("8. Add student to class report")
        print("9. Remove student from class report")
        print("10. Show student report")
        print("11. Calculate student average")
        print("12. Display all reports")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            add_student(sid, name)
        elif choice == "2":
            sid = int(input("Enter student ID to remove: "))
            remove_student(sid)
        elif choice == "3":
            sid = int(input("Enter student ID to show: "))
            show_student(sid)
        elif choice == "4":
            display_all_students()
        elif choice == "5":
            name = input("Enter student name to search: ")
            student = search_student_by_name(name)
            if student:
                print(student)
            else:
                print("Student not found.")
        elif choice == "6":
            sid = int(input("Enter student ID: "))
            subj = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            add_or_update_grade(sid, subj, grade)
        elif choice == "7":
            sid = int(input("Enter student ID: "))
            subj = input("Enter subject to remove: ")
            remove_grade(sid, subj)
        elif choice == "8":
            sid = int(input("Enter student ID to add to report: "))
            add_student_to_report(sid)
        elif choice == "9":
            sid = int(input("Enter student ID to remove from report: "))
            remove_student_from_report(sid)
        elif choice == "10":
            sid = int(input("Enter student ID to show report: "))
            show_student_report(sid)
        elif choice == "11":
            sid = int(input("Enter student ID to calculate average: "))
            calculate_average(sid)
        elif choice == "12":
            display_all_reports()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")


# Run the menu
menu()
