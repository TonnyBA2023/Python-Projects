from datetime import datetime


class BankAccount:
    def __init__(self, account_number, owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        self.transaction_history.append(
            f"{datetime.now()} - Deposit: {amount}"
        )

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        self.transaction_history.append(
            f"{datetime.now()} - Withdrawal: {amount}"
        )

    def get_balance(self):
        return self.balance

    def print_statement(self):
        print(f"\nStatement for {self.owner_name}")
        print("-" * 40)

        for transaction in self.transaction_history:
            print(transaction)

        print(f"\nCurrent Balance: {self.balance}")
