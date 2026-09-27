class Account:
    def _init_(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

a = Account(1000)
a.deposit(500)
print(a.get_balance())