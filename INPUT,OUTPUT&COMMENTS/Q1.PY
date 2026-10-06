# Practice output and f-string formatting:
# Create a variable name and display: Hello, {name}!
# Create variables name and age. Display output in this format: My name is Python and I am 30 years old.
# Create variables item and price. Display output in this format: Ram bought a pen for Rs. 10.56.
# Create variable age. Display what the age will be next year using an f-string.

NAME = "Bishwas Rai"
print(f"Hello,{NAME}!")

age = int(19)
print(f"My name is {NAME} and I am {age}years old.")


pen_price = float(10.56)
print(f"Ram bought a pen for Rs{pen_price}.")

current_age = age
next_year = current_age + 1
print(f"I will be {next_year}years old.")
