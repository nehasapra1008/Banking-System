from Account import Bank
class BankSystem:

    def __init__(self):
        self.accounts = []

    def create_account(self):
        account_no = int(input("Enter account no :"))
        holder_name = input("Enter account holder name :")
        balance = int(input("Enter balance :"))

        bank=Bank(account_no,holder_name,balance)
        
        self.accounts.append(bank)
        print("Account Created successfully!")
    
    def display_account(self):
        print("\nList of Account:")
        for ac in self.accounts:
            ac.display()

    def deposite_money(self):
        print("deposit money")

    def withdrow_money(self):
        print("withdrow money")

    def search_account(self):
        print("search account")

    def delete_account(self):
        account_no = int(input("Enter account_no :"))
        for bank in self.accounts:
            if bank.account_no == account_no:
                self.accounts.remove(bank)
                print("account remove successfully")
                return
        print("account not found.")
        
                        



