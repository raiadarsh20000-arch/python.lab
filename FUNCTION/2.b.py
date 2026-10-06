#Write a function calculate_discount(price, discount=10) that returns final price after discount.
def calculate_discount(price,discount=10):

    return price-(price*discount/100)
print(calculate_discount(1900))
    