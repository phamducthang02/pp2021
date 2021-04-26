class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_credits(self, credits):
        self.__credits = credits