import random
def hangman():
    r=random.randint(0,24)
    print('---------Welcome to Hangman Game------')
    words = [
        "apple",
        "italy",
        "pizza",
        "banana",
        "japan",
        "sushi",
        "france",
        "croissant",
        "mango",
        "australia",
        "burger",
        "strawberry",
        "brazil",
        "pasta",
        "laptop",
        "smartphone",
        "tablet",
        "smartwatch",
        "headphones",
        "camera",
        "television",
        "router",
        "speaker",
        "monitor"
    ]

    fruits = ["apple","banana","mango","strawberry"]

    countries = ["italy","japan","france","australia","brazil"]

    food_items = ["pizza","sushi","croissant","burger","pasta"]

    electronic_devices= ["laptop","smartphone","tablet","smartwatch","headphones",
        "camera","television","router","speaker","monitor"]


    s=words[r]
    if s in fruits:
        print('HINT: It is a fruit name..')
    elif s in countries:
        print('HINT: It is a country name..')
    elif s in food_items:
        print('HINT: It is a food item name..')
    else:
        print('HINT: It is an electronic device name..')


    l=[]
    for i in s:
        l.append('_')
    print(' '.join(l))
    c=7
    while c:
        print(' ')
        ch=input('Enter a char: ').lower()
        if ch in s:
            for index,char in enumerate(s):
                if ch==char:
                    l[index]=char
            
            print(' '.join(l))
            for _ in l:
                if _=='_':
                    break
            else:
                print('---------you won!!..🎉🎉🏆🏆-------')
            if '_' not in l:
                break
        else:
            print('char not present..😑😑')
            c-=1
            print('Chances Left: ',c)
    else:
        print(' ')
        print('you are Hanged... 💀💀')
        print(' ')
        print('correct ans: ',s)
        print(' ')
        print('----------GAME OVER 💀💀--------')
    
    a=input('Do you want to play again? (y/n): ')
    if a.lower()=='y':
        hangman()
    else:
        print('Thank you!!!!..😊😊')
hangman()