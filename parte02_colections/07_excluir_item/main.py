# Lista de frutas
frutas = [
    "Maçã",
    "Pera",
    "Maracujá",
    "Morango",
    "Manga",
    "Melancia",
    "Goiaba"
]

# Loop principal
while True:

    # Exibe a lista com os respectivos índices
    for n, fruta in enumerate(frutas):
        print(f"Índice {n}: {fruta}")

    # Menu de opções
    print("1 - Alterar fruta")
    print("2 - Encerrar programa")
    opcao = input("Opção desejada: ").strip()

    # Verifica opção
    match opcao:
        case "1":
            indice = int(input("Informe o índice a ser excluído: "))
            del(frutas[indice])
            print("Fruta excluída com sucesso!")
            continue
        case "2":
            break
        case _:
            print("Opção inválida.")
            continue