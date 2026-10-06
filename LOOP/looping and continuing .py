#Assign num_tuple = (1, 4, 7, 12, 20). Using a loop, find even numbers and their sum

num_tuple = (1, 4, 7, 12, 20)
even_num=[]
sum_num=0
for x in num_tuple:
    if x %2 ==0 :
        even_num.append(x)
        sum_num += x
print(f"Even numbers: {even_num}")
print(f"Sum of even numbers: {sum_num}")
