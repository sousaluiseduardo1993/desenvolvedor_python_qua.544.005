# Bibliotecas
import os

# Lista de nomes
nomes = ["José", "João", "Antônio", "Francisco", "Pedro", "Carlos", "Lucas"]

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

# Loop principal
while True:
    # Exibe a lista com os respectivos índices
    for n, nome in enumerate(nomes):
        print(f"Índice {n}: {nome}")

    # Menu de opções
    print("1 - Alterar item da lista")
    print("2 - Finalizar")
    opcao = input("Opção desejada: ").strip()

    # Verifica a opção escolhida
    match opcao:
        case "1":
            # Altera o nome no índice informado
            indice = int(input("Informe o índice a ser alterado: "))
            nomes[indice] = input("Informe o novo nome: ").strip().title()

            # Limpa a tela e confirma a alteração
            os.system("cls" if os.name == "nt" else "clear")
            print("Item da lista alterado com sucesso!")
            continue

        case "2":
            # Limpa a tela e exibe a lista atualizada
            os.system("cls" if os.name == "nt" else "clear")

            for n, nome in enumerate(nomes):
                print(f"Índice {n}: {nome}")

            # Encerra o programa
            break

        case _:
            # Informa que a opção não é válida
            print("Opção inválida.")
            continue