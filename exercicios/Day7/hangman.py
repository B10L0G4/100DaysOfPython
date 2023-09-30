#TODO - Step 1 - Escolher uma palavra aleatoria de uma lista e atribuir a palavra para a variavél - chosem_word ok
#TODO - Step 2 - pedir ao usuario para escolher uma letra e atribuir a resposta a variavel guess , lowercase
#TODO - Step 3 - vericar se a letra escolhida esta contida na letra escolhida (guess) é uma das letras na palavra contida em chosen_word
#TODO - Step 4 - Crear uma lista vazia chamada display.( para cada letra na variavel chosen_words deve ser add "_"
# ao display)(se a palavra tiver 5 letras o display devera ter 5 espaços no display - ok
#TODO - Step 5 - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]. ok
#TODO - Step 6 - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3. ok
#TODO - step 7 -  Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
#TODO - step 8: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
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
    print(chosen_error_words)
    if guess in display:
        letter = True
        print('letter repeated')

    print('acert',live)
    for numb_words in range(0, len(chosen_word)):
        word = chosen_word[numb_words]


        if word == guess:
            display[numb_words] = word

    if guess not in chosen_word:
        live -= 1
        print(f'You chose {guess.upper()}, this letter not in this word\n You lost 1 life')


    if live == 0:
        win = True
        print('You Lose')
        print('You try write',chosen_error_words)

    if '_' not in display:
        win = True
        print('You win')

    print(stages[live])










# for numb_words in range (0,len(chosen_word)):
#     word = chosen_word[numb_words]
#     display.append(chosen_word)
#     display[numb_words] = "_"
#print(display)







