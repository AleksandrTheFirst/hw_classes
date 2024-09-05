from hw_classes.mentor import Mentor
from hw_classes.student import Student


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            raise ValueError('Некорректный объект студента')
        if course not in self.courses_attached or course not in student.courses_attached:
            raise ValueError('Курс не прикреплен к проверяющему или студенту')
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n'
