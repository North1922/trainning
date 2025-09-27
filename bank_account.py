# 🔹 Задание 1. Банковские счета
#
# Сделай систему для работы с разными типами банковских счетов.
#
#TODO Базовый класс BankAccount с атрибутами owner, balance, методами deposit(amount), withdraw(amount).
#
#TODO Класс SavingsAccount (сберегательный), у которого есть процентная ставка и метод add_interest().
#
#TODO Класс CheckingAccount (расчётный), у которого есть лимит на снятие за день.
#
#TODO Подумай, где использовать наследование, а где — композицию (например, история транзакций
from datetime import datetime, date
from decimal import Decimal, ROUND_HALF_UP

class AccountError(Exception):
    pass

class InvalidAmount(AccountError):
    """Сумма операции некорректна (<= 0 или невалидна)."""

class LimitExceeded(AccountError):
    """Превышен суточный лимит снятий."""

class InsufficientFunds(AccountError):
    """Недостаточно средств/запрещённый уход ниже минимума."""


class BankAccount:
    def __init__(self, owner: str, balance: Decimal = Decimal('0.00'), currency='RUB'):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def deposit(self, amount: Decimal):
        if not isinstance(amount, Decimal):
            raise AccountError('В качестве суммы необходимо передавать тип Decimal')
        if amount <= 0:
            raise InvalidAmount('Сумма должна быть > 0')
        amount = type(self).quantize_money(amount)
        self.balance = type(self).quantize_money(self.balance + amount)


    def withdraw(self, amount: Decimal, *, now: datetime | None = None):
        pass

    def get_balance(self):
        return self.balance

    def _validate_withdraw(self, amount, now):
        # В первый вызов validate_withdraw(now)
        # если window_date is None — просто устанавливаю window_date = локальная_дата(now) и withdrawn_today = 0.00(без сравнения);
        # дальше работаю
        pass

    @staticmethod
    def quantize_money(x: Decimal) -> Decimal:
        return x.quantize(Decimal('1.00'), ROUND_HALF_UP)


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance: Decimal = Decimal('0.00'), currency='RUB',
                 daily_withdraw_limit: Decimal | None = None):
        super().__init__(owner, balance, currency)
        self.daily_withdraw_limit = daily_withdraw_limit
        self.withdrawn_today: Decimal = Decimal('0.00')
        self.window_date: date | None = None
        self.tz_info = 'UTC+3'
        self.allow_overdraft = True

    def _reset_window_if_need(self, now):
        pass

    def _validate_withdraw(self, amount, now):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance: Decimal = Decimal('0.00'), currency='RUB',
                 annual_rate: Decimal = Decimal(0.00)):
        super().__init__(owner, balance, currency)
        self.annual_rate = annual_rate
        self.last_accrual_date: date | None = None #для этого поля достаточно будет date а не datetime

    def accure_monthly_interest(self, now: date):
        pass