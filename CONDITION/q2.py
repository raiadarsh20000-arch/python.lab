#Store customer balance in a variable. Ask user for amount to withdraw. If withdraw amount is less than or equal to balance, display: 123 withdrawn successfully. New Balance: 456. Otherwise display: Insufficient balance. You only have 123 in your account
current_balance=10000
withdraw_amount=int(input("Enter amount to withdraw:"))
if withdraw_amount<=current_balance:
        remaning_amount=current_balance-withdraw_amount
        print(f' Rs {withdraw_amount} : successfuly withdraw.New balance is Rs {remaning_amount}')
else:
    print(f" Insufficient balance.you only have Rs {current_balance}" )