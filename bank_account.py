from abc import ABC, abstractmethod

class BankAccount(ABC):
    # constructor
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass
