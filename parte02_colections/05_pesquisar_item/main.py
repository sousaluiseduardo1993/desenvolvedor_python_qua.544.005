# Lista
cidades = [
    'Taguatinga',
    'Plano Piloto',
    'Santa Maria',
    'Gama',
    'Samambaia',
    'Santa Maria',
    'Taguatinga',
    'Planaltina',
    'Plano Piloto',
    'Brazlândia',
    'Plano Piloto'
]

# Usuário informa o item a ser pesquisado
item = input("Informe a cidade a ser pesquisada: ").strip().title()

# Verifica quantas vezes o termo foi encontrado e informa na tela
print(f"{item} foi encontrado {cidades.count(item)} vezes na lista.")
