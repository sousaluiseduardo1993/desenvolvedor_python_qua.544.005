# TODO: parte 02 atividade 01
"""
Crie um programa que faça as seguintes operações:
- Cadastra novo usuário (nome, email, telefone, cpf)
- Lista todos os usuários
- Altera os dados de um usuário
- Exclui um usuário
- Grava os dados de todos os usuários em um .json
- Abre arquivo .json e lista todos os usuários cadastrados nele
"""

# Biblioteca
import os
import json

# Lista de usuários vazia
usuarios = []

# Limpa o terminal
os.system("cls" if os.name == "nt" else "clear")

# Loop
while True:

    print("1 - Cadastrar novo usuário")
    print("2 - Exibir usuários na lista")
    print("3 - Alterar os dados do usuário")
    print("4 - Excluir um usuário")
    print("5 - Gravar novo arquivo JSON")
    print("6 - Abrir arquivo JSON")
    opcao = input("Opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            # TODO:
            pass
        case "2":
            # TODO:
            pass
        case "3":
            # TODO:
            pass
        case "4":
            # TODO:
            pass
        case "5":
            # TODO:
            pass
        case "6":
            # TODO:
            pass
        case _:
            break
