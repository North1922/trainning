# 4) Каршеринг
#
# Классы: Car (база), ElectricCar, HybridCar, RentalService.
# Методы: rent(car, user), return(car, km).
# Проверки: нельзя сдавать несданную машину; при возврате обновлять ресурс (battery%/fuel).
# Инварианты: ресурсы в диапазоне; тарифы корректны.
# Усложнение: разные тарифы по типу, депозит, штраф за низкий заряд.

# 4) Каршеринг
#
# Сущности: Car (абстрактный), ElectricCar, HybridCar, User, RentalService, PricingPolicy.
#
# Атрибуты:
#
# Car: car_id, odometer_km, is_available, location.
#
# ElectricCar: battery_percent (0–100), consumption_kWh_per_100km.
#
# HybridCar: fuel_liters, battery_percent.
#
# User: name, driver_license_id, статус верификации.
#
# RentalService: парк машин, активные аренды, ценовая политика.
#
# PricingPolicy: параметры тарифа (цена/мин, цена/км, доп. сборы).
#
# Методы (обязательные):
#
# RentalService.register_user(user) — верифицировать.
#
# RentalService.rent(car, user) — начать аренду (помечает is_available=False, фиксирует start_time, start_odometer).
#
# RentalService.return_car(car, end_km) — завершить, обновить пробег, рассчитать стоимость, пометить is_available=True.
#
# ElectricCar.drive(distance_km) — уменьшить battery_percent по расходу, увеличить odometer_km, запретить, если батареи не хватает.
#
# ElectricCar.charge(percent) — увеличить заряд (ограничить 100).
#
# (Аналогично для HybridCar: refuel(liters), расход топлива/батареи.)
#
# PricingPolicy.calculate(start_time, end_time, km_delta, car) — расчёт цены.
#
# Проверки/ошибки:
#
# Неверифицированный пользователь не может арендовать.
#
# Машина уже в аренде/недоступна.
#
# return_car без активной аренды.
#
# drive при нулевом ресурсе; заряд/топливо вне диапазона; отрицательный end_km.
#
# Инварианты: 0 ≤ battery_percent ≤ 100; odometer_km не убывает; «в аренде» ↔ is_available=False.
#
# Усложнения: депозит; штраф за низкий заряд при возврате; бронирование по локации; разные тарифы для типов авто.