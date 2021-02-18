#!/usr/bin/env python3

import random
import sys
import hashlib


def manual(num_task,user):
    print('\n')
    print('----------------------------------')
    print('\n')
    print('----------------------------------TASK-7 MANUAL----------------------------------')
    print('\n')
    print('This is a multiplayer! So make sure that you have a friend with you to play with.')
    print('You should enter numbers!(in Coordinates)')
    print('Usage:')
    print('      Enter the coordinates: > "number1"<space>"number2"')
    print('Coordinates should be from 1 to 3!')
    print('"number1" = column and "number2" = row')
    print('Note!  ROWS ARE COUNTED FROM BOTTOM')
    task7(num_task,user)


def print_board(str_list):
    print('---------')
    for index in range(0,3):
        subline = str_list[index*3:index*3+3]
        print(f'| {" ".join(subline)} |')
    print('---------')
    #range

def three_in_row(line):
    if line == 'XXX':
        return 'X'
    elif line == 'OOO':
        return 'O'
    else:
        return None

def validate_game(str_list):
    x_count = 0
    o_count = 0
    for l in str_list:
        if l == 'X':
            x_count += 1
        if l == 'O':
            o_count += 1
    if(abs(x_count - o_count ) >= 2):
        return False
    else:
        return True

def judge(str_list):
    if not validate_game(str_list):
        return 'Impossible'

    sublines = []
    x_win = False
    o_win = False
    result = None

    for index in range(0,3):
        sublines.append(''.join(str_list[index*3:index*3+3]))
        sublines.append(''.join([str_list[index], str_list[index + 3], str_list[index + 6]]))   

    sublines.append(''.join([str_list[0], str_list[4], str_list[8]]))
    sublines.append(''.join([str_list[2], str_list[4], str_list[6]]))
    
    # loop all the possible rows
    for line in sublines:
        result = three_in_row(line)
        if result == 'X':
          x_win = True
        if result == 'O':
          o_win = True

    if x_win and o_win:
        return 'Impossible'
    elif x_win or o_win:
        return 'X wins' if x_win else 'O wins'
    elif '_' in str_list:
        return 'Game not finished'
    else:
        return 'Draw'

def is_int(val):
    try:
        _ = int(val)
    except ValueError:
        return False
    return True

def verify_move(current, move_input, player):
  move = move_input.split(' ')
  for t in move:
    if not is_int(t):
      return False, 'You should enter numbers!'
    if int(t) > 3 or int(t) < 1:
      return False, 'Coordinates should be from 1 to 3!'
  
  # find current location
  move_int = [int(move[0]), int(move[1])]
  loc = 3* (3 - move_int[1]) + move_int[0] - 1
  loc_state = current[loc]
  if loc_state != '_':
    return False, 'This cell is occupied! Choose another one!'
  else:
    current[loc] = player
    return True, current

def init_game():
    return list('_________')

def user_input(game_state, player):
    valid_move = False
    while(not valid_move):
        move_input = input("Enter the coordinates: > ")
        valid,result = verify_move(game_state, move_input, player)
        if not valid:
            print(result)
            valid_move = False
        else:
            game_state = result
            valid_move = True
    return game_state

def game_begins():
    heading = "** GAMBLING WITH THE SECRET NUMBER **"
    print("*" * len(heading))
    print(heading)
    print("*" * len(heading))


def game(num_task,user):
    global secret_number
    guess = int(input(user+" ,Please enter your guess: "))
    if (guess == secret_number):
        for i in range(5):
            print (user+" ,you are amazing..your guess is absolutely right")
    elif(guess != secret_number):
        print (user+" ,Your guess is wrong")
        print(user+' ,now its task time!')
        if (num_task==1):
            task1(num_task,user)
        if(num_task==2):
            task2(num_task,user)
        if(num_task==3):
            task3(num_task,user)
        if(num_task==4):
            task4(num_task,user)
        if(num_task==5):
            task5(num_task,user)
        if(num_task==6):
            task6(num_task,user)
        if(num_task==7):
            manual(num_task,user)
        else:
            sys.exit()


def game1(num_task):
    user = input('Enter your name:')
    print(user+' ,let us start the game....')
    global secret_number
    game(num_task,user)
            
            
    
#TASK 1
def task1(num_task,user):
    print('\n')
    print('----------------------------------')
    print('\n')
    print('TASK 1')
    numbers = []
    for charater in user:
        numbers.append(ord(charater))
    for number_1 in numbers:
        print(hex(number_1))
    print('Guess the hidden word')
    word=input('>')
    if (word == user):      
        print(user+"  .YES, you have successfully completed the task ")
        print('lets try again')
        game(num_task,user)
        
    else:
        print('Task failed, better luck next time.')
        num_task = num_task+1
        task2(num_task,user)
                
##TASK 2
def task2(num_task,user):
    print('\n')
    print('----------------------------------')
    print('\n')        
    print('TASK 2')
    a=input('Print the hidden word- (16,25,20,8,15,14):')
    a1='python'
    if (a == a1):
        print(user+" ,YES the word is right, you have successfully completed the task ")
        game(num_task,user)
    else:
        print('Task failed, better luck next time.')
        num_task = num_task+1
        task3(num_task,user)
                    
#TASK 3
def task3(num_task,user):
    print('\n')
    print('----------------------------------')
    print('\n')
    print('TASK 3')
    num_1 = int(input("Please Enter the Number to Check for Armstrong: "))
    sum = 0
    temp = num_1
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num_1 == sum:
        print(user+" ,YES it is an armstrong no., you have successfully completed the task ")
        game(num_task,user)
    else:
        print('Task failed, better luck next time.')
        num_task = num_task+1
        task4(num_task,user)

#TASK 4
def task4(num_task,user):
    print('\n')
    print('----------------------------------')
    print('\n')
    print('TASK 4')
    name_hash = hashlib.sha256(user.encode('utf-8')).hexdigest()
    print('Find out the hidden string!!')
    print(name_hash)
    checker = input('>')
    if(user == checker):
        print('YES!! You have successfully completed the task')
        game(num_task,user)
    else:
        print('Task failed, better luck next time.')
        num_task = num_task+1
        task5(num_task,user)
#Task 5
def task5(num_task,user):
    print('\n')
    print('----------------------------------')
    print('\n')
    print('Task 5')
    rows = 8
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*")

        print(" ")
    print('Can you see an amazing pattern?')
    a=int(input('Enter the number of rows in this pattern: '))
    if (a == rows):
        print(user+' ,yes,you have successfully completed the task')
        game(num_task,user)
    else:
        print('Task failed, better luck next time.')
        num_task = num_task+1
        task6(num_task,user)
#Task 6
def task6(num_task,user):
    print('\n')
    print('----------------------------------')
    print('\n')
    print('Task 6')
    print('who created python?')
    a='Monty Python'
    b='Guido van Rossum'
    c='Kaustubh'
    print('option 1=',a)
    print('option 2=',b)
    print('option 3=',c)
    ur_ans = int(input('enter an option(1/2/3):'))
    org_ans = 2
    if(ur_ans == org_ans):
        print('Excellent!!you even knew this!!,you have successfully completed the task' +user)
        game(num_task,user)
    else:
        print('Task failed, better luck next time.')
        num_task=num_task+1
        manual(num_task,user)
#task7
def task7(num_task,user):
    print('\n')
    print('----------------------------------')
    print('\n')
    print('TASK 7')
#print(secret_number)
    game_over = False
    players = ['X', 'O']
    rounds = 0 
    game_state = init_game()

    while(not game_over):
        print_board(game_state)
        game_state = user_input(game_state, players[rounds % 2])
        out = judge(game_state)
        rounds += 1
        if 'wins' in out or out == 'Draw':
            print_board(game_state)
            print(out)
            game_over = True
    restart_task7=input('Do you want to play again this task?(Y/n):')
    if restart_task7.lower == 'y':
        manual(num_task,user)
    task8(num_task,user)
#Task 8
def task8(num_task,user):
    global secret_number
    print('\n')
    print('----------------------------------')
    print('\n')
    print('Thank you '+user)
    print("Aren't you curious to know the answer?" )
    print(secret_number,'is the mysterious secret number')
    print('Good bye '+user)
    task9(num_task,user)
#end of the program
def task9(num_task,user):
    print('\n')
    print('----------------------------------')
    print('\n')
    print('exiting game...')
    sys.exit()
    
num_task = 1
game_begins()
secret_number = random.randrange(1, 5)
game1(num_task)
