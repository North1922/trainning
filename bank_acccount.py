# 6) Банковские счета
#
# Классы: Account (абстрактный), CheckingAccount, SavingsAccount, Bank.
# Методы: deposit(amount), withdraw(amount), transfer(to, amount).
# Проверки: сумма > 0; овердрафт по правилам типа счёта.
# Инварианты: баланс ≥ минимально допустимого.
# Усложнение: проценты по SavingsAccount; собственные исключения (InsufficientFundsError).

# 6) Банковские счета
#
# Сущности: Account (абстрактный), CheckingAccount, SavingsAccount, Bank.
#
# Атрибуты:
#
# Account: account_id, owner, balance.
#
# CheckingAccount: overdraft_limit.
#
# SavingsAccount: interest_rate_apy.
#
# Методы (обязательные):
#
# Account.deposit(amount) — сумма > 0.
#
# Account.withdraw(amount) — политика по типу счёта (овердрафт у чекового, запрет у сберегательного).
#
# Account.transfer(to, amount) — атомарно: списать/зачислить.
#
# Bank.open_account(account) / close_account(account_id).
#
# Bank.find_account(account_id).
#
# SavingsAccount.apply_interest(days) — начисление процентов (можно просто по дням).
#
# Проверки/ошибки: недостаточно средств; отрицательные суммы; перевод на тот же счёт.
#
# Инварианты: баланс не падает ниже правила счёта.
#
# Усложнения: комиссии за перевод; блокировки на время расследований; кастомные исключения.