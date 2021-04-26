if __name__ == '__main__':
    studentList = []
    studentIdList = []
    courseList = []
    courseIdList = []
    markList = []

    numberStudent = int(input("Enter number of student: "))
    print("Class has:", numberStudent, "student")


    def input_student(id, name, dob):
        studentList.append((id, name, dob))
        studentIdList.append(id)


    for i in range(numberStudent):
        print("Student number #" + str(i + 1))
        input_student(input("Id: "), input("Name: "), input('Dob: '))

    numberCourse = int(input("Enter course number: "))
    print(f"There are {numberCourse} courses")


    def input_course(id, name):
        courseList.append((id, name))
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

    for student in studentList:
        mark = float(input(f"Enter mark for {student[1]}: "))
        markList.append((student[1], idForSum, mark))

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
            for course in courseList:
                if course[0] == mark[1]:
                    print(mark[0], "-", course[1], "-", mark[2])
