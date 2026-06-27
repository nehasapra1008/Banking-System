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
    print("create acconnt")

 elif choice == "2":
    print("display account detail")
  
 elif choice == "3":
   print("deposit money")

 elif choice == "4":
   print("withdrow money")

 elif choice == "5":
   print("search account") 

 elif choice == "6":
   print("delete account")

 elif choice == "7":
   print("exit") 

 else:
   print("invalid choice.plese try again")
   break   
