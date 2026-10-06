# Practice using comments in code:
# WRite a program that displays your name and age. Add a comment explaining what the program does.
# Write a program that calculates area of a rectangle. Add comments explaining length, breadth, and area.
# Write a program that converts feet to meter. Add comments explaining the formula.
# Write a program with at least three lines of code and use Ctrl + / in VS Code to comment and uncomment them.

NAME = "Bishwas Rai"  # i have given mine varaible a meaning full name that is Name because i'm writting mine name so it should be realted that topic
age = int(
    19
)  # same logive i hae used for creating this block of code as upper code line i have added specifice function name
print(f"My  name is {NAME} and I'm {age}years old")

length = int(23)
breadth = int(22)
area_of_rectangle = (
    length * breadth
)  # ok so the given value is kept in a meaningfull variable thus in secand code of line i have put the logic to calculate the are of rectangle the frmula is 2(l+b)
# but computer doesnt under the empty so ihave again add for more accruacy to near mine desire operation symbole of "*" which mean multiplicationn.
print(f"Area of rectangle is {area_of_rectangle} cm")


one_feet = input(int())
convertig_into_int = int(one_feet)
one_metter = 0.3048
open_colum = int(one_feet) * (one_metter)
print(f"converting feet into {open_colum} metter")
