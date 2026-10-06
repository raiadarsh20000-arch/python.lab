"""4. Combining, Sorting, and Copying Lists
Question 4 of 5

Check
Practice combining, sorting, and copying lists:
Create list_1 = [1, 2, 3] and list_2 = [4, 5, 6].
Combine both lists using + and display the result.
Extend list_1 using list_2 and display list_1.
Create book_list = ["harry_potter", "lord_of_rings", "math"].
Create book_2 = ["math", "science", "history"].
Add all books from book_2 to book_list and display the result.
Sort book_list in ascending order and display it.
Sort book_list in descending order and display it.
Sort book_list based on length of book name and display it.
Create a copy of book_list.
Add a new book to the copied list.
Display both original and copied lists."""

list_1 = [2, 4, 6]
list_2 = [3, 6, 9]
combined_llist = list_1 + list_2
print(combined_llist)

list_1.extend(list_2)
print(list_1)
print(list_2)


book_list = ["harry_potter", "lord_of_rings", "math"]
book_2 = ["math", "science", "history"]
book_list.extend(book_list)
book_list.sort()
print(book_list)


book_list = ["harry_potter", "lord_of_rings", "math"]
book_2 = ["math", "science", "history"]
book_list.extend(book_list)
book_list.sort(reverse=True)
print(book_list)


book_2 = ["math", "science", "history"]
book_list.sort(key=len)

print(book_list)


book_list = ["harry_potter", "lord_of_rings", "math"]

new_list = book_list.copy()
new_list.append("Economic")
print(new_list)
print(book_list)
