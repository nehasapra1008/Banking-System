from BankingManagementSystem import BankSystem
bank = BankSystem()

while True:

 print("\n=====Banking System====")
 print("1.Create account")
 print("2.Display account detail")
 print("3.Deposit money")
 print("4.Withdrow money")
 print("5.Search account")
 print("6.Delete account")
 print("7.Exit")

 choice = input("Enter your choice :")

 if choice == "1":
    bank.create_account()

 elif choice == "2":
    bank.display_account()
  
 elif choice == "3":
    bank.deposite_money()

 elif choice == "4":
   bank.withdrow_money()

 elif choice == "5":
   bank.search_account()

 elif choice == "6":
   bank.delete_account()

 elif choice == "7":
   print("exit") 

 else:
   print("invalid choice.plese try again")
   break   
