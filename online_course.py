# 5) Онлайн-курс
#
# Классы: Course, Student, EnrollmentSystem.
# Методы: enroll(student, course), is_space_available(course).
# Проверки: вместимость не превышается; нельзя записать дважды.
# Усложнение: пререквизиты: студент должен иметь completed_courses; лист ожидания.

# 5) Онлайн-курс
#
# Сущности: Course, Student, EnrollmentSystem.
#
# Атрибуты:
#
# Course: course_id, title, capacity, enrolled (множество id студентов), prerequisites (набор course_id).
#
# Student: name, email, completed_courses (набор).
#
# EnrollmentSystem: словари курсов и студентов; лист ожидания.
#
# Методы (обязательные):
#
# EnrollmentSystem.add_course(course) / add_student(student).
#
# EnrollmentSystem.enroll(student, course) — с проверками вместимости и пререквизитов.
#
# EnrollmentSystem.drop(student, course) — отписка.
#
# EnrollmentSystem.is_space_available(course) — булево.
#
# EnrollmentSystem.complete(student, course) — перенос в completed_courses.
#
# (Опционально) лист ожидания: join_waitlist/promote_from_waitlist.
#
# Проверки/ошибки: повторная запись; запись без пререквизитов; отписка, если не записан.
#
# Инварианты: 0 ≤ len(enrolled) ≤ capacity.
#
# Усложнения: приоритеты в листе ожидания; ограничения по одновременным курсам.