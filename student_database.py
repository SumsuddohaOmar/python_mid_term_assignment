class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, new_student):
        cls.student_list.append(new_student)


class Student:
    def __init__(self, name, department, is_enrolled=False):
        self.__student_id = len(StudentDatabase.student_list) + 1
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def view_student_info(self):
        print(f"Student ID : {self.__student_id}")
        print(f"Name : {self.__name}")
        print(f"Department : {self.__department}")
        print(f"Enrollment Status : {self.__is_enrolled}\n")

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print("Succesfully Enrolled.\n")
        else:
            print("Already Enrolled.\n")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"{self.__name} dropped out.\n")
        else:
            print("Not Enrolled.\n")

    @classmethod
    def search_student(cls, ID):
        for student in StudentDatabase.student_list:
            if student.__student_id == ID:
                return student
        return None


s1 = Student("Ali", "CSE")
s2 = Student("Sara", "EEE")
s3 = Student("Omar", "BBA")

while True:
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    option = input("Enter Option: ")

    if option == "1":
        for student in StudentDatabase.student_list:
            student.view_student_info()
    elif option == "2":
        ID = int(input("Enter your Student ID: "))
        student = Student.search_student(ID)
        if student is None:
            print("Invalid Student ID.")
        else:
            student.enroll_student()
    elif option == "3":
        ID = int(input("Enter your Student ID: "))
        student = Student.search_student(ID)
        if student is None:
            print("Invalid Student ID.")
        else:
            student.drop_student()
    elif option == "4":
        break
    else:
        print("Invalid Option, Please Enter Again.")
