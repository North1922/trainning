# TODO Класс Course (название, преподаватель, список студентов).
class Course:
    def __init__(self, title, teacher, course_id):
        self.title = title
        self.teacher = teacher
        self.course_id = course_id

        self.list_of_students = dict()

    def __repr__(self):  # Представление объекта. Этот метод вызывается функцией repr() для получения представления объекта в виде строки
        return f'Название курса: {self.title}. Преподаватель: {self.teacher}. Список студентов: {self.list_of_students}'


# TODO Класс Student (имя, email, список курсов).
class Student:
    def __init__(self, name, email, student_id):
        self.name = name
        self.email = email
        self.student_id = student_id

        self.list_of_courses = dict()

    def __repr__(self):  # Представление объекта. Этот метод вызывается функцией repr() для получения представления объекта в виде строки
        return f'Имя студента: {self.name}. E-mail: {self.email}. Id студента: {self.student_id}'


#TODO Класс Teacher (имя, специализация).
# Методы: add_student(), remove_student(), list_students()
class Teacher:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
    @staticmethod
    def add_student(student: Student, course: Course):#метод добавляет студента на курс


    def remove_student(self):#метод удаляет студента с курса
        pass

    def list_students(self, course: Course): #метод показывавет всех студентов с курса
        pass
