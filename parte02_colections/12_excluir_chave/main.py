# Dicionario
usuario = {
    'nome': "Luis Eduardo",
    'idade': 33,
    'email': "sousaluiseduardo1993@gmail.com",
    'telefone': "(61) 99970-3128",
    'endereço': "Brasília"
}

# Exibe a lista original
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# Informe a chave a ser deletada
chave_escolhida = input("Informe a chave excluir: ").strip().lower()

# Deleta a chave
del usuario[chave_escolhida]

# Re-exibe o novo dicionário
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")
