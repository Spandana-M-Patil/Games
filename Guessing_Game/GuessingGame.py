import random
from colorama import *
import pygame


def play_congratulations():
    pygame.mixer.init()
    pygame.mixer.music.load('congs.mp3')
    pygame.mixer.music.play()
    pygame.time.wait(4000)


def try_again():
    pygame.mixer.init()
    pygame.mixer.music.load('buzz.mp3')
    pygame.mixer.music.play()
    pygame.time.wait(800)


def random_guess():
    print(Fore.RESET + 'Welcome!! ' + Fore.MAGENTA + 'Guessing number game!')
    f = int(input(Fore.RESET + 'Enter lower bound: '))
    t = int(input('Enter higher bound: '))
    ran_choose = random.choice(range(f, t))
    # print(ran_choose)
    print('Note: You have only 5 chances to guess.All the best!!')
    i = 1
    while True:
        i += 1
        user_guess = int(input(Fore.BLUE + 'Guess a number: '))
        if user_guess == ran_choose:
            print(Fore.CYAN + 'Excellent!!')
            print(Fore.MAGENTA + f'Congratulations! You did it in {i - 1} try.' + Fore.RESET)
            play_congratulations()
            break
        elif user_guess < ran_choose:
            if i > 5:
                print(Fore.GREEN + 'Sorry! Your chances are over.')
                print(Fore.MAGENTA + f'Number is: {ran_choose}')
                break
            else:
                print(Fore.RESET + 'Try again! You guessed too small.')
                try_again()
        elif user_guess > ran_choose:
            if i > 5:
                print(Fore.GREEN + 'Sorry! You have no more chance left.')
                print(Fore.MAGENTA + f'Number is: {ran_choose}')
                break
            else:
                print(Fore.RESET + 'Try again! You guessed too large.')
                try_again()


random_guess()