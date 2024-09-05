class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


    def average_grade(self, grades):
        avg_all = []
        avg = 0
        if len(grades) > 0:
            for grade in grades.values():
                avg = sum(grade)/len(grade)
                avg_all.append(avg)
            avg = sum(avg_all) / len(avg_all)
        return avg

    def __str__(self):
        return (f'===MENTOR===\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')
