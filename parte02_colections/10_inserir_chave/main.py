# Dicionário
usuario = {
    'nome': "Fulano de Tal",
    'idade': 18,
    'email': "fulano@gmai.com"
}

# Usuário informa o nome da nova chave
nova_chave = input("Informe o nome da nova chave: ").strip().lower()

# Usuario informe o valor da nova chave
usuario[nova_chave] = input("Informe o valor da nova chave: ").strip()

# Exibe o dicionário
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")
