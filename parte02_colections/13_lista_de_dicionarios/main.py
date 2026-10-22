# Lista de dicionários
usuarios = [
    {
        'nome': "Luis Eduardo",
        'idade': 33,
        'email': "sousaluiseduardo1993@gmail.com"
    },
    {
        'nome': "Roberto Carlos",
        'idade': 20,
        'email': "roberto123@gmail.com"
    },
    {
        'nome': "Cristiano Ronaldo",
        'idade': 30,
        'email': "cristiano123@gmail.com"
    }
]

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")