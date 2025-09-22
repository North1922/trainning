# 8) Турнир
#
# Классы: Player, Match, Tournament.
# Методы: register(player), schedule(), report_result(match, score).
# Проверки: матч можно завершить один раз; оба игрока — зарегистрированы.
# Усложнение: сетка single-elimination; авто-генерация раундов; ничьи/тай-брейки.

# 8) Турнир
#
# Сущности: Player, Match, Tournament.
#
# Атрибуты:
#
# Player: name, rating (опц.).
#
# Match: player1, player2, score, is_finished.
#
# Tournament: список участников, сетка раундов, статус.
#
# Методы (обязательные):
#
# Tournament.register(player) / unregister(player) (пока не начался).
#
# Tournament.start() — сгенерировать пары (single-elimination, бай при нечётном числе).
#
# Tournament.report_result(match, score) — завершить матч, продвинуть победителя.
#
# Tournament.current_round() / is_finished() / winner().
#
# Проверки/ошибки: результат матча можно записать один раз; игрок должен быть зарегистрирован; нельзя начать без ≥ 2 игроков.
#
# Инварианты: игрок участвует только в одном матче на раунд; структура сетки непротиворечива.
#
# Усложнения: тай-брейки; посев по рейтингу; двойное выбывание.