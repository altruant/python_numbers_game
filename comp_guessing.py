from random import randint


userPrompt = 'Please enter a number between 0-100\n'
user = -1

while user < 0 or user > 100:
    user = int(input(userPrompt))
    if user < 0:
        user = int(input(userPrompt))
    elif user > 100:
        user = int(input(userPrompt))

computer = randint(0,100)
count = 0
while computer != user:
    print('The Computer guessed the number ', computer)
    count += 1
    computer = randint(0,100)
    if computer == user:
        print('The Computer guessed the number ', computer)
        print('It took the computer ', count, ' tries to guess your number')
        break
