studentList = []
studentIdList = []
courseList = []
courseIdList = []
markList = []
courseMarkList = []

scr = curses.initscr()

scr.addstr("Enter number of student: ")
numberStudent = int(scr.getstr().decode())
scr.addstr(f"Class has: {numberStudent} students")
scr.clear()

for i in range(numberStudent):
    scr.addstr("Student number #" + str(i + 1))
    scr.addstr("\nId: ")
    id = scr.getstr().decode()
    scr.addstr("Name: ")
    name = scr.getstr().decode()
    scr.addstr("Dob: ")
    dob = scr.getstr().decode()
    scr.addstr("\n")
    input_student(id, name, dob)
    f = open('students.txt', 'w')
    f.write(id)
    f.write(name)
    f.write(dob)
    f.close()
scr.clear()

scr.addstr("Enter course number: ")
numberCourse = int(scr.getstr().decode())
scr.addstr(f"There are {numberCourse} courses")
scr.clear()

for i in range(numberCourse):
    scr.addstr("Course number #" + str(i + 1))
    scr.addstr("\nId: ")
    id = scr.getstr().decode()
    scr.addstr("Name: ")
    name = scr.getstr().decode()
    scr.addstr("Credits: ")
    credits = int(scr.getstr().decode())
    scr.addstr("\n")
    input_course(id, name, credits)
    f = open('courses.txt', 'w')
    f.write(id)
    f.write(name)
    f.write(credits)
    f.close()
scr.clear()

while len(markList) < len(studentList) * len(courseList):
    scr.addstr("Courses that have not inputted marks: \n")
    for course in courseList:
        if course.get_id() not in courseMarkList:
            scr.addstr(course.get_name() + "\n")
    scr.addstr("\nEnter Course Id to input Mark: ")
    idForSum = scr.getstr().decode()
    while True:
        if idForSum not in courseIdList:
            scr.clear()
            scr.addstr("Wrong, enter again course ID: ")
            idForSum = scr.getstr().decode()
        if idForSum in courseMarkList:
            scr.clear()
            scr.addstr("Course mark already inputted, enter again course ID: ")
            idForSum = scr.getstr().decode()
        else:
            scr.clear()
            break

    for student in studentList:
        scr.addstr(f"Enter mark for {student.get_name()}: ")
        markList.append(
            Mark(student, get_course_by_id(idForSum), math.floor((float(scr.getstr().decode())) * 10) / 10.0))
        courseMarkList.append(idForSum)
        f = open("marks.txt", "w")
        f.write(markList)
        f.close()
        scr.clear()

    while True:
        scr.clear()
        scr.addstr("Now you are done with input")
        scr.addstr("\nPress 1: Show student list")
        scr.addstr("\nPress 2: Show course list")
        scr.addstr("\nPress 3: Show Mark")
        scr.addstr("\nPress 4: Calculate GPA for a student")
        scr.addstr("\nPress 5: Exit")

        scr.addstr("\nSelect: ")
        choice = int(scr.getstr().decode())
        if choice == 1:
            scr.clear()
            for student in studentList:
                scr.addstr(student.get_id(), student.get_name(), "\n")
            curses.napms(1000 * numberStudent)
        elif choice == 2:
            scr.clear()
            for course in courseList:
                scr.addstr(course.get_id(), course.get_name(), "\n")
            curses.napms(1000 * numberCourse)
        elif choice == 3:
            scr.clear()
            for mark in markList:
                scr.addstr(f"{mark.get_student().get_name()} - {mark.get_course().get_name()} - {mark.get_mark()}\n")
            curses.napms(1000 * len(markList))
        elif choice == 4:
            scr.clear()
            scr.addstr("Enter student id to calculate GPA: ")
            student_id = scr.getstr().decode()
            if student_id not in studentIdList:
                scr.clear()
                scr.addstr("\nStudent does not exist")
            else:
                scr.clear()
                for student in studentList:
                    if student.get_id() == student_id:
                        scr.addstr(f"\nGPA of {student.get_name()}:", calculate_gpa(student_id))
                curses.napms(1000)
        elif choice == 5:
            exit()
        else:
            scr.clear()
            scr.addstr("Wrong choice. Choose again: ")