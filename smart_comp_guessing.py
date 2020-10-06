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

lower = 0
upper = 100
while computer != user:
    print('The Computer guessed the number ', computer)
    count += 1
    if computer > user:
        upper = computer
    elif computer < user:
        lower = computer
    computer = (lower+upper)//2
    if computer == user:
        count += 1
        print('The Computer guessed the number ', computer)
        print('It took the Computer', count, 'guesses to find your number')
        break
