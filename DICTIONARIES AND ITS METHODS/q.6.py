'''Copying Dictionary
Question 4 of 7

Check
4.1 Use student_info = {"name": "Ram", "age": 22, "grade": "A"}
Create a copy of student_info.
Update copied dictionary name to "Bob".
Update copied dictionary grade to "B".
Display original dictionary.
Display copied dictionary.
Assign student_info to another variable using =.
Update age using the new variable.
Display both dictionaries and observe the result.'''

orignal_name={"name":"Bishwas","age":19}
copy_name=orignal_name.copy()
copy_name["name"]=['Bob']
copy_name["age"]=20
print(copy_name)
print(orignal_name)
