import os

# Just initiating some variables so they can be used in any functions
people = {'p1':'X', 'p2':'O'}
table = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print('Hello players!!')
person1 = input('Enter 1st player Name: ')
person2 = input('Enter 2nd person Name: ')

# Checking the winner
def check_winner(name):
    row = table[0][0] == table[0][1] == table[0][2] or \
        table[1][0] == table[1][1] == table[1][2] or \
        table[2][0] == table[2][1] == table[2][2]
    column = table[0][0] == table[1][0] == table[2][0] or \
        table[0][1] == table[1][1] == table[2][1] or \
        table[0][2] == table[1][2] == table[2][2]
    diagonal = table[0][0] == table[1][1] == table[2][2] or \
            table[0][2] == table[1][1] == table[2][0]
    p = ['X', 'O']
    draw = table[0][0] in p and table[0][1] in p and table[0][2] in p and \
           table[1][0] in p and table[1][1] in p and table[1][2] in p and \
           table[2][0] in p and table[2][1] in p and table[1][2] in p

    if row or column or diagonal:
        os.system('cls')
        print_table()
        print(f'{name} won! well done.\U0001F389')
        return 1
    elif draw:
        print('The match ended in draw \U0001F973')
        return 1
    else:
        os.system('cls')
        print_table()
        return 0
    
# Placing the 'x' or 'o' in user chosen place
def place_it(num, person, name):
    row, col = -1, -1
    if num == 1:
        row = 0
        col = 0
    elif num == 2:
        row = 0
        col = 1
    elif num == 3:
        row = 0
        col = 2
    elif num == 4:
        row = 1
        col = 0
    elif num == 5:
        row = 1
        col = 1
    elif num == 6:
        row = 1
        col = 2
    elif num == 7:
        row = 2
        col = 0
    elif num == 8:
        row = 2
        col = 1
    elif num == 9:
        row = 2
        col = 2
    if table[row][col] == 'X' or table[row][col] == 'O':
        print('Place already choosen! Enter another place: ')
        n = int(input())
        place_it(n, person, name)
    else:
        table[row][col] = people[person]
        r = check_winner(name)
        return r

# Printing the tic tac toe table
def print_table():
    print(f'{person1}(X) and {person2}(O)')
    tic_tacTable = f'{table[0][0]}|{table[0][1]}|{table[0][2]}\n_|_|_\n\
{table[1][0]}|{table[1][1]}|{table[1][2]}\n_|_|_\n\
{table[2][0]}|{table[2][1]}|{table[2][2]}\n | |'
    print(tic_tacTable)

# playing the game
def play():
    print('Good Luck \U0001F44D')
    print_table()
    print('Enter your choices.')
    while True:
        p1 = int(input(f'{person1}: '))
        if p1 not in range(1,10):
            print('Enter a valid number!!')
            continue
        res = place_it(p1,'p1', person1)
        if res == 1:
            break
        p2 = int(input(f'{person2} : '))
        res = place_it(p2, 'p2', person2)
        if res == 1:
            break
play()
