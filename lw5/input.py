class Input:
    def input_student(self, id, name, dob):
        studentList.append(Student(id, name, dob))
        studentIdList.append(id)

    def input_course(id, name, credits):
        courseList.append(Course(id, name, credits))
        courseIdList.append(id)

    def get_course_by_id(id):
        for course in courseList:
            if course.get_id() == id:
                return course

