from random import randint


userPrompt = 'Please enter a number between 0-100\n'

user = int(input(userPrompt))

# computer = randint(0,100)
count = 0

lower = 0
upper = 100

while count < 8:
    count += 1
    computer = (lower + upper)//2
    print('The Computer guessed the number', computer)

    if computer == user:
        print('The Computer guessed the number', computer)
        print('It took the Computer', count, 'guesses to find your number')
        break
    elif computer > user:
        upper = computer
    elif computer < user:
        lower = computer
