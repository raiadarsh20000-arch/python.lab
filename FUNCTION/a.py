# a function get_simple_interest(principal, rate, time) to calculate and return simple interest. Formula: simple_interest = (principal * rate * time) / 100
#def simple_interest (principal,rate,time):
def simple_interest(principal,time,rate):

    return (principal*rate*time)/100
principal=float(input('Enter principle:'))
rate=float(input('Enter rate:'))
time=float(input('Enter time:'))
print(f" The simple interest: {simple_interest(principal,time,time)}")