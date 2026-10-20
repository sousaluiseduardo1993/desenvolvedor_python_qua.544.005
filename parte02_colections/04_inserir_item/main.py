# Biblioteca
import os

# Lista Vazia
tarefas = []

# Limpa Terminal
os.system("cls" if os.name == "nt" else "clear")

# Loop
while True:
    print("1 - Inserir nova tarefa na lista")
    print("2 - Finalizar e exibir lista")
    opcao = input("Opção desejada: ").strip()

    match opcao:
        case "1":
            nova_tarefa = input("Informe a nova tarefa: ")
            tarefas.append(nova_tarefa)
            continue
        case "2":
            os.system("cls" if os.name == "nt" else "clear")

            for n, tarefa in enumerate(tarefas, start=1):
                print(f"{n}ª tarefa: {tarefa}")
            break
        case _:
            print("Opção inválida.")
