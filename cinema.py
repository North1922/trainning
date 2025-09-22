# 3) Управление кинотеатром
#
# Классы: Movie, Screening (сеанс: зал, время, места), Cinema.
# Методы: schedule(movie, time, capacity), book(screening, seats), cancel(screening, seats).
# Проверки: не бронировать сверх доступных мест; отмена — только ранее забронированных мест.
# Инварианты: 0 ≤ booked ≤ capacity.
# Усложнение: возрастные ограничения (по фильму) и проверка зрителя.


# 3) Кинотеатр
#
# Сущности: Movie, Screening (сеанс), Cinema.
#
# Атрибуты:
#
# Movie: title, rating (возраст), длительность.
#
# Screening: movie, start_time, capacity, booked_seats (набор номеров).
#
# Cinema: расписание (список сеансов).
#
# Методы (обязательные):
#
# Cinema.schedule(movie, start_time, capacity) — добавить сеанс.
#
# Cinema.cancel_screening(screening) — удалить сеанс (если нет брони — легко, если есть — политика).
#
# Screening.book(seat_numbers) — забронировать конкретные места.
#
# Screening.cancel(seat_numbers) — отменить бронь.
#
# Screening.available_seats() — список свободных мест.
#
# Проверки/ошибки: двойное бронирование мест; бронирование несуществующих мест; отмена небронированных.
#
# Инварианты: 0 ≤ len(booked_seats) ≤ capacity.
#
# Усложнения: автоматическая выдача лучших мест; разные залы; скидки на дневные сеансы.