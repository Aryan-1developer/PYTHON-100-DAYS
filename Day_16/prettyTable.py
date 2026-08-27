from prettytable import PrettyTable 

"""class StudentTable:
   
    def __init__(self):
        no_of_input = int(input("Enter the number of students: "))
        self.name = input("enter your name:")
        self.roll_no = int(input("enter your roll number:"))
        self.marks = int(input("enter your marks:"))

    def display_table(self):
        student = []
        for _ in range(self.no_of_input):
            student.append(StudentTable())

        table = PrettyTable()
        table.field_names = ["Name", "Roll Number", "Marks"]

        for s in student:
            table.add_row([s.name, s.roll_no, s.marks])

        print(table)

student_table = StudentTable()
student_table.display_table()"""


class StudentTable:

    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter your name: ")
        roll_no = int(input("Enter your roll number: "))
        marks = int(input("Enter your marks: "))


        self.students.append({"name": name, "roll_no": roll_no, "marks": marks})

    def display_table(self):
        table = PrettyTable()
        table.field_names = ["Name", "Roll Number ", "Marks"]

        for s in self.students:
            table.add_row([s.name, s.roll_no, s.marks])

        print(table)

student_table = StudentTable()


no_of_input = int(input("Enter the number of students: "))

student_table.add_student()

for _ in range(no_of_input):
    student_table.add_student()

student_table.display_table()



