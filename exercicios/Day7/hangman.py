#TODO - Step 1 - Escolher uma palavra aleatoria de uma lista e atribuir a palavra para a variavél - chosem_word ok
#TODO - Step 2 - pedir ao usuario para escolher uma letra e atribuir a resposta a variavel guess , lowercase
#TODO - Step 3 - vericar se a letra escolhida esta contida na letra escolhida (guess) é uma das letras na palavra contida em chosen_word
import random

list_word =['barraca','barriga','burro','cachorro','carro','churrasco','corrida','corrupto','errado','erro','ferrado','ferradura','ferro',
              'garra','garrafa','gorro','horrível','irritado','jarra','serra','serrote','sorriso','terremoto','torre.bateria','cadeira',
              'camarão','coleira','coroa','faqueiro','feira','geladeira','gorila','jacaré','lírio','madeira','muro','pera','periquito',
              'picareta','pirata','pirueta','tabuleiro','tubarão','zero','armário','árvore','barba','barbatana','barco','borboleta','calor',
              'carteira','cartola','catorze','cobertor','colar','corda','formiga','garfo','guardanapo','harpa','margarida','martelo','partir',
              'porta','ralador','revólver','sorvete','tartaruga','torneira','torta','urso','verdade','verde',]

chosen_word =''
for numb_words in range (0,len(list_word)):
    random_word = random.randint(0,numb_words)
    chosen_word = list_word[random_word].lower()

guess =input('Escolha uma letra de A a Z: ').lower()

for i in chosen_word:
    if i == guess:
        print('Right')
    else:
        print('Wrong')


print(i)
print(chosen_word)