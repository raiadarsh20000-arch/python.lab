subject_list=["Math","Science","English","Computer"]
mark_list=[90,97,93,95]

totoal_marks=sum (mark_list)
print(totoal_marks)

highest_marks=max(mark_list)
now_postion= mark_list.index(highest_marks)
final_position= subject_list[now_postion]

print(final_position)



subject_list = ["Math", "Science", "English", "Computer", "Nepali"]
mark_list = [80, 75, 89, 95, 20]

highest_mark = max(mark_list)
highest_index = mark_list.index(highest_mark)

name_of_subject = subject_list[highest_index]

print(name_of_subject)




lowest_mark=min (mark_list)
finding_index=mark_list.index(lowest_mark)

last_position=subject_list[finding_index]
print(last_position)