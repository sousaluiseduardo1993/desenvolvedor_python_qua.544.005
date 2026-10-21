# Biblioteca
import os

# Dicionário
usuario = {
    'nome': "Tomas Anderson",
    'idade': 40,
    'email': "mranderson@gmail.com",
    'telefone': "(61) 99999-9999"
}

# Limpa terminal
os.system("cls" if os.name == "nt" else "clear")

# Loop
while True:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")    

    # Informa o nome da chave
    chave_escolhida = input("Informe o nome da chave que deseja alterar: " \
    "").strip().lower()

    # Verifica se a chave é válida
    if chave_escolhida:
        usuario[chave_escolhida] = input("Informe o novo valor: ").strip()
        continue
    else:
        break