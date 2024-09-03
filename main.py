from hw_classes.lecturer import Lecturer
from hw_classes.mentor import Mentor
from hw_classes.student import Student

mentor1 = Mentor('Nikolay', 'Vasnecov')
mentor2 = Mentor('Yaroslav', 'Barinov')


lector1 = Lecturer('Iogan', 'Shtraus')
lector2 = Lecturer('Akim', 'Akimov')

student1 = Student('Vasiliy', 'Bobkov', 'M')
student2 = Student('Ekaterina', 'Vlasova', 'W')

print(f'mentor1 - {mentor1}')
print(f'mentor2 - {mentor2}')

print(f'lector1 - {lector1}')
print(f'lector2 - {lector2}')

print(f'student1 - {student1}')
print(f'student2 - {student2}')
