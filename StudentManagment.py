import json

class Student:
    def __init__(self, name, id_number, grade):# ინიციალიზაცია სტუდენტის სახელით, ნომრით და შეფასებით
        self.name = name
        self.id_number = id_number
        self.grade = grade

class StudentList:
    def __init__(self):
        self.students = [] # სტუდენტების სია
        self.load_students()# სტუდენტების ჩატვირთვა

    def load_students(self):#სტუდენტების ჩატვირთვა students.json ფაილიდან
        try:
            with open('students.json', 'r') as f:
                data = json.load(f)
                self.students = [Student(student['name'], student['id_number'], student['grade']) for student in data]
        except FileNotFoundError:
            
            pass

    def save_students(self):#სტუდენტების შენახვა json ფაილში
        with open('students.json', 'w') as f:
            json.dump([student.__dict__ for student in self.students], f)

    def add_student(self, name=None, id_number=None, grade=None):#სტუდენტის დამატება
        if name is None:
           name = input("Enter student name: ")

        if id_number is None:
           id_number = int(input("Enter id number: "))

        if grade is None:
           grade = input("Enter grade: ")

    
        if grade not in ["A", "B", "C", "D", "E", "F"]:#შეფასების ვალიდაცია
           print("Invalid grade. Grade should be one of: A, B, C, D, E, F")
           return

    
        if any(student.id_number == id_number for student in self.students):#სტუდენტის დამატებას id_number ის ვალიდაცია
           print(f"Student with id number {id_number} already exists.")
           return

        self.students.append(Student(name, id_number, grade))#სტუდენტის დამატება სიაში
        self.save_students()#დამატებული სტუდენტის შენახვა
        print("Student added successfully!")

    def view_all_students(self):#ყველა სტუდენტის ნახვა
        for student in self.students:
            print(f"Name: {student.name}, id Number: {student.id_number}, Grade: {student.grade}")

    def search_student(self):#სტუდენტის ძებნა id_number ით
        id_number = int(input("Enter id number to search: "))
        for student in self.students:
            if student.id_number == id_number:
                print(f"Name: {student.name}, id Number: {student.id_number}, Grade: {student.grade}")
                return
        print("Student not found!")

    def update_grade(self, id_number, new_grade):#შეფასების ვალიდაცია
        if new_grade not in ["A", "B", "C", "D", "E", "F"]:
           print("Invalid grade. Grade should be one of: A, B, C, D, E, F")
           return

        found_student = None #სტუდენტის ძებნა id_number ით
        for student in self.students:
           if student.id_number == id_number:
            found_student = student
            break
        if not found_student:
           print(f"No student found with id number {id_number}.")
           return
        found_student.grade = new_grade #შეფასების განახლება
        self.save_students() #განახლებული ინფორმაციის შენახვა
        print("Grade updated successfully.")

def main():
    student_system = StudentList()

    while True:#მენიუს დაბეჭდვა
        print("\nMenu:")
        print("1. Add new student")
        print("2. View all students")
        print("3. Search student by id number")
        print("4. Update student grade")
        print("5. Exit")

        choice = input("Enter your choice: ")
        #მენიუს ღილაკები
        if choice == "1":
            student_system.add_student()
        elif choice == "2":
            print("\nAll Students:")
            for student in student_system.students:
                print(f"Name: {student.name}, id Number: {student.id_number}, Grade: {student.grade}")
        elif choice == "3":
            id_number = int(input("Enter id number to search: "))
            found = False
            for student in student_system.students:
                if student.id_number == id_number:
                    print(f"Name: {student.name}, id Number: {student.id_number}, Grade: {student.grade}")
                    found = True
                    break
            if not found:
                print("Student not found.")
        elif choice == "4":
            id_number = int(input("Enter id number to update grade: "))
            new_grade = input("Enter new grade: ")
            student_system.update_grade(id_number, new_grade)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()