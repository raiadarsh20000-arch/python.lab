#Create a global variable x = 10. Create a function that has local variable x = 5 and prints it. Print x outside the function and observe the result.
x=10
def local_variable():
    x=5
    print(f"locAL variable:",{x} )
local_variable()
print(f'global variable',{x})


