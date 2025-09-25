DEFAULT_NOTE = "Student Management System - Main branch update"


class Student:
    def __init__(self, name, roll_no, student_class):
        self.name = name
        self.roll_no = roll_no
        self.student_class = student_class

    def display(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Class: {self.student_class}"

if __name__ == "__main__":
    print(DEFAULT_NOTE)
    s1 = Student("Alice", 1, "CSE")
    print(s1.display())
