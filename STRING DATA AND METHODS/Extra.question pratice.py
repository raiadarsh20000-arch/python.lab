# File name: student_data_2026
# Extension: xlsx
file_name = "student_data_2026.xlsx"
File_Name, Extension = file_name.split(".")
print(File_Name)
print(Extension)

# 2.
my_date = "2026-09-17"  # --->Day: 17
Year, Month, Day = my_date.split("-")
print("year:", Year)
print("month:", Month)
print("Day:", Day)

# 3.P Y T H O N
my_str = "PYTHON"
new_my_str = "\t".join(my_str)
print(new_my_str)


# Replace every "Java" with "Python" and display the result.
sentence = "I study Java with Java is popular."
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)

# count the  word
word = "programming"
counting = word.count("g")
print(counting)

text = "Python is powerful. Python is popular."
counting_python = text.count("Python")
print(counting_python)

word = "COMPUTER"
vowel = "a,e,i,u,o"
reslut = (
    word.lower().count("e")
    + word.lower().count("i")
    + word.lower().count("o")
    + word.lower().count("a")
)
print(reslut)

# sales_report_2026_backup.csv
# Name: sales_report_2026
# Extension: csv

file_name = "sales_report_2026.csv"
Name, EXtension = file_name.split(".")
print("Name:", Name)
print("Extension:", EXtension)

new_file = Name + "_cave." + EXtension
print(new_file)
