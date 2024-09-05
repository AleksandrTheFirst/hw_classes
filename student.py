from hw_classes.lecturer import Lecturer
from hw_classes.mentor import Mentor


class Student(Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer,
                       Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress) \
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
                f'Завершенные курсы: {', '.join(self.finished_courses)}\n')

    def __eq__(self, other):
        if isinstance(other, Student) and self.grades is not None and other.grades is not None:
            self_avg = self.average_grade(self.grades)
            other_avg = other.average_grade(other.grades)
            if self_avg == other_avg:
                return True
            else:
                return False

    def avg_all_students(self, students, course):
        avg = []
        avg_all = 0
        if course in self.courses_in_progress and course in self.grades and students is not None:
            for student in students:
                avg.append(student.average_grade(student.grades))
            avg_all = sum(avg) / len(avg)
        return avg_all