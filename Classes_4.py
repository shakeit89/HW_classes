class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя студента: {self.name}\n' \
            f'Фамилия студента: {self.surname} \n'\
            f'Средняя оценка за домашние задания: {self.mean_grade()} \n'\
            f'Курсы в процессе изучения: {", ".join(map(str, self.courses_in_progress))} \n'\
            f'Завершенные курсы: {", ".join(map(str, self.finished_courses))} \n'

    def __gt__(self, another_student):
        if isinstance(another_student, Student):
            if self.mean_grade() != 'нет оценок' and another_student.mean_grade() != 'нет оценок':
                return self.mean_grade() > another_student.mean_grade()
            else: return 'Ошибка! У одного из студентов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть студентами!'

    def __lt__(self, another_student):
        if isinstance(another_student, Student):
            if self.mean_grade() != 'нет оценок' and another_student.mean_grade() != 'нет оценок':
                return self.mean_grade() < another_student.mean_grade()
            else: return 'Ошибка! У одного из студентов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть студентами!'

    def __ge__(self, another_student):
        if isinstance(another_student, Student):
            if self.mean_grade() != 'нет оценок' and another_student.mean_grade() != 'нет оценок':
                return self.mean_grade() >= another_student.mean_grade()
            else: return 'Ошибка! У одного из студентов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть студентами!'

    def __le__(self, another_student):
        if isinstance(another_student, Student):
            if self.mean_grade() != 'нет оценок' and another_student.mean_grade() != 'нет оценок':
                return self.mean_grade() <= another_student.mean_grade()
            else: return 'Ошибка! У одного из студентов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть студентами!'

    def __eq__(self, another_student):
        if isinstance(another_student, Student):
            if self.mean_grade() != 'нет оценок' and another_student.mean_grade() != 'нет оценок':
                return self.mean_grade() == another_student.mean_grade()
            else: return 'Ошибка! У одного из студентов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть студентами!'

    def __ne__(self, another_student):
        if isinstance(another_student, Student):
            if self.mean_grade() != 'нет оценок' and another_student.mean_grade() != 'нет оценок':
                return self.mean_grade() != another_student.mean_grade()
            else: return 'Ошибка! У одного из студентов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть студентами!'

    def mean_grade(self):
        count = 0
        sum_of_grades = 0
        for grade_list in self.grades.values():
            count += len(grade_list)
            sum_of_grades += sum(grade_list)
        if count:
            return sum_of_grades / count
        else:
             return 'нет оценок'


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

    def __str__(self):
        return f'Имя лектора: {self.name}\n' \
            f'Фамилия лектора: {self.surname} \n'\
            f'Средняя оценка за лекции: {self.mean_grade()} \n'\

    def mean_grade(self):
        count = 0
        sum_of_grades = 0
        for grade_list in self.grades.values():
            count += len(grade_list)
            sum_of_grades += sum(grade_list)
        if count:
            return sum_of_grades / count
        else:
            return 'нет оценок'
    
    def __gt__(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            if self.mean_grade() != 'нет оценок' and another_lecturer.mean_grade() != 'нет оценок':
                return self.mean_grade() > another_lecturer.mean_grade()
            else: return 'Ошибка! У одного из лекторов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть лекторами!'

    def __lt__(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            if self.mean_grade() != 'нет оценок' and another_lecturer.mean_grade() != 'нет оценок':
                return self.mean_grade() < another_lecturer.mean_grade()
            else: return 'Ошибка! У одного из лекторов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть лекторами!'

    def __ge__(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            if self.mean_grade() != 'нет оценок' and another_lecturer.mean_grade() != 'нет оценок':
                return self.mean_grade() >= another_lecturer.mean_grade()
            else: return 'Ошибка! У одного из лекторов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть лекторами!'

    def __le__(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            if self.mean_grade() != 'нет оценок' and another_lecturer.mean_grade() != 'нет оценок':
                return self.mean_grade() <= another_lecturer.mean_grade()
            else: return 'Ошибка! У одного из лекторов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть лекторами!'

    def __eq__(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            if self.mean_grade() != 'нет оценок' and another_lecturer.mean_grade() != 'нет оценок':
                return self.mean_grade() == another_lecturer.mean_grade()
            else: return 'Ошибка! У одного из лекторов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть лекторами!'

    def __ne__(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            if self.mean_grade() != 'нет оценок' and another_lecturer.mean_grade() != 'нет оценок':
                return self.mean_grade() != another_lecturer.mean_grade()
            else: return 'Ошибка! У одного из лекторов нет оценок!'
        else:
            return f'Ошибка! При сравнении оценок оба должны быть лекторами!'

class Reviewer(Mentor):
    def __str__(self):
        return f'Имя ревьювера: {self.name}\n'\
            f'Фамилия ревьювера: {self.surname}\n'


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print(f'Ошибка, {self.name} {self.surname} не может оценивать работу данного курса или студент не проходит данный курс')

def mean_grade_course_students(list_of_students, course):
    count = 0
    sum_of_grades = 0
    for student in list_of_students:
        count += 1
        sum_of_grades += student.mean_grade()
    return sum_of_grades / count

def mean_grade_course(list_of_lecturers, course):
    count = 0
    sum_of_grades = 0
    for lecturer in list_of_lecturers:
        if course not in lecturer.grades.keys():
            continue
        count += len(lecturer.grades[course])
        sum_of_grades += sum(lecturer.grades[course])
    return sum_of_grades / count

#создадим студентов
stud1 = Student('Vasya', 'Vasin', 'm')
stud2 = Student('Kolya', 'Kolin', 'm')

#определим курсы, которые проходят студенты
stud1.courses_in_progress += ['math', 'chemistry', 'biology']
stud2.courses_in_progress += ['chemistry', 'IT','math']

#определим завершенные курсы
stud1.finished_courses += ['english']
stud2.finished_courses += ['english']

#создадим лекторов
lect1 = Lecturer('Oleg', 'Olegov', ['math', 'english', 'biology'])
lect2 = Lecturer('Ivan', 'Ivanov', ['math', 'chemistry', 'IT'])

#создадим ревьеверов
rev1 = Reviewer('Petr', 'Petrov', ['math', 'english', 'biology', 'chemistry', 'IT'])
rev2 = Reviewer('Pavel','Pavlov', ['english', 'IT'])


#Поставим оценки лекторам
print('Поставим оценки лекторам')
stud1.rate_lecturer(lect1, 'math', 8)
stud1.rate_lecturer(lect1, 'math', 7)
stud2.rate_lecturer(lect2, 'chemistry', 4)
stud2.rate_lecturer(lect1, 'math', 10)

#Поставим оценки студентам
print('Поставим оценки студентам')
rev1.rate_hw(stud1, 'math', 5)
rev1.rate_hw(stud1, 'math', 8)
rev1.rate_hw(stud1, 'math', 9)
rev1.rate_hw(stud1, 'math', 10)
rev1.rate_hw(stud2, 'math', 7)
rev1.rate_hw(stud2, 'chemistry', 7)
rev1.rate_hw(stud2, 'math', 7)
rev1.rate_hw(stud2, 'math', 7)
rev1.rate_hw(stud1, 'IT', 5)



#применим методы __str__
print('применим методы __str__')
print(stud1)
print(stud2)
print(lect1)
print(lect2)
print(rev1)


#Посчет средних за курсы какм студентам, так и лекторам (применили 1 универсальную функцию вместо 2х)
print('Посчет средних за курсы по математике среди студентов:')
print(mean_grade_course([stud1, stud2], 'math'))
print('Посчет средних за курсы по математике среди лекторов:')
print(mean_grade_course([lect1, lect2], 'math'))

#сравнение оценок у студентов и лекторов
print('Сравнение оценок:')
print(stud1 > stud2)
print(stud1 != stud2)
print(stud1 <= stud2)
print(lect1 > lect2)
print(lect1 != lect2)
print(lect1 <= lect2)