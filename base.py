import random

print('Hello! We\'re going to play a number guessing game!');
name = input('What is your name? \n');
color = input('What is your favorite color? \n');
print('What is the air speed of an unladen swallow?');
print('\n')
print('*************************************************************************')
print('\n')
print('Were not going to be doing that today, don\'t worry');

print('Let\'s begin: ')
guess = int(input('What number am I thinking of between 0 and 15? \n'))

computer_number = random.randrange(0,15)
count = 1
fail_statements=('Try again!\n', 'Not quite! Try again!\n', 'That wasn\'t the number I was thinking of. Maybe try another number?\n')

while count < 5:
    if guess != computer_number:
        guess = int(input(random.choice(fail_statements)))
        count += 1
    elif guess == computer_number:
        print('Congratulations!')
        break
else:
    print('You Lose!')
