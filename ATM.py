#Mini Project on ATM
'''1) check_bal
2) deposit
3)withdraw
4)set_pin
variables:  bal=0
            og_pin=None
'''

#create set_pin function

bal=0
og_pin=None

def set_pin():
    global og_pin
    while True:
        print('-'*60)
        if og_pin==None:
            pin1=int(input('Enter a 4 Digit Pin: '))
            pin2=int(input('Confirm your Pin: '))
            if pin1==pin2:
                print('Pin set successful')
                og_pin=pin1
                break
            else:
                print("Incorrect Pin or Pin doesn't match")
        else:
            print('Pin is already set')

def check_bal():
    pin=int(input('Enter a 4 Digit Pin: '))
    if pin==og_pin:
        print('Available Balance in your A/C is: ',bal,'Rs.')
    else:
        print('Incorrect Pin or pin not set')

def deposit():
    global bal
    pin=int(input('Enter a 4 Digit Pin: '))
    if pin==og_pin:
        amt=int(input('Enter your amount to Deposit: '))
        bal+=amt
        print(f'Amount of {amt} Rs. Deposited Successfully')
    else:
        print('Incorrect Pin or pin not set')

def withdraw():
    global bal
    pin=int(input('Enter a 4 Digit Pin: '))
    if pin==og_pin:
        amt=int(input('Enter your amount to Withdraw: '))
        if amt<=bal:
            bal-=amt
            print(f'Amount of {amt} Rs. Withdraw Successful')
        else:
            print('Insufficient Funds')
    else:
        print('Incorrect pin or pin not set')
def services():
    while True:
        print('-'*60)
        print('-----WELCOME TO THIS ATM------')
        print('Enter 1: Deposit')
        print('Enter 2: Withdraw')
        print('Enter 3: Check Balance')
        print('Enter 4: Set Pin')
        print('Enter 5: Exit')
        choice=int(input('Enter your choice: '))
        if choice==1:
            deposit()
        elif choice==2:
            withdraw()
        elif choice==3:
            check_bal()
        elif choice==4:
            set_pin()
        elif choice==5:
            print('Thank you for using our ATM services....')
            break
        a=input('Do you want to continue (y/n)? :  ')
        if a.lower()=='y':
            continue
        else:
            print('Thank you for using our ATM services....')
            break

services()
    
