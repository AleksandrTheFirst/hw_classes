from hw_classes.lecturer import Lecturer
from hw_classes.mentor import Mentor


class Student(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_attached = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer,
                       Lecturer) and course in lecturer.courses_attached and course in self.courses_attached) \
                or (course in self.finished_courses and course in lecturer.courses_attached):
            if course in lecturer.grades.keys():
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'===STUDENT===\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade(self.grades)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses) if self.finished_courses else "нет"}\n'
                f'Курсы в процессе: {", ".join(self.courses_attached) if self.courses_attached else "нет"}')

    def __eq__(self, other):
        if isinstance(other, Student) and self.grades and other.grades:
            self_avg = self.average_grade(self.grades)
            other_avg = other.average_grade(other.grades)
            if self_avg == other_avg:
                return True
            else:
                return False
