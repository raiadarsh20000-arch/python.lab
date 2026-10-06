#Assign a list of numbers. Find the second largest number in it using a for loop.
number=[23,34,89,43,99]
largest_nun=number[0]
second_largest=number[0]

for i in number:
    if i>number:
        second_largest=largest_num
        largest_nun=i
    if i>largest_nun and i!=largest_nun:
        second_largest=i
print(second_largest)