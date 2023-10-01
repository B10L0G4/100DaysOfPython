
import random
import livesASCII
import list_words

list_word = list_words.list_word()
stages = livesASCII.stage()
logo = livesASCII.logo()
chosen_word = random.choice(list_word).lower()
display = []
chosen_error_words = ''
win = False
letter = False
live = 6

print(logo)

for letter in chosen_word:
    display += '_'

while not win:
    print(" ".join(display))
    guess = input('Escolha uma letra de A a Z: ').lower()
    chosen_error_words = chosen_error_words + guess.upper()

    if guess in display:
        letter = True
        print('letter repeated')

    for numb_words in range(0, len(chosen_word)):
        word = chosen_word[numb_words]

        if word == guess:
            display[numb_words] = word

    if guess not in chosen_word:
        live -= 1
        print(f'You chose {guess.upper()},this letter not in this word\nYou lost 1 life')


    if live == 0:
        win = True
        print('You Lose')
        print('You try write',chosen_error_words)
        print(" ".join(display))

    if '_' not in display:
        win = True
        print('You win')

    print(stages[live])


# for numb_words in range (0,len(chosen_word)):
#     word = chosen_word[numb_words]
#     display.append(chosen_word)
#     display[numb_words] = "_"
#print(display)







