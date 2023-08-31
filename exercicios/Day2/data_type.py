# 'Day 2'

# escrever um programa que adicione os dígitos em um número e some todos os dígitos

digito = input("Digite um número: ")
#################################################################################
# resolvendo com for em uma linha

print('\nresolvendo com sum', sum(int(i)for i in digito)) # resolvendo com sum

#################################################################################
# resolvendo com for só sem o list
a = 0


for i in range(len(digito)):
    i = int(digito) // 10 ** i % 10
    a = a + i
    i = i / 10

print('\nUtilizando for sem list ',a,type(a), '\n')

######################################################################################################
# resolvendo com for e list

digito = list(digito) # transforma o iteravel em uma lista de caracteres
print('lista',digito)

for i in range(len(digito)): # transforma a lista em inteiros
    digito[i] = int(digito[i]) # transforma a lista em inteiros

print('\nTransformando em lista e utilizando o sum ',sum(digito)) # soma os inteiros da lista






