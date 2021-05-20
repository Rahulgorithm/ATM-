Ammount = int(input("Enter Ammount: "))
Balance = int(input("enter balance: "))

if Ammount % 5 == 0:
    if Balance>Ammount:
        Remaining_balance = Balance-Ammount-(2/100*Ammount)
        print("Transaction Sucessfull, Remaining balance is", Remaining_balance)
    else:
        print("insufficient Funds")
else:
    print("Not Avilable")
