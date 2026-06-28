from Bank import Account
class BankSystem:

    def __init__(self):
        self.accounts = []

    def create_account(self):
        account_no = int(input("Enter account no :"))
        holder_name = input("Enter account holder name :")
        balance = int(input("Enter balance :"))

        bank=Account(account_no,holder_name,balance)
        
        self.accounts.append(bank)
        print("Account Created successfully!")
    
    def display_account(self):
        print("\nList of Account:")
        for ac in self.accounts:
            ac.display()

    def deposite_money(self):
       ac_no=int(input("Please Enter Your Account No : "))
       for a in self.accounts:
           print(f"{a.account_no}")
           if(a.account_no ==ac_no):
               deposit_amount=int(input("Please Enter Your Deposit Amount : "))
               a.balance=a.balance + deposit_amount
               print("Deposit Successfully")
                  
    def withdrow_money(self):
        print("withdrow money")

    def search_account(self):
        print("search account")

    def delete_account(self):
        account_no = int(input("Enter account_no :"))
        for bank in self.accounts:
            if Account.account_no == account_no:
                self.accounts.remove(bank)
                print("account remove successfully")
                return
        print("account not found.")
        
                        



