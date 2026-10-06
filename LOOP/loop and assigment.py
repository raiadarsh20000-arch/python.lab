money = 1000

# Spend 250 using -=

money-= 250
print(money)

price = 200

# Double the price using *=

price*=2
print(price)


number = 27

# Use %= to get the remainder when number is divided by 5
number %=5
print(number)


x = 10

x += 5
x *= 2
x -= 8
print(x)

salary = 20000      #initial value salary is 20000 no change

salary += 5000  # salary here is add by 5000 so the total salary is 25000
salary -= 2000  # in this case the salary is been decated or decrease by 2000 so the total price is 25000-2000=23000.
salary *= 2     # so after the decuttion the salary have doubled by twice.so the total price is 46000

print(salary,x,money,number)

total = 500

# Add 200
# Subtract 100 as a discount
# Add 50 delivery charge
total+=200
total-=100
total+=50

print(f"The amount after all the addition and subtraction plus delivery charge is :{total} ")