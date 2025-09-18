#Algorithm for simulating ATM cash withdrawal with balance check
balance=int(input("Enter your balance:"))
withdrawal_amount=int(input("Enter amount you want to withdraw:"))
while withdrawal_amount!=0:
    if withdrawal_amount<=balance:
        balance-=withdrawal_amount
        print("Withdrawal successful, Remaining Balance:", balance)
    else: 
        print("Insufficient Balance")
    withdrawal_amount=int(input("Enter amount you want to withdraw:"))
print("Final Balance:", balance)