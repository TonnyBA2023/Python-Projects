students = {}

def add_student(name, marks):
    students[name] = marks

def view_students():
    if not students:
        print("No students available.")
        return

    for name, marks in students.items():
        print(f"{name}: {marks}")

def delete_student(name):
    if name in students:
        del students[name]
        print("Student deleted.")
    else:
        print("Student not found.")

add_student("John", 85)
add_student("Mary", 92)

view_students()
