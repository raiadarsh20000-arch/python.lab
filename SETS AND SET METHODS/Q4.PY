'''3.1 Store this list: items_sold = ["book", "book", "pen", "pen", "pen", "pencil", "marker", "notebook"]
Convert items_sold into a set named unq_items_set.
Display all unique items sold in the stationery shop.
Display total number of unique items sold.
Sort unique items and display the result.'''

items_sold = ["book", "book", "pen", "pen", "pen", "pencil", "marker", "notebook"]
unq_iteam_set=set(items_sold)
print(unq_iteam_set)

stationary_shop=unq_iteam_set
print(stationary_shop)

print(len(stationary_shop))