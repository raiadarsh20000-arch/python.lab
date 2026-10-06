'''Display numbers from 1 to 10 using a for loop.
Display numbers from 1 to 10 using a while loop.
Display even numbers from 1 to 20 using a for loop.
Display odd numbers from 1 to 20 using a while loop.
Assign num = 7. Display its factorial using a for loop.
Assign num = 7. Display its factorial using a while loop.'''
 
for i in  range(10):
    print(i)
    
    
number_list=[1,2,3,4,5,6,7,8,9]
even_num=[]
for x in number_list:
    if x % 2 == 0 :
        even_num.append(x)

print(even_num)

num=7
factorial=1
for i in range(1,num+1):
    factorial = factorial * i
print(f"Factorial of {num} is {factorial}")



num=9
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(factorial)



