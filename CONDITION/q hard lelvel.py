#Ask user for electricity unit consumed. Calculate bill using: First 20 units ➜ Rs. 5 per unit. Units from 21 to 50 ➜ Rs. 7 per unit. Units above 50 ➜ Rs. 10 per unit. Display total bill.

consumed_unit=int(input("Enter electricity unit consumed."))
if consumed_unit>=20:
   c0= consumed_unit*5
elif consumed_unit<=21>=50:
    c1=consumed_unit*7
elif consumed_unit>=50:
    c2=consumed_unit*10
    
    print(consumed_unit)