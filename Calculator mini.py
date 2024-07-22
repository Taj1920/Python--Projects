#Mini Project on Calculator
'''Create a get function which will take and return two \
inputs from the user'''

def get():
    a=int(input('Enter val1: '))
    b=int(input('Enter val2: '))
    return a,b


#Create functions which will perform mathematical operations
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def true_div(a,b):
    return a/b
def floor_div(a,b):
    return a//b
def mod(a,b):
    return a%b
def fact():
    a=int(input('Enter val: '))
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
def sqrt():
    a=int(input('Enter val: '))
    return a**(1/2)
def power(a,b):
    return a**b

while True:
    print('-'*45)
    print('Enter 1: addition')
    print('Enter 2: subtraction')
    print('Enter 3: Multiplication')
    print('Enter 4: True Division')
    print('Enter 5: Floor Division')
    print('Enter 6: Modular Division')
    print('Enter 7: Factorial')
    print('Enter 8: square root')
    print('Enter 9: Power')
    print('Enter 10: To Exit the app')
    choice=int(input('Enter your choice: '))
    if choice==1:
        m,n=get()
        print('The Sum is: ',add(m,n))
    elif choice==2:
        m,n=get()
        print('Sub is: ',sub(m,n))
    elif choice==3:
        m,n=get()
        print('Mul is: ',mul(m,n))
    elif choice==4:
        m,n=get()
        print('True division is: ',true_div(m,n))
    elif choice==5:
        m,n=get()
        print('Floor Division is: ',floor_div(m,n))
    elif choice==6:
        m,n=get()
        print('Modular Division is: ',mod(m,n))
    elif choice==7:
        print('Factorial is: ',fact())
    elif choice==8:
        print('Square root is: ',sqrt())
    elif choice==9:
        m,n=get()
        print('Power is: ',power(m,n))
    elif choice==10:
        print('Thank you for using this app')
        break
    else:
        print('Invalid Choice')
