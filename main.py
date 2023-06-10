from bank import Bank

from admin import Admin



def main():
    bank = Bank()
    admin = Admin(bank)



    while True:
        print("1. create an account")
        print("2. deposit amount")
        print("3. withdraw amount")
        print("4. transfer amount")
        print("5. check balance")
        print("6. view transaction history")
        print("7. take a loan")
        print("8. repay loan")
        print("9. check account details")
        print("10. check total bank balance")
        print("11. check total loan amount")
        print("12. toggle loan feature")
        print("0. exit")



        choice = input("enter your choice: ")



        if choice == "1":
            name = input("enter account holder name: ")
            bank.create_account(name)
            print("account created successfully.")


        elif choice == "2":
            name = input("enter account holder name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("enter amount to deposit: "))
                account.deposit(amount)
                print("amount deposited successfully.Must be Check Balance")
            else:
                print("account not found.")


        elif choice == "3":
            name = input("enter account holder name: ")
            account = bank.get_account(name)

            if account:
                amount = float(input("enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("account not found.")


        elif choice == "4":

            sender_name = input("enter sender's account holder name: ")
            sender = bank.get_account(sender_name)
            recipient_name = input("enter recipient's account holder name: ")
            recipient = bank.get_account(recipient_name)


            if sender and recipient:
                amount = float(input("Enter amount to transfer: "))
                sender.transfer(recipient, amount)
                print("amount transferred successfully.")
            else:
                print("account not found.")



        elif choice == "5":
            name = input("enter account holder name: ")
            account = bank.get_account(name)
            if account:
                print(f"account balance: {account.check_balance()}")
            else:
                print("account not found.")



        elif choice == "6":
            name = input("enter account holder name: ")
            account = bank.get_account(name)


            if account:
                print("transaction history:")
                for transaction in account.get_transaction_history():
                    print(transaction)
            else:
                print("account not found.")



        elif choice == "7":
            name = input("enter account holder name: ")
            account = bank.get_account(name)


            if account:
                amount = float(input("enter loan amount: "))
                account.take_loan(amount)
                print("loan taken successfully.")
            else:
                print("account not found.")



        elif choice == "8":
            name = input("enter account holder name: ")
            account = bank.get_account(name)


            if account:
                amount = float(input("enter repayment amount: "))
                account.repay_loan(amount)
                print("loan repayment successful.")
            else:
                print(" not found.")




        elif choice == "9":
            name = input("enter account holder name: ")
            print(admin.check_account(name))



        elif choice == "10":
            print(f"total bank balance: {admin.check_total_balance()}")



        elif choice == "11":
            print(f"total loan amount: {admin.check_total_loan_amount()}")



        elif choice == "12":
            loan_feature_enabled = admin.toggle_loan_feature()


            if loan_feature_enabled:
                print("loan feature has been enabled.")
            else:
                print("loan feature has been disabled.")



        elif choice == "0":
            print("thank you  -_-")
            break

        else:
            print("invalid choice.  try again.")




if __name__ == "__main__":
    main()