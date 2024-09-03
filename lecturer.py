from mentor import Mentor


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.finished_courses = []
        self.courses_in_progress = []

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.avarage_grade(self.grades)}')

    def __eq__(self, other):
        if isinstance(other, Lecturer) and self.grades is not None and other.grades is not None:
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
