# dictionary_name={key-1:value_1,key_2:value2}
collage_1={
    'python':{'duration':3,'level':'basic'},
    'java':{'duration':4,'level':'hard'}
}
print(collage_1)
print(collage_1['python'])
print(collage_1['python']['duration'])


collage_1['python']['level']="extream hard"
print(collage_1)

'''1 Use student_info = {"name": "Ram", "age": 22, "grade": "A", "courses": ["DS", "SQL"]}
Update student's grade to "A+" and display updated dictionary.
Add "level" key with value "Beginner" and display updated dictionary.
Add one more course "Python" to student's courses and display updated dictionary.
Remove age from student information and display updated dictionary.
Display total number of key-value pairs in student_info.'''

student_info = {"name": "Ram", "age": 22, "grade": "A", "courses": ["DS", "SQL"]}
student_info["grade"]='A+'
print(student_info)


#adding a new keys in student info
student_info["level"]="beginner"
print(student_info)


student_info["courses"]='DS','SQL','PYTHON'
print(student_info)

removing_items=student_info.pop("age")
print(removing_items)
print(student_info)


keys_len=len(student_info)
print(keys_len)


