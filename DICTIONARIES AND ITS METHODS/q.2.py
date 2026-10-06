"""Keys, Values, Items, and Membership
Question 3 of 7

Check
3.1 Use student_info = {"name": "Ram", "age": 22, "grade": "A", "courses": ["DS", "SQL"]}
Display all keys.
Display all values.
Display all key-value pairs.
Check if "address" key is present in student_info.
Check if "grade" key is present in student_info.
Check if "Ram" is present in  dictionary values.
Check if "Kathmandu" is present in dictionary values."""

Use_student_info = {"name": "Ram", "age": 22, "grade": "A", "courses": ["DS", "SQL"]}
only_keys=(Use_student_info.keys())
print(only_keys)

only_value=(Use_student_info.values())
print(only_value)


print(Use_student_info)

print("Adressh" in Use_student_info)

print("Ram" in Use_student_info.values())

print("kathmandu"in Use_student_info.values())