import random


# map = [row1]
# print(map)



# position = input("Where do you want to put the treasure? ")
row1 = ['irritado','jarra','serra']
row1 = random.choice(row1)
guess =input('Escolha uma letra de A a Z: ').lower()
display = []



for numb_words in range (0,len(row1)):
        chosen_word = row1[numb_words]
        display.append(chosen_word)
        display[numb_words] = "_"
print('display', display)
if chosen_word == guess:
    display[numb_words] = guess
    print('Right')
else:
    print('Wrong')
print(row1)
print('display',display)


# print(f"{row1}")
# linha = row1[0]
#
# print(linha)




# linha = "X"


# position = list(position)

# linha = linha -1



