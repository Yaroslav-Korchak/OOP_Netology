class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_hw_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return total_grades / total_courses if total_courses > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.avg_hw_grade() < other.avg_hw_grade()

    def __str__(self):
        avg_grade = self.avg_hw_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: "
                f"{avg_grade}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: "
                f"{finished_courses_str}")

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Оценка должна быть в диапазоне от 0 до 10'
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_lecture_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())  # суммируем все оценки за лекции
        total_courses = len(self.grades.values())  # определяем общее количество курсов
        return total_grades / total_courses if total_courses > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_lecture_grade() < other.avg_lecture_grade()

    def __str__(self):
        avg_grade = self.avg_lecture_grade()
        return (f"Имя: {self.name}\nФамилия: {self.surname}" + f"\nСредняя оценка за лекции: {avg_grade}")


class Reviewer(Mentor):


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 <= grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Оценка должна быть в диапазоне от 0 до 10'
        else:
            return 'Ошибка'


    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}")


best_student1 = Student('Ruoy', 'Eman', 'male')
best_student1.courses_in_progress += ['Python', 'Git']

best_student2 = Student('Vasya', 'Ivanov', 'male')
best_student2.courses_in_progress += ['Python', 'Git']


cool_lecturer1 = Lecturer('Some', 'Buddy')
cool_lecturer1.courses_attached += ['Python', 'Git']
cool_lecturer2 = Lecturer('Another', 'Buddy2')
cool_lecturer2.courses_attached += ['Python', 'Git']


cool_reviewer1 = Reviewer('Best', 'Reviewer')
cool_reviewer1.courses_attached += ['Python', 'Git']
cool_reviewer2 = Reviewer('Best2', 'Reviewer2')
cool_reviewer2.courses_attached += ['Python', 'Git']

cool_reviewer1.rate_hw(best_student1, 'Python', 10)
cool_reviewer2.rate_hw(best_student1, 'Git', 10)
cool_reviewer1.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student2, 'Git', 10)

best_student1.rate_lecture(cool_lecturer1, 'Python', 8)
best_student1.rate_lecture(cool_lecturer1, 'Git', 8)
best_student2.rate_lecture(cool_lecturer2, 'Python', 8)
best_student2.rate_lecture(cool_lecturer2, 'Git', 10)

best_student1.finished_courses.append('Введение в программирование')
best_student2.finished_courses.append('Введение в программирование')

#Сравнение средней оценки студентов:


if best_student1 > best_student2:
    print(f'Средняя оценка {best_student1.name} {best_student1.surname} лучше чем у {best_student2.name} {best_student2.surname}')
else:
    print(f'Средняя оценка {best_student1.name} {best_student1.surname} хуже чем у {best_student2.name} {best_student2.surname}')

#Сравнение средней оценки лекторов
if cool_lecturer1 > cool_lecturer2:
    print(f'Средняя оценка {cool_lecturer1.name} {cool_lecturer1.surname} лучше чем у {cool_lecturer2.name} {cool_lecturer2.surname}')
else:
    print(f'Средняя оценка {cool_lecturer1.name} {cool_lecturer1.surname} хуже чем у {cool_lecturer2.name} {cool_lecturer2.surname}')


#Подсчет средней оценки студентов по курсу
def avg_students_grade(students_list, course_name):
        total_grade = 0
        count = 0
        for student in students_list:
            if course_name in student.grades:
                total_grade += sum(student.grades[course_name])
                count += len(student.grades[course_name])
        return round(total_grade / count, 1) if count > 0 else 0

#Подсчет средней оценки лекторов по курсу
def avgerage_lectors_grade(lectors_list, course_name):
        total_grade = 0
        count = 0
        for lecturer in lectors_list:
            if course_name in lecturer.grades:
                total_grade += sum(lecturer.grades[course_name])
                count += len(lecturer.grades[course_name])
        return round(total_grade / count, 1) if count > 0 else 0


students = [best_student1, best_student2]
lectors = [cool_lecturer1, cool_lecturer2]


# print(cool_lecturer2.grades)
# print(best_student2.__str__())
# print(cool_lecturer2.__str__())
print(f'Студенты:\n{best_student1}\n{best_student2}')
print(f'Лекторы:\n{cool_lecturer1}\n\n{cool_lecturer2}\n')
print(f'Ревьюеры:\n{cool_reviewer1}\n\n{cool_reviewer2}\n')
print(f'Средняя оценка лекторов по курсу Git: {avgerage_lectors_grade(lectors, 'Git')}')
print(f'Средняя оценка студентов по курсу Python: {avg_students_grade(students, 'Python')}')
