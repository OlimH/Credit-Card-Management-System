from datetime import datetime

class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = float(limit)
        self.balance = 0.0
        self.transactions = []

    def charge(self, amount):
        if amount <= 0:
            raise ValueError("Charge amount must be greater than zero")
        if self.balance + amount > self.limit:
            return False
        self.balance += amount
        self.transactions.append({"type":"PURCHASE","amount":amount,"timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        return True

    def make_payment(self, amount):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero")
        self.balance -= amount

    def available_credit(self):
        return self.limit - self.balance

    def utilization_percentage(self):
        return round((self.balance/self.limit)*100,2)

    def get_balance(self):
        return round(self.balance,2)

    def get_transaction_history(self):
        return self.transactions

    def __str__(self):
        return f"Customer: {self.customer}\nBalance: ${self.balance:.2f}"
