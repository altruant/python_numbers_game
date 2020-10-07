import random

with open('/usr/share/dict/words/') as infile:
    words = infile.read().splitlines()

def start_game():
    random_word = random.choice(words).lower()
    char_list= list(random_word)
    display_list = ['_'] * len(random_word)
    count = (len(random_word) + 2)

    print(f'There are {len(random_word)} letters in the random word')
    print(f'You have {count} incorrect guesses')


    guesses_made=[]

    while count > 0:
        user = input('Guess a letter: ').lower()

        if user in guesses_made:
            print('You\' already guessed that letter, try again.')
        else:
            guesses_made.append(user)

        if user in char_list:
            for index, char in enumerate(char_list):
                if char == user:
                    display_list[index] = user
            if '_' not in display_list:
                print(f'Congratulations! You guessed the word: {random_word}')
                break
            else:
                print('Good job! You\'ve guessed a letter!')
                print(''.join(display_list))
                print(guesses_made, '\n')
        else:
            count -= 1
            if count == 1:
                print(f'That was not correct, you have 1 guess remaining')
            print(f'That was not correct, you have {count} guesses remaining')
            print(''.join(display_list))
            print(guesses_made)
            if count == 0:
                print('Game over')
                break

start_game()
