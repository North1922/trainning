# TODO Класс Course (название, преподаватель, список студентов).
class Course:
    def __init__(self, title, course_id):
        self.title = title
        self.course_id = course_id

        self.teacher = None
        self.dict_of_students = dict()

    # def __repr__(self):  # Представление объекта. Этот метод вызывается функцией repr() для получения представления объекта в виде строки
    #     return f'Название курса: {self.title}. Преподаватель: {self.teacher}. Список студентов: {self.list_of_students}'


# TODO Класс Student (имя, email, список курсов).
class Student:
    def __init__(self, name: str, email: str, student_id: int):
        if not isinstance(name, str):
            raise TypeError('name должен быть str')
        self.name = name
        if not isinstance(email,str):
            raise TypeError('email должен быть str')
        self.email = email
        if not isinstance(student_id,int):
            raise TypeError('Id студента должен быть int')
        self.student_id = student_id

        self.list_of_courses = dict()

    # def __repr__(self):  # Представление объекта. Этот метод вызывается функцией repr() для получения представления объекта в виде строки
    #     return f'Имя студента: {self.name}. E-mail: {self.email}. Id студента: {self.student_id}'


# TODO Класс Teacher (имя, специализация).
# Методы: add_student(), remove_student(), list_students()
class Teacher:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    @staticmethod
    def add_student(student: Student, course: Course):  # метод добавляет студента на курс
        if  not isinstance(student, Student) and not isinstance(course, Course):
            raise TypeError('Метод должен принимать два объекта типа Student и Course')
        if student.student_id in course.dict_of_students:
            print('Студент уже находится в списке учеников')
        else:
            course.dict_of_students[student.student_id] = student
            print(f'Студент {student.name} посутпил на курс {course.title} ')

    @staticmethod
    def remove_student(student: Student, course: Course):  # метод удаляет студента с курса
        if  not isinstance(student, Student) and not isinstance(course, Course):
            raise TypeError('Метод должен принимать два объекта типа Student и Course')
        if student.student_id not in course.dict_of_students:
            print('Студент не числится в списке учеников')
        else:
            del course.dict_of_students[student.student_id]

    @staticmethod
    def list_students(course: Course):  # метод показывавет всех студентов с курса
        if not course.dict_of_students:
            print('На курсе нет студентов')
        for key, val in course.dict_of_students.items():
            print(f'Имя студента: {val.name}. Id: {val.student_id}')



st = Student('alex', 'asda@fdsdf.com', 14)
ts = Student('max', 'asdamxmasxa@fdsdf.com', 88)
tc = Teacher('name', 'Python')
co = Course('road to pro', 88)
tc.add_student(st, co)
tc.add_student(ts, co)
tc.list_students(co)
