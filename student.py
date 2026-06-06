import time
import json

students = []

class Student:
    
    count = 0
    total_marks = 0

    def __init__(self, name, section, roll_no, marks):
        self.name = name
        self.section = section
        self.roll_no = roll_no
        self.marks = marks
        Student.count += 1
        Student.total_marks += marks

    def get_info(self):
        return (
    "-----------------------------------\n"
    f"Name : {self.name}\n"
    f"Section : {self.section}\n"
    f"Roll No : {self.roll_no}\n"
    f"Marks : {self.marks}\n"
    "-----------------------------------"
)

    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
            return cls.total_marks/cls.count
    @classmethod
    def get_count(cls):
        return f"Total students = {cls.count}"
    
    def __str__(self):
        return self.get_info()
    

def save():
    data = []
    for student in students:
        data.append({
            "name": student.name,
            "section": student.section,
            "roll_no": student.roll_no,
            "marks": student.marks
        })
    with open("students.json", "w") as file:
        json.dump(data, file)


def load():
    global students
    Student.count = 0
    Student.total_marks = 0
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
            students = [Student(d["name"], d["section"], d["roll_no"], d["marks"]) for d in data]
    except FileNotFoundError:
        students = []
    except json.JSONDecodeError:
        students = []

running = True

def menu():
    load()
    while running:
        print("Which feature would you like to use?")
        print("1. Add Student\n" \
        "2. View All Students\n" \
        "3. Delete Student\n"
        "4. Edit Student Info\n" \
        "5. Search Student\n" \
        "6. Average Marks\n" \
        "7. Exit")

        choice = input()

        if choice == "1":
            add_student()

        elif choice == "2":
            print(Student.get_count())
            for student in students:
                time.sleep(1)
                print(student)
                time.sleep(0.5)

        elif choice == "7":
            save()
            exit()

        elif choice == "3":
            delete_student()

        elif choice == "4":
            edit()
                
        elif choice == "5":
            search()

        elif choice == "6":
            average()

def add_student():
    name = input("Add Student's Name: ")
    section = input("Enter Section: ")
    roll_no = input("Enter Roll No.: ")
    marks = int(input("Enter marks: "))

    student = Student(name, section, roll_no, marks)
    students.append(student)
    save()
    print("Added successfully")


def delete_student():
    for index, student in enumerate(students, start=1):
        print(f"""
------------------------------------------
{index}. Name : {student.name}
         Section : {student.section}
         Roll No. : {student.roll_no}
         Marks : {student.marks}
-------------------------------------------""")
    
    try:
        choice = int(input("Which would you like to delete? "))
    except ValueError:
        print("Enter Valid Value")
        return

    if 1 <= choice <= len(students):
        removed_student = students.pop(choice - 1)
        print("Deleted Successfully")
        Student.count -= 1
        Student.total_marks -= removed_student.marks
        save()
        time.sleep(1.5)
    else:
        print("Invalid Choice")


def edit():
    user = input("Enter the roll_no of student to edit: ")
    found = False

    for student in students:
        old_marks = student.marks
        if user == student.roll_no:
            found = True
            new_name = input("Enter new name: ")
            new_section = input("Enter new section: ")
            new_roll_no = input("Enter new roll no.: ")
            new_marks = int(input("Enter new marks: "))

            student.name = new_name
            student.section = new_section
            student.roll_no = new_roll_no
            student.marks = new_marks
            Student.total_marks += new_marks - old_marks

            print("Edited Successfully")
            save()
            time.sleep(1)
        
    if not found:
        print("Invalid Input")
        time.sleep(1)


def search():
    found = False
    user = input("Enter roll no. to search: ")

    for student in students:
        if user == student.roll_no:
            print(f"""
------------------------------------
Name : {student.name}
Section : {student.section}
Roll No. : {student.roll_no}
Marks : {student.marks}
------------------------------------""")
            found = True
            time.sleep(1)
    if not found:
        print("Invalid Input")


def average():
    user = input("Enter section you want to find average of: ").upper()
    count = 0
    total = 0
    try:
        for student in students:
            if student.section == user:
                total += student.marks
                count += 1

        average_marks = total/count
        print(f"Average of {user} section is : {average_marks}")
        time.sleep(1)
    except ZeroDivisionError:
        print("This section has no students")

menu()