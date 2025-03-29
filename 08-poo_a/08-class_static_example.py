

class BankAccount:
    interest_rate = 0.02

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print("Interés cambiado")

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def withdraw(self, amount):
        if self.validate_amount(amount):
            if self.balance >= amount:
                self.balance -= amount
                print("Retiro éxitoso")
            else:
                print("Saldo insuficiente")
        else:
            print("Error: El monto debe ser mayor a cero")


account1 = BankAccount("Ricardo", 1000)
account2 = BankAccount("Dante", 300)

print(BankAccount.interest_rate)
BankAccount.change_interest_rate(0.03)
print(BankAccount.interest_rate)

account1.withdraw(500)
account2.withdraw(-100)

print(BankAccount.validate_amount(-100))
