class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Enter a positive amount")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Enter a positive amount")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    def __str__(self):
        return f"{self.owner}: Rs. {self.__balance:.2f}"


account = BankAccount("Ali", 5000)

try:
    account.deposit(2000)
    account.withdraw(1000)
    print(account)
except ValueError as error:
    print("Transaction failed:", error)