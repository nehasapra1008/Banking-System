class Account:

    def __init__(self,account_no,holder_name,balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance
        print("-"*20)

    def display(self):
        print("*********")
        print(f"account_no : {self.account_no}")
        print(f"holder_name : {self.holder_name}")
        print(f"balance : {self.balance}")
        

