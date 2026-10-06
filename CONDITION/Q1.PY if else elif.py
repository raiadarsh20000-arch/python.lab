#Ask user for name and birth year. Calculate age and display voting eligibility in this format: Ram, You are eligible for voting or Ram, You are not eligible for voting. Rule: 18+ people can vote.
import math
from datetime import date
user_name=input("Enter ur name:")
user_birth_year=int(input("Enter ur birth year"))

curent_year=date.today().year
age=curent_year-user_birth_year
if age>=18:
    print( f"{user_name} you are egiabile for vote")
else:
    print( f"{user_name} you are not egiable for vote.")


