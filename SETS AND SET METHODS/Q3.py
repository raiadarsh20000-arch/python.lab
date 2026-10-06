'''2. Adding and Removing Set Items
Question 2 of 6

Check
2.1 Create unq_items_set = {"book", "pen", "pencil", "marker", "notebook"}
Add "sticky_notes" to unq_items_set and display the updated set.
Add "pen" again and observe the result.
Create new_items = ["highlighter", "chart_paper"].
Add all items from new_items to unq_items_set using update().
Remove "pen" using remove() and display the updated set.
Try to remove "eraser" using discard() and display the result.
Remove one arbitrary item using pop().
Display the removed item.
Display the updated set.'''

unq_items_set = {"book", "pen", "pencil", "marker", "notebook"}
unq_items_set.add("stick_note")
print(unq_items_set)

unq_items_set.add("pen")
print(unq_items_set)


new_items={"roluar","compash","protacter"}
unq_items_set.update(new_items)
print(unq_items_set)