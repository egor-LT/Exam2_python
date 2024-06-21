class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._log = []
        return cls._instance

    def log(self, message):
        self._log.append(message)

    def get_logs(self):
        return self._log


class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.logger = Logger()
        self.logger.log(f"Account {self.account_number} created with balance {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.logger.log(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.logger.log(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            self.logger.log(f"Failed withdrawal attempt of {amount} from account {self.account_number}. Insufficient funds.")
            raise ValueError("Insufficient funds for withdrawal.")


# Приклад використання:
try:
    account = BankAccount("12345678", 100)
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(150)  # Це викличе виняток

except ValueError as e:
    print(e)

# Виведення логів:
logger = Logger()
logs = logger.get_logs()
for log in logs:
    print(log)
