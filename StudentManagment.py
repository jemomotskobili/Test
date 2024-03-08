import json

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class StudentList:
    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        try:
            with open('students.json', 'r') as f:
                data = json.load(f)
                self.students = [Student(student['name'], student['roll_number'], student['grade']) for student in data]
        except FileNotFoundError:
            
            pass

    def save_students(self):
        with open('students.json', 'w') as f:
            json.dump([student.__dict__ for student in self.students], f)

    def add_student(self, name=None, roll_number=None, grade=None):
        if name is None:
           name = input("Enter student name: ")

        if roll_number is None:
           roll_number = int(input("Enter roll number: "))

        if grade is None:
           grade = input("Enter grade: ")

    
        if grade not in ["A", "B", "C", "D", "E", "F"]:
           print("Invalid grade. Grade should be one of: A, B, C, D, E, F")
           return

    
        if any(student.roll_number == roll_number for student in self.students):
           print(f"Student with roll number {roll_number} already exists.")
           return

        self.students.append(Student(name, roll_number, grade))
        self.save_students()
        print("Student added successfully!")

    def view_all_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")

    def search_student(self):
        roll_number = int(input("Enter roll number to search: "))
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")
                return
        print("Student not found!")

    def update_grade(self, roll_number, new_grade):
        if new_grade not in ["A", "B", "C", "D", "E", "F"]:
           print("Invalid grade. Grade should be one of: A, B, C, D, E, F")
           return

        found_student = None
        for student in self.students:
           if student.roll_number == roll_number:
            found_student = student
            break
        if not found_student:
           print(f"No student found with roll number {roll_number}.")
           return
        found_student.grade = new_grade
        self.save_students()
        print("Grade updated successfully.")

def main():
    student_system = StudentList()

    while True:
        print("\nMenu:")
        print("1. Add new student")
        print("2. View all students")
        print("3. Search student by roll number")
        print("4. Update student grade")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_system.add_student()
        elif choice == "2":
            print("\nAll Students:")
            for student in student_system.students:
                print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")
        elif choice == "3":
            roll_number = int(input("Enter roll number to search: "))
            found = False
            for student in student_system.students:
                if student.roll_number == roll_number:
                    print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")
                    found = True
                    break
            if not found:
                print("Student not found.")
        elif choice == "4":
            roll_number = int(input("Enter roll number to update grade: "))
            new_grade = input("Enter new grade: ")
            student_system.update_grade(roll_number, new_grade)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()