from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited {amount} and you have a total of {self.balance}")

    def withdraw(self, amount):
        if (self.balance <= 0 or amount > self.balance):
            print(f"You're broke, you only have {self.balance} lol. Go ask your mom for {amount}.")
        else: 
            self.balance -= amount
            print(f"You withdrew {amount} and now have a balance of {self.balance}")