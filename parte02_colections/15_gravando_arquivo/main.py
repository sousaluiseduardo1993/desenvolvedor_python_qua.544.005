# Biblioteca
import os

# Limpa Terminal
os.system("cls" if os.name == "nt" else "clear")

# Loop
while True:

    print("1 - Gravar novo arquivo")
    print("2 - Abrir e ler arquivo")
    print("3 - Sair do programa")
    opcao = input("Opção desejada: ").strip()

    # Verifica a opção
    match opcao:
        case "1":
            # Informa o texto a ser gravado
            novo_texto = input("Digite aqui o seu texto: ")

            # Informa o nome do arquivo
            novo_arquivo = input("Informe o nome do arquivo: ").strip()

            # Grava o novo arquivo
            with open(f"15_gravando_arquivo/{novo_arquivo}.txt", "w", encoding="utf-8") as f:
                f.write(novo_texto)
            continue   

        case "2":
            abrir_arquivo = input("Informe o nome do .txt que deseja abrir: ").strip()

            # Abre e lê o arquivo
            with open(f"15_gravando_arquivo/{abrir_arquivo}.txt", "r", encoding="utf-8") as f:
                texto = f.read()

            # Exibe o conteúdo do arquivo na tela
            print(texto)
            continue
        case "3":
            break
        case _:
            print("Opção inválida.")
            continue