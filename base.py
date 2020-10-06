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
fail_statements=('Try again!', 'Not quite! Try again!', 'That wasn\'t the number I was thinking of. Maybe try another number?')

while count < 5:
    if guess != computer_number:
        count += 1
        if guess < computer_number:
            print(random.choice(fail_statements))
            guess = int(input('Your guess was too low \n'))
        elif guess > computer_number:
            print(random.choice(fail_statements))
            guess = int(input('Your guess was too high \n'))
    elif guess == computer_number:
        print('Congratulations!')
        break
else:
    print('You Lose!')
