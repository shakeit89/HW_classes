class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        #проверяем что лектор - класс лектора, что студент прошел или проходит курс и что лектор читал на данном курсе
        if isinstance(lecturer, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress) and course in lecturer.courses_attached:
            if course in lecturer.grades.keys():
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print(f'Ошибка: студент {self.name} {self.surname} не проходит/проходил данный курс либо лектор не читал лекцию на данном курсе')
        
class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached
        

class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name,surname, courses_attached)
        self.grades = {} 

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print(f'Ошибка, {self.name} {self.surname} не может оценивать работу данного курса или студент не проходит данный курс')

#создадим студентов
stud1 = Student('1', '11', 'm')
stud2 = Student('2', '22', 'm')
stud3 = Student('3', '33', 'm')
stud4 = Student('4', '44', 'f')
stud5 = Student('5', '55', 'f')
stud6 = Student('6', '66', 'f')

stud1.courses_in_progress.extend(['math', 'chemistry'])
stud2.courses_in_progress.extend(['chemistry'])

#создадим лекторов
lect1 = Lecturer('l1', 'l11', ['math', 'english', 'biology'])
lect2 = Lecturer('l2', 'l22', ['math', 'chemistry', 'IT'])

#создадим ревьеворов
rev1 = Reviewer('rev1', 'rev11', ['math', 'english', 'biology', 'chemistry', 'IT'])
rev2 = Reviewer('rev2','rev22', ['english'])


stud1.rate_lecturer(lect1, 'math', 8)
stud2.rate_lecturer(lect1,'chemistry', 9)

rev1.rate_hw(stud1,'math', 6)
rev1.rate_hw(stud1,'math', 8)
rev2.rate_hw(stud1,'math',9)



print(f'{stud1.courses_in_progress=}')
print(f'{lect1.grades=}')
print(f'{stud1.grades=}')