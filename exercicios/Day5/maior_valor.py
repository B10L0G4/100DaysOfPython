student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0
for item in student_scores:
    item = int(item) # não esquecer de converter o numero , caso contrario ele dara erro pois tipo lista nao consegue iterar sobre integer
    if item > max:
        max = item # é necessario armazenar em uma nova variavel o maior valor conforme encontrado , caso contrario  ira ficae buscando sempre o mesmo item da lista , ou seja eles serão sempre igauis
print(max) # a impressao precisa ficar fora do loop para imprir apenas a ultima opção desejada , caso contrario todos os itens serão mostrados

#precisei da ajuda do stacloverflow aqui , pois nao consegui visualizar o segundo armazenamento de valores.

# entender melhor o in e range , pelo menos


