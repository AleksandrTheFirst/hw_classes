from mentor import Mentor


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.finished_courses = []
        self.courses_in_progress = []

    def __str__(self):
        return f'Имя: {self.name}''\n' f'Фамилия: {self.surname}''\n' f'Средняя оценка за лекции: '
