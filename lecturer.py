from mentor import Mentor


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.finished_courses = []

    def __str__(self):
        return ('===LECTURER===\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade(self.grades)}\n')

    def __eq__(self, other):
        if isinstance(other, Lecturer) and self.grades and other.grades:
            self_avg = self.average_grade(self.grades)
            other_avg = other.average_grade(other.grades)
            if self_avg == other_avg:
                return True
            else:
                return False
