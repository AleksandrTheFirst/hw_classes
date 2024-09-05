class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (f'===MENTOR===\n'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

    def average_grade(self, grades):
        avg_all = []
        avg = 0
        if len(grades) > 0:
            for grade in grades.values():
                avg = sum(grade)/len(grade)
                avg_all.append(avg)
            avg = sum(avg_all) / len(avg_all)
        return avg if avg else 0

    def average_for_group(self, objects, course):
        avg_list = [obj.average_grade(obj.grades) for obj in objects if course in obj.courses_attached]
        return sum(avg_list) / len(avg_list) if avg_list else 0
