class Account:


    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.transaction_history = []
        self.loan_amount = 0.0



    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"deposit: +{amount}")



    def withdraw(self, amount):


        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"withdrawal: -{amount}")
            else:
                print("insufficient balance.")



    def transfer(self, recipient, amount):


        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                recipient.deposit(amount)
                self.transaction_history.append(f"transfer to {recipient.name}: -{amount}")
                recipient.transaction_history.append(f"transfer from {self.name}: +{amount}")

            else:
                print("insufficient balance.")



    def check_balance(self):
        return self.balance



    def get_transaction_history(self):
        return self.transaction_history



    def take_loan(self, amount):


        if amount > 0:
            max_loan_amount = self.balance * 2
            if amount <= max_loan_amount:
                self.loan_amount += amount
                self.balance += amount
                self.transaction_history.append(f"loan received: +{amount}")
            else:
                print(f"you  can  only  borrow up  to {max_loan_amount} based  on your  account  balance.")



    def repay_loan(self, amount):

        
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.loan_amount -= amount
                self.transaction_history.append(f"loan repayment: -{amount}")
            else:
                print("insufficient balance to repay the loan.")