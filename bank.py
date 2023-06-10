from account import Account



class Bank:
    
    def __init__(self):
        self.accounts = []
        self.loan_feature_enabled = True




    def create_account(self, name):
        account = Account(name)
        self.accounts.append(account)




    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None
    