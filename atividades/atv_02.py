# Biblioteca
import os

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

# Dados
nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: "))
idade_minima = None

# Loop
while True:
    # Menu de filmes
    print(f"{'-' * 20} CINEMARK {'-' * 20}")
    print("Sala 1 - Garfield: Fora de Casa - Livre")
    print("Sala 2 - Homem-Aranha: Sem Volta para Casa - 12 anos")
    print("Sala 3 - Duna: Parte Dois - 14 anos")
    print("Sala 4 - Oppenheimer - 16 anos")
    print("Sala 5 - A Substância - 18 anos")

    # Usuário informa a sala do filme desejado
    sala = input("Sala desejada: ").strip()

    # Verifica se o usuário tem idade
    match sala:
        case "1":
            idade_minima = 0
        case "2":
            idade_minima = 12
        case "3":
            idade_minima = 14
        case "4":
            idade_minima = 16
        case "5":
            idade_minima = 18
        case _:
            print("Sala inexistente.")
            idade_minima = idade + 1

    # Verifica a idade
    if idade >= idade_minima:
        print(f"Ingresso impresso para: {nome}")
        print("Tenha um bom filme!")
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Ingresso negado para: {nome}")
        print("Você nâo possui a idade mínima para ver o filme!")
        print("Por favor, escolha outro filme: ")
        continue
