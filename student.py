from hw_classes.lecturer import Lecturer


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress)\
                or (course in self.finished_courses and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.avarage_grade(self.grades)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}\n')

    def __eq__(self, other):
        if isinstance(other, Student) and self.grades is not None and other.grades is not None:
            self_avg = self.avarage_grade(self.grades)
            other_avg = other.avarage_grade(other.grades)
            if self_avg == other_avg:
                return True
            else:
                return False

    def avarage_grade(self, grades):
        for grade in grades.values():
            summary = sum(grade)
            avg = summary/len(grade)
        return avg
