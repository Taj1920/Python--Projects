import random

l=['Rock','Paper','Scissor']

while True:
    r=random.randint(0,2)
    for i in range(0,len(l)):
        print(i+1,'--',l[i])

    ch=int(input('Enter your choice: '))
    print('you: ',l[ch-1])
    print('Computer: ',l[r])

    if l[ch-1]==l[r]:
        print('It\'s a Draw')
    elif l[ch-1]=='Scissor' and l[r]=='Paper':
        print('Wow nice you won ..!!')
    elif l[ch-1]=='Paper' and l[r]=='Rock':
        print('You won very nice...')
    elif l[ch-1]=='Rock' and l[r]=='Scissor':
        print('Yow won ....great...!!')
    else:
        print('Computer WINS...You lost....')
    
    a=input('Do you want to Play again?? (y/n): ')
    if a.lower()=='y':
        continue
    else:
        print('Thank you for playing.....')
        break

