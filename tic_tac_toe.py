import numpy as np

def disp_board(board):
    print()
    for i in board:
        for j in i:
            print(j,end='|')
        print()

def play():
    board=np.array([['_','_','_'],
                ['_','_','_'],
                ['_','_','_']])
    empty=board
    p1=False
    p2=False
    print()
    disp_board(board)
    print('select player 1 (or) 2')
    ch=int(input('Enter your choice: '))
    if ch==1:
        p1=True
    else:
        p2=True

    while True:
        print(f'player 1\'s Turn' if p1==True else f'player 2\'s Turn')
        print('Rows--> 0, 1, 2')
        print('Cols--> 0, 1, 2')
        print()
        r,c=int(input('Enter row: ')),int(input('Enter col: '))

        if  0<=r<=2 and 0<=c<=2 and board[r][c]=='_':
            if p1==True:
                board[r][c]='X'
                p1,p2=p2,p1
            else:
                board[r][c]='o'
                p1,p2=p2,p1
            disp_board(board)
            if list(board[0])==['X','X','X'] or list(board[1])==['X','X','X'] or\
                list(board[2])==['X','X','X'] or list(board[0:,0:1])==[['X'],['X'],['X']] or\
                list(board[0:,1:2])==[['X'],['X'],['X']] or list(board[0:,2:])==[['X'],['X'],['X']] or\
                (board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X') or \
                (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X'):
                print('Player 1 won🏆🎉')
                break
            elif list(board[0])==['o','o','o'] or list(board[1])==['o','o','o'] or\
                list(board[2])==['o','o','o'] or list(board[0:,0:1])==[['o'],['o'],['o']] or\
                list(board[0:,1:2])==[['o'],['o'],['o']] or list(board[0:,2:])==[['o'],['o'],['o']] or\
                (board[0][0]=='o' and board[1][1]=='o' and board[2][2]=='o') or \
                (board[0][2]=='o' and board[1][1]=='o' and board[2][0]=='o'):
                print('Player 2 won🏆🎉')
                break
            elif np.all(board!='_'):
                print('Draw!! Game over❌')
                break
        else:
            print('Invalid😵')
    
    if input('Do you want to play agiain❓ (y/n): ').lower()=='y':
        play()
    else:
        print('Thank you for playing!!😊')
        
    
play()


        


