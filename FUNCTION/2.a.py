#Write a function greet(name, course="Python") that returns: Hello, {name}, Welcome to {course} class. Call this function once by passing your name only, and another time by passing your name and "Data Science".
def greet(name,course='Python'): 
    return f"hello,{name},Welcome,to {course}"
print(greet('Bishwas'))
print(greet('Bishwas','Data science'))