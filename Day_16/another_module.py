from prettytable import PrettyTable

class StudentTable:
    def __init__(self):
        # Initialize an empty list to store student records
        self.students = []

    def add_student(self):
        # Collect input for one student
        name = input("Enter your name: ")
        roll_no = int(input("Enter your roll number: "))
        marks = int(input("Enter your marks: "))
        
        # Store as a dictionary or tuple
        self.students.append({"name": name, "roll_no": roll_no, "marks": marks})

    def display_table(self):
        # Create and populate PrettyTable
        table = PrettyTable()
        table.field_names = ["Name", "Roll Number", "Marks"]

        for s in self.students:
            table.add_row([s["name"], s["roll_no"], s["marks"]])

        print(table)


# Usage
student_table = StudentTable()

# Ask how many students to enter
n = int(input("Enter the number of students: "))
for _ in range(n):
    student_table.add_student()

student_table.display_table()
