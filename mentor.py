class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


    def avarage_grade(self, grades):
        avg = 0
        for grade in grades.values():
            summary = sum(grade)
            avg = summary/len(grade)
        return avg