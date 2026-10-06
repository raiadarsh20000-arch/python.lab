# Practice creating and accessing list items:
# Create a list named student_names with names of five students.
# Create a list named marks with marks in five subjects.
# Display the first student name.
# Display the last student name using negative indexing.
# Display the second and third marks using slicing.
# Change the second student name to "Python" and display the updated list.
# Create a nested list in this format: [[name_1, age_1], [name_2, age_2], [name_3, age_3]]. Display the second student's age.


student_list = ["Hari", "Sayam", "kunti", "Arjun", "krishna"]
print(student_list)
print(type(student_list))

"""student_list = ["Hari", "Sayam", "kunti", "Arjun", "krishna"]
student_marks = [69, 77, 76, 78, 80]

show_result = input(f"student name:")

if show_result in (student_list):
    index = student_list.index(show_result)
    print(f"{show_result} scored {student_marks[index]} marks.")
else:
    print("NOTHING FOUND")"""


student_list = ["Hari", "Sayam", "kunti", "Arjun", "krishna"]
print(student_list[0])


print(student_list[-1])


replace_name = student_list[1] = "Python"
print(replace_name)

print(student_list)
