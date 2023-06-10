from bank import Bank


class Admin:
    def __init__(self, bank):
        self.bank = bank



    def check_account(self, name):
        account = self.bank.get_account(name)


        if account:
            return account.get_account_details()
        else:
            return "Account not found."
        



    def check_total_balance(self):
        total_balance = sum(account.balance for account in self.bank.accounts)
        return total_balance
    


    def check_total_loan_amount(self):
        total_loan_amount = sum(account.loan_amount for account in self.bank.accounts)
        return total_loan_amount
    

    

    def toggle_loan_feature(self):
        self.bank.loan_feature_enabled = not self.bank.loan_feature_enabled
        return self.bank.loan_feature_enabled

