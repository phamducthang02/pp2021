class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_dob(self, dob):
        self.__dob = dob


class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name


class Mark:
    def __init__(self, student, course, mark):
        self.__student = student
        self.__course = course
        self.__mark = mark

    def get_student(self):
        return self.__student

    def get_course(self):
        return self.__course

    def get_mark(self):
        return self.__mark

    def set_student(self, student):
        self.__student = student

    def set_course(self, course):
        self.__course = course

    def set_mark(self, mark):
        self.__mark = mark


if __name__ == '__main__':
    studentList = []
    studentIdList = []
    courseList = []
    courseIdList = []
    markList = []

    numberStudent = int(input("Enter number of student: "))
    print("Class has:", numberStudent, "student")


    def input_student(id, name, dob):
        studentList.append(Student(id, name, dob))
        studentIdList.append(id)


    for i in range(numberStudent):
        print("Student number #" + str(i + 1))
        input_student(input("Id: "), input("Name: "), input('Dob: '))

    numberCourse = int(input("Enter course number: "))
    print(f"There are {numberCourse} courses")


    def input_course(id, name):
        courseList.append(Course(id, name))
        courseIdList.append(id)


    for i in range(numberCourse):
        print("Course number #" + str(i + 1))
        input_course(input("Id: "), input("Name: "))

    idForSum = input("Enter Course Id to input Mark: ")
    while True:
        if idForSum not in courseIdList:
            idForSum = input("Wrong, Enter Again course ID: ")
        else:
            break

    def get_course_by_id(id):
        for course in courseList:
            if course.get_id() == id:
                return course

    for student in studentList:
        markList.append(Mark(student, get_course_by_id(idForSum), float(input(f"Enter mark for {student.get_name()}: "))))

    print("Now you are done with input")
    print("Press 1: Show student list")
    print("Press 2: Show course list")
    print("Press 3: Show Mark")

    choice = int(input("Select: "))
    if choice == 1:
        print(studentList)
    elif choice == 2:
        print(courseList)
    elif choice == 3:
        for mark in markList:
            print(mark.get_student().get_name(), "-", mark.get_course().get_name(), "-", mark.get_mark())
