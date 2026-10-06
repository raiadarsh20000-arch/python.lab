salary_tuple=(20000,25000,30000)
vice=len(salary_tuple)
print(f"Numbers of employees:{vice}")


total_salary=sum(salary_tuple)
print(f"Total salary paid to employees:{total_salary}")

Average_salary=total_salary/3
print(f"Average salry per employee is:{Average_salary}")


highest_salry=max(salary_tuple)
print(f"Highest paid amount to employees:{highest_salry}")

lowest_salary=min(salary_tuple)
print(f"lowest paid amount to employees:{lowest_salary}")


num_of_low_paid=salary_tuple.count(lowest_salary)
print(num_of_low_paid)