from hw_classes.lecturer import Lecturer
from hw_classes.mentor import Mentor
from hw_classes.student import Student

mentor1 = Mentor('Nikolay', 'Vasnecov')
mentor2 = Mentor('Yaroslav', 'Barinov')


lector1 = Lecturer('Iogan', 'Shtraus')
lector2 = Lecturer('Akim', 'Akimov')

student1 = Student('Vasiliy', 'Bobkov', 'M')
student2 = Student('Ekaterina', 'Vlasova', 'W')

# lector1.grades = {'Python': [2,5,8,10,9]}
# lector2.grades = {'Python': [1,1,1,1,1]}
# print(lector1)
# print(lector2)

student1.grades = {'Python': [2,3,7,10,5,8,8,5]}
student1.courses_in_progress.append('Java')
student1.grades.setdefault('Java', [9,7,8,7,10,10,8,7])

student2.grades = {'Java': [7,7,7,10,10,8,8,9]}
student2.courses_in_progress.append('Java')
student2.grades.setdefault('Java Core', [10,10,10,10,10,10,10,10])

print(student2.avg_all_students([student1, student2], 'Java'))