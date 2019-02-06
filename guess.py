import random

random_number = random.randint(1, 10)

while True:
    guess = input('Pick a number from 1 to 10 : ')
    guess = int(guess)
    if (guess < random_number):
        print('Too Low')
    elif (guess > random_number):
        print('Too High')
    elif (guess == random_number):
        print('You WON')
        play_again = input('Do you want to play again? (y/n)')
        if play_again == 'y':
            random_number = random.randint(1, 10)
        else:
            print('Thank you for playing')
            break
    else:
        print('Something wrong happened')

