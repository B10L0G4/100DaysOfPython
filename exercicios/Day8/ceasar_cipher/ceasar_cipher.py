alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#
#

def encrypt(text_func,shift_func):
    # text_func = text_func.replace(" ", "")
    cipher = ''
    for letter in text_func.strip(' '):
        position = alphabet.index(letter)
        shift_position = position + shift_func
        if shift_position > 25:
            alphabet.sort(reverse=True)
            position = len(alphabet)-1
            shift_position = position - shift_func
        new = alphabet[shift_position]
        cipher += new
        alphabet.sort(reverse=False)
    print(f'The encoded text is {cipher}')


def decrypt(text_func,shift_func):
    decipher = ''
    for letter in text_func:
        position = alphabet.index(letter)
        shift_position = position - shift_func
        new = alphabet[shift_position]
        decipher += new
    print(f'The encoded text is {decipher}')


if direction == 'encode':
    encrypt(text_func=text,shift_func=shift)
elif direction == 'decode':
    decrypt(text_func=text, shift_func=shift)


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.



# for index, value in enumerate(my_list):
#     if value in texto:
#       my_list[index] = my_list[shift]
#
# print(my_list)
# for l in texto:
#     display += l
#
# for index, value in enumerate(my_list):
#     my_list[index] = my_list[index]
# print(my_list)
#
# for index, value in enumerate(display):
#     if value in display:
#         display[index] = my_list[shift]




#     for letter in range(len(texto)):
#         if l in a:
#             word = texto[letter]
#             display[letter] = a[letter]
# print(display)



