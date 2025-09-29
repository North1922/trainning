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
from datetime import datetime, date, timezone, timedelta
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
        self.owner = owner # имя пользователя
        self.balance = type(self).quantize_money(balance) # баланс счёта
        self.currency = currency # баланс счёта
        self.tz_info = timezone(timedelta(hours=3), name="UTC+3")

    def deposit(self, amount: Decimal): # функция внесения денег на счёт, в качестве аргументов необходимо передавать Decimal
        if not isinstance(amount, Decimal):
            raise AccountError('В качестве суммы необходимо передавать тип Decimal')
        if amount <= 0:
            raise InvalidAmount('Сумма должна быть > 0')
        amount = type(self).quantize_money(amount) # квантизируем сумму на входе
        self.balance = type(self).quantize_money(self.balance + amount) # так же перед дувеличением баланса квантизируем


    def withdraw(self, amount: Decimal, *, now: datetime | None = None):
        if not isinstance(amount, Decimal):
            raise AccountError('В качестве суммы необходимо передавать тип Decimal')
        if amount <= 0:
            raise InvalidAmount('Сумма должна быть > 0')
        self._validate_withdraw(amount, now)
        amount_quantize = type(self).quantize_money(amount) #amount привели к нужному денежному формату 2 знака после точки и округлили ROUND_HALF_UP
        self.balance = type(self).quantize_money(self.balance - amount_quantize) #изменяем баланс за вычетом суммы которую сняли со счёта



    def get_balance(self):
        return self.balance

    def _validate_withdraw(self, amount: Decimal, now: datetime | None):
        amount_q = type(self).quantize_money(amount)
        if self.balance < amount_q:
            raise InsufficientFunds('Недостаточно средств на счёте')

    @staticmethod
    def quantize_money(x: Decimal) -> Decimal:
        return x.quantize(Decimal('0.01'),
                          ROUND_HALF_UP)


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance: Decimal = Decimal('0.00'), currency='RUB',
                 daily_withdraw_limit: Decimal | None = None):
        super().__init__(owner, balance, currency)
        if daily_withdraw_limit is None:
            self.daily_withdraw_limit = None
        else:
            self.daily_withdraw_limit: Decimal = type(self).quantize_money(daily_withdraw_limit)
        self.withdrawn_today: Decimal = Decimal('0.00')
        self.window_date: date = datetime.now(self.tz_info).date()

    def _reset_window_if_need(self, now: date):
        if now != self.window_date:
            self.withdrawn_today = Decimal("0.00")
            self.window_date = now

    def _validate_withdraw(self, amount, now: datetime | None):
        amount_quantize = type(self).quantize_money(amount)

        if now is None:
            now = datetime.now(self.tz_info)
        elif now.tzinfo is None:
            now = now.replace(tzinfo=self.tz_info)
        else:
            now = now.astimezone(self.tz_info)

        local_date = now.date()
        self._reset_window_if_need(local_date)

        super()._validate_withdraw(amount_quantize, now)

        if self.balance < amount_quantize:
            raise InsufficientFunds('Недостаточно средств на счёте')

        if self.daily_withdraw_limit is not None:
            withdrawn_candidate = self.withdrawn_today + amount_quantize
            if withdrawn_candidate > self.daily_withdraw_limit:
                raise LimitExceeded('Превышен суточный лимит снятий.')


    def withdraw(self, amount: Decimal, *, now: datetime | None = None):
        if not isinstance(amount, Decimal):
            raise AccountError('В качестве суммы необходимо передавать тип Decimal')
        if amount <= 0:
            raise InvalidAmount('Сумма должна быть > 0')

        self._validate_withdraw(amount, now)

        amount_quantized = type(self).quantize_money(amount)

        self.balance = type(self).quantize_money(self.balance - amount_quantized)

        if self.daily_withdraw_limit is not None:
            if now is None:
                now = datetime.now(self.tz_info)
            elif now.tzinfo is None:
                now = now.replace(tzinfo=self.tz_info)
            else:
                now = now.astimezone(self.tz_info)
            local_date = now.date()
            self._reset_window_if_need(local_date)
            self.withdrawn_today = type(self).quantize_money(self.withdrawn_today + amount_quantized)




class SavingsAccount(BankAccount):
    def __init__(self, owner, balance: Decimal = Decimal('0.00'), currency='RUB',
                 annual_rate: Decimal = 0.00):
        super().__init__(owner, balance, currency)
        self.annual_rate = Decimal(str(annual_rate))
        self.last_accrual_date: date = datetime.now(self.tz_info).date()  # для этого поля достаточно будет date а не datetime

    @staticmethod
    def _add_months(start: date, months: int):
        if months < 0:
            raise ValueError('Месяц должен быть больше или равен 0')

        year = start.year + (start.month + months - 1) // 12
        month = (start.month + months -1) % 12 + 1

        if month == 12:
            next_month = date(year + 1, 1, 1)
        else:
            next_month = date(year, month + 1, 1)
        last_day = (next_month - timedelta(days=1)).day

        day = min(start.day, last_day)
        return date(year, month, day)


    def accrue_monthly_interest(self, now: date):
        as_of = now
        start = self.last_accrual_date

        total_month = (as_of.year - start.year) * 12 + (as_of.month - start.month)

        if as_of.day < start.day:
            total_month -= 1
        if total_month == 0:
            return Decimal('0.00')

        r_month = (Decimal(1) + self.annual_rate) ** (Decimal(1) / Decimal(12)) - Decimal(1)  # расчитываем месячную ставку

        total_interest = Decimal('0.00')
        balance_work = self.balance

        for month in range(total_month):
            interest = type(self).quantize_money(balance_work * r_month)
            total_interest = type(self).quantize_money(total_interest + interest)
            balance_work = type(self).quantize_money(balance_work + interest)

        self.balance = balance_work
        self.last_accrual_date = as_of

        return total_interest
