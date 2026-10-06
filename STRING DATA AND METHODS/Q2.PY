# """Create a variable my_str that stores We are learning Python and it's fun!
# Find and display the first character.
# Find and display the character at index 8.
# Find and display the last character using negative indexing.
# Find the word Python using slicing and display it.
# Find the word fun using negative indexing and display it.
# Find the text lrn from the word learning and display it.
# Reverse the string and display it.
# Find the substring from index 5 till the end and display it.
# Find the substring from the start till index 10 and display it."""

course = "We are learning python and it's fun!"

first_character = course[0]
print(first_character)

indexing_course = course[8]
print(indexing_course)

last_character = course[-1]
print(last_character)

fing_by_slicing = course[16:22:]
print(fing_by_slicing)

negative_index = course[-4:]
print(negative_index)

reverseing_string = course[::-1]
print(reverseing_string)

secand_case = course[::-5]
print(secand_case)
