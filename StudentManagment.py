import json

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"

class StudentList:
    def __init__(self, filename='studentlist.json'):
        self.students = []
        self.filename=filename
        self.view_all_students()

    def add_student(self, student):
        self.students.append(student)
        self.save_students

    def view_all_students(self):
        for student in self.students:
            print(student)

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None
        
    
    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump([student.__dict__ for student in self.students], f)

    def load_students(self):
        try:
            with open(self.filename, 'r') as f:
                students_data = json.load(f)
                for student_data in students_data:
                    self.students.append(Student(**student_data))
        except FileNotFoundError:
            self.students = []       

    def update_grade(self, roll_number, new_grade):
        student = self.search_student(roll_number)
        if student:
            student.grade = new_grade
            return True
        return False

def main():
    manager = StudentList()

    while True:
        print("\nStudent Management System")
        print("1. Add a new student")
        print("2. Show all students")
        print("3. Search for a student by roll number")
        print("4. Update student grade")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_number = int(input("Enter roll number: "))
            grade = input("Enter grade: ")

            if not name or not roll_number or not grade.isdigit():
                print("Invalid input. Please try again.")
                continue

            student = Student(name, int(roll_number), int(grade))
            manager.add_student(student)
            print("Student added successfully.")
            

        elif choice == "2":
            print("\nList of all students:")
            manager.view_all_students()

        elif choice == "3":
            roll_number = int(input("Enter roll number to search: "))
            found_student = manager.search_student(roll_number)
            if found_student:
                print("\nStudent found:")
                print(student)
                
            else:
                print("Student not found.")

        elif choice == "4":
            roll_number = int(input("Enter roll number to update grade: "))
            new_grade = input("Enter new grade: ")
            if manager.update_grade(roll_number, new_grade):
                print("Grade updated successfully.")
            else:
                print("Student not found.")

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()