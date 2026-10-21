# Dicionário
usuario = {
    'nome': "Luis Eduardo",
    'idade': 33,
    'altura': 1.72,
    'email': "sousaluiseduardo1993@gmail.com",
    'cpf': "123.456.789-12",
    'telefone': "(61) 99970-3128"
}

# Exibe valor específico
print(f"Nome: {usuario['nome']}")

print(f"E-mail: {usuario.get('email')}")

# Percorre o dicionário
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")
