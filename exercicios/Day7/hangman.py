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
import random

list_word =['barraca','barriga','burro','cachorro','carro','churrasco','corrida','corrupto','errado','erro','ferrado','ferradura','ferro',
              'garra','garrafa','gorro','horrivel','irritado','jarra','serra','serrote','sorriso','terremoto','torre','bateria','cadeira',
              'camarao','coleira','coroa','faqueiro','feira','geladeira','gorila','jacare','lirio','madeira','muro','pera','periquito',
              'picareta','pirata','pirueta','tabuleiro','tubarao','zero','armario','arvore','barba','barbatana','barco','borboleta','calor',
              'carteira','cartola','catorze','cobertor','colar','corda','formiga','garfo','guardanapo','harpa','margarida','martelo','partir',
              'porta','ralador','revolver','sorvete','tartaruga','torneira','torta','urso','verdade','verde',]
chosen_word = random.choice(list_word).lower()
print(chosen_word)
display = []

#simple solution
for letter in chosen_word:
    display += '_'
print(display) #word: apple output: ['_','_','_','_','_']


word_r = list(chosen_word)
while display != word_r:
    guess = input('Escolha uma letra de A a Z: ').lower()

    for numb_words in range(0, len(chosen_word)):
        word = chosen_word[numb_words]

        if word == guess:
            display[numb_words] = word

    print('display', display)
print('You win')




# for numb_words in range (0,len(chosen_word)):
#     word = chosen_word[numb_words]
#     display.append(chosen_word)
#     display[numb_words] = "_"
#print(display)





