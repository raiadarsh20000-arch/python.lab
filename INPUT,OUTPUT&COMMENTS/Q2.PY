num = 3.14159
print(f"{num:.2f}")


item_1 = "Apple"
price_1 = 3

item_2 = "Banana"
price_2 = 7

items_3 = "orange"
price_3 = 8

print(f"{'item':>5}{'price':>10}")
print("-" * 17)
print(f"{item_1:<16}{price_1:>6}")
print(f"{item_2:<16}{price_2:>6}")
print(f"{items_3:<16}{price_3:>6}")


price = 125.5
new_price = price = 242.5656
print(f"Rs{new_price}")

num = 123
print(f"{num:->10}")
print(f"{ num:-<10}")
print(f"{num:*^10}")
