"""Create a shopping list shopping_list = ["rice", "oil", "salt", "sugar"]
Display the first item.
Display the last item.
Add "tea" to the list.
Insert "milk" at index 1.
Remove "salt" from the list.
Remove the last item using pop().
Display the removed item.
Display the updated shopping list.
Display the total number of items.
Display all shopping items separated by comma."""

shopping_list = ["rice", "oil", "salt", "sugar"]
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("tea")
print(shopping_list)

shopping_list.insert(
    1, "milk")  # i have used , and () typle because in list we can only add typle because it non muital but support in other list.
print(shopping_list)

print(len(shopping_list))




shopping_list.remove("salt")
print(shopping_list)


shopping_list.pop()
print(shopping_list)



shopping_list.split(",")
print(shopping_list)