# Practice combined input, calculation, and formatting tasks:
# Ask user for name and price of a pen. Display output in this format: Ram bought a pen for Rs. 10.56.
# Ask user for current year, month, and day. Display it in this format: Today's Date: 2026-03-12
# Ask user for name and marks in 3 subjects. Calculate average percentage and display: Hari scored 85.5% in exam.
# Ask user for mass and length of a cube. Calculate and display its density.
# Formula: density = mass / volume, volume = length ** 3
# Ask user for a file name in format file.ext. Extract and display the file extension.

"""name = input("Enter user name:")
price = input("Enter price of a pen:")
print(f"{name} bought a pen for Rs.{price}")"""

""""year_2 = input("current year:")
month_3 = input("current month:")
day_3 = input("current day:")
todays_date = ("year,month,day").join
print(f"Today's date :{year_2}/{month_3}/{day_3}")"""


"""user_name = input("Enter name:")
subject_one = int(89)
subject_two = int(88)
subject_three = int(78)

average_marks = (subject_two + subject_one + subject_three) / 3
print(f"{user_name} SCORED {average_marks}% IN EXAM.")"""


mass_c = float(
    input("Enter cm:")
)  # Formula: density = mass / volume, volume = length ** 3
length_f_cube = float(input("Enter cm:"))
volume = length_f_cube**3
formula_for_density = mass_c / volume
print(f"density :{formula_for_density}")
