import json

cidade1 = input('Digite o nome da cidade: ')

visitas = input("Digite a quantidade de visitas:")

lista_de_cidades = eval("['{}']".format(input("Digite a lista de cidades, separadas por vírgula: ").replace(', ', "','")))



reg_de_viagem = [{}]

def add_nova_viagem(cidade1, visitas, lista_de_cidades):
    nova_viagem = {}
    nova_viagem['cidade']= cidade1
    nova_viagem['visitas']= visitas
    nova_viagem['cidades_visitadas']= lista_de_cidades


    try:
        with open('reg_de_viagem.json', 'r') as f:
            reg_de_viagem = json.load(f)
    except FileNotFoundError:
        reg_de_viagem = []

    reg_de_viagem.append(nova_viagem)

    with open('reg_de_viagem.json', 'w') as f:
        json.dump(reg_de_viagem, f, indent=4)

    return reg_de_viagem


add_nova_viagem(cidade1, visitas, lista_de_cidades)
print(f"Eu estive no {reg_de_viagem[-1]['cidade']} {reg_de_viagem[-1]['visitas']} vezes." )
print(f"Minha cidade favorita foi {reg_de_viagem[-1]['cidades_visitadas'][0]} ")
