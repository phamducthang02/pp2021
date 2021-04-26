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