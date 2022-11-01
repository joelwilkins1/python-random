import random

print('\n####Welcome to the guessing game ####')
Name = input('\n Hello Player, what is your name? ')
print('\nHello', Name, '!')
upper = int(input('\nWhat is the upper range you require?: '))
number = random.randint(1, upper)
print(number)
guess = int(input('Please enter your guess: '))
if guess == number:
    print('Correct')
elif guess != number:
    print('Unlucky!')
