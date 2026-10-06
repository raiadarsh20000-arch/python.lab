"""""5.1 Create college_1 = {"python": {"duration": 3, "type": "basic"}, "java": {"duration": 4, "type": "medium"}} and college_2 = {"multimedia": {"duration": 2, "type": "basic"}, "javascript": {"duration": 5, "type": "advanced"}}
Display python course details.
Display python course duration.
Display java course type.
Update python course type to "advanced".
College_1 acquired College_2. Update College_1 courses with College_2 courses.
Display updated College_1 dictionary."""


college_1={"python": {"duration": 3, "type": "basic"}, 
          "java": {"duration": 4, "type": "medium"}
           } 
college_2 = {"multimedia": {"duration": 2, "type": "basic"},
             "javascript": {"duration": 5, "type": "advanced"}
             }
college_1 ["python"]["type"]="advance"
print(college_1)

college_1.update(college_2)
print(college_1)


print(list(range(5)))

print(list(range(1,6)))
 
print(list(range(0,5)))