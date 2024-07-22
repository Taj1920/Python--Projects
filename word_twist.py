import random
d = {
    "tca": ["cat", "act"],
    "lpepa": ["apple"],
    "ateb": ["beat", "beta"],
    "rcsa": ["scar", "cars", "arcs"],
    "edr": ["red"],
    "tsae": ["seat", "east"],
    "rcae": ["care", "race"],
    "tloh": ["holt", "loth"],
    "prsae": ["parse", "spare", "spear", "pears"],
    "kool": ["look"],
    "pale": ["leap", "pale", "plea"],
    "arc": ["car", "arc"],
    "plehe": ["help"],
    "tsil": ["list", "slit"],
    "opst": ["post", "spot", "stop", "tops", "pots"],
    "elas": ["sale", "seal"],
    "trit": ["tirt", "trit"],
    "draob": ["board", "broad"],
    "nopia": ["piano"],
    "peehs": ["sheep"],
    "mrea": ["ream", "mare"],
    "enot": ["note", "tone"],
    "dgo": ["dog", "god"],
    "hsif": ["fish"],
    "kciuq": ["quick"]
}

def play(d):
    s=list(d)[random.randint(0,len(d))]
    print('word is: ',s)
    print('possible words: ',len(d[s]))
    print('Guess the words')
    c=10
    l=[]
    while c:
        word=input('Enter your word: ').lower()
        if word in d[s] and word not in l:
            l.append(word)
            print(f'{word} is correct')
            if len(l)==len(d[s]):
                print('you won!!!  all the words are correct 🎉🥇')
                break
        else:
            print('Incorrect..')
            c-=1
            print('Chances Left: ',c)
    else:
        print('you Lost😒😒')
        print('correct words: ',d[s])
    a=input('Do you want to play again? (y/n): ').lower()
    if a=='y':
        play(d)
    else:
        print('Thanks for playing!!')
play(d)