import json

reg_de_lances = []


def lances(name, lance):
    # lista_de_bids = {}
    # lista_de_bids ['nome'] = name
    # lista_de_bids ['lance'] = lance


    lista_de_bids = {'nome': name, 'lance': lance}
    print(f"O livro '{lista_de_bids}' foi adicionado com sucesso!")
    # reg_de_lances.append(lista_de_bids )

    try:
        with open('reg_de_lances.json', 'r') as f:
            reg_de_lances = json.load(f)

    except FileNotFoundError:
        reg_de_lances = []

    reg_de_lances.append(lista_de_bids)

    with open('reg_de_lances.json', 'w') as f:
        json.dump(reg_de_lances, f, indent=4)

    # return max(name, key=lance.get)
    return reg_de_lances

def maior_valor():
    try:
        with open('reg_de_lances.json', 'r') as f:
            reg_de_lances = json.load(f)

        valores = [valor['lance'] for valor in reg_de_lances]
        return valores
    except FileNotFoundError:
        reg_de_lances = []

