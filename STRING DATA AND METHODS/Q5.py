file_name = "report_2026.pdg"
file, extesion = file_name.split(".")
print("file_name:", file)
print("file_exten:", extesion)


my_date = "20260 - 3 - 46"
years, month, day = my_date.split("-")
print("years", years)
print("month", month)
print("day", day)

mu_str = "PYTHON"
adding__ING = ".".join(mu_str)
print(adding__ING)

myt_str = "HELLO,WORLD"
x = myt_str.replace("WORLD", "PYTHON")
print(x)

date = "2029-4-6"
new_date = date.replace("-", "/")
print(new_date)

set_3 = "pineapple"
indexing = set_3[4:]
print(indexing)

vowel_letter = "a", "i", "o", "e"
your_name = "Bishwas raie"
result = (
    your_name.count("a")
    + your_name.count("i")
    + your_name.count("o")
    + your_name.count("e")
)

print(result)


my_str = "Hello,World!"
occurance_test = myt_str.lower().count("l")
print(occurance_test)
