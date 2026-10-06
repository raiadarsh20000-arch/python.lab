def can_get_adult_age (age):
    if type(age)not in (int):
        raise TypeError ("Age should be in integer form")
    if age<0:
        raise ValueError(" Age is not  valid")
    if age>100:
        raise ValueError("Age is not valid")
    if age>=18:
        return True
    else:
        return False
    