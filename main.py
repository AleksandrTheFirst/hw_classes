from hw_classes.lecturer import Lecturer
from hw_classes.mentor import Mentor
from hw_classes.student import Student

mentor1 = Mentor('Nikolay', 'Vasnecov')
mentor2 = Mentor('Yaroslav', 'Barinov')

print(mentor1)
print(mentor2)

lecturer1 = Lecturer('Iogan', 'Shtraus')
lecturer2 = Lecturer('Akim', 'Akimov')

student1 = Student('Vasiliy', 'Bobkov', 'M')
student2 = Student('Ekaterina', 'Vlasova', 'W')

lecturer1.grades.setdefault('Python', [2, 5, 8, 10, 9])
lecturer1.grades.setdefault('Java', [5, 6, 8, 10, 10])
lecturer1.courses_attached.append('Python')
lecturer1.courses_attached.append('Java')

lecturer2.grades.setdefault('Python', [1, 1, 1, 1, 1])
lecturer2.grades.setdefault('Java', [8, 8, 8, 9, 9])
lecturer2.courses_attached.append('Java')

print(lecturer1)
print(lecturer2)

student1.grades = {'Python': [2,3,7,10,5,8,8,5]}
student1.courses_in_progress.append('Java')
student1.courses_in_progress.append('Python')
student1.grades.setdefault('Java', [9,7,8,7,10,10,8,7])

student2.grades = {'Java': [7,7,7,10,10,8,8,9]}
student2.courses_in_progress.append('Java')
student2.grades.setdefault('Java Core', [10,10,10,10,10,10,10,10])

print(student1)
print(student2)

print(f'Средняя оценка студента по курсу "Java": {student2.avg_all_students([student1, student2], 'Java')}')

print(f'Средняя оценка лектора по курсу "Python": {lecturer1.avg_all_lecturers([lecturer1, lecturer2], 'Python')}')
