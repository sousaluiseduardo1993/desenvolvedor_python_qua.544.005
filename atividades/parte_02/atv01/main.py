# TODO: Parte 02 - Atividade 01
"""
Crie um programa que faça as seguintes operações:
- Cadastra novo usuário (nome, email, telefone, cpf)
- Lista todos os usuários
- Altera os dados de um usuário
- Exclui um usuário
- Grava os dados de todos os usuários em um arquivo JSON
- Abre um arquivo JSON e lista todos os usuários cadastrados nele
"""

# ==============================
# Bibliotecas
# ==============================
import os
import json

# ==============================
# Lista de usuários vazia
# ==============================
usuarios = []

# ==============================
# Loop principal do programa
# ==============================
while True:

    # Limpa o terminal a cada retorno ao menu
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 40)
    print("       SISTEMA DE USUÁRIOS")
    print("=" * 40)
    print("1 - Cadastrar novo usuário")
    print("2 - Exibir usuários cadastrados")
    print("3 - Alterar dados de um usuário")
    print("4 - Excluir um usuário")
    print("5 - Gravar arquivo JSON")
    print("6 - Abrir arquivo JSON")
    print("0 - Sair do programa")
    print("=" * 40)

    opcao = input("Opção desejada: ").strip()

    match opcao:

        # ==============================
        # CASE 1 - Cadastrar usuário
        # ==============================
        case "1":

            print("\n=== CADASTRO DE USUÁRIO ===")

            # Cria um novo dicionário
            usuario = {}

            # Solicita os dados do usuário
            usuario["nome"] = input(
                "Informe o nome: "
            ).strip().title()

            usuario["email"] = input(
                "Informe o e-mail: "
            ).strip().lower()

            usuario["telefone"] = input(
                "Informe o telefone: "
            ).strip()

            usuario["cpf"] = input(
                "Informe o CPF: "
            ).strip()

            # Adiciona o dicionário à lista
            usuarios.append(usuario)

            # Exibe a confirmação do cadastro
            print("\nUsuário cadastrado com sucesso!")
            print(f"Nome: {usuario['nome']}")

            input("\nPressione Enter para voltar ao menu...")

        # ==============================
        # CASE 2 - Listar usuários
        # ==============================
        case "2":

            print("\n=== USUÁRIOS CADASTRADOS ===")

            # Verifica se existem usuários na lista
            if not usuarios:

                print("Nenhum usuário cadastrado.")

            else:

                # Percorre a lista com índice e usuário
                for indice, usuario in enumerate(usuarios):

                    print(f"\nÍndice: {indice}")

                    # Exibe os dados de cada usuário
                    for chave, valor in usuario.items():

                        print(f"{chave.capitalize()}: {valor}")

                    print("-" * 40)

                print(f"Total de usuários: {len(usuarios)}")

            input("\nPressione Enter para voltar ao menu...")

        # ==============================
        # CASE 3 - Alterar usuário
        # ==============================
        case "3":

            print("\n=== ALTERAR DADOS DO USUÁRIO ===")

            # Verifica se existem usuários cadastrados
            if not usuarios:

                print("Nenhum usuário disponível para alteração.")

            else:

                # Exibe os usuários e seus índices
                for indice, usuario in enumerate(usuarios):

                    print(
                        f"Índice: {indice} | "
                        f"Nome: {usuario.get('nome', 'Sem nome')}"
                    )

                try:

                    # Solicita o índice do usuário
                    indice = int(
                        input("\nInforme o índice do usuário: ")
                    )

                    # Verifica se o índice existe
                    if 0 <= indice < len(usuarios):

                        # Seleciona o usuário
                        usuario = usuarios[indice]

                        print("\nUsuário selecionado:")
                        print(f"Nome: {usuario.get('nome', '')}")
                        print(f"E-mail: {usuario.get('email', '')}")
                        print(f"Telefone: {usuario.get('telefone', '')}")
                        print(f"CPF: {usuario.get('cpf', '')}")

                        print("\nO que deseja alterar?")
                        print("1 - Nome")
                        print("2 - E-mail")
                        print("3 - Telefone")
                        print("4 - CPF")
                        print("5 - Todos os dados")

                        alteracao = input(
                            "Opção desejada: "
                        ).strip()

                        # Seleciona o campo que será atualizado
                        match alteracao:

                            case "1":

                                usuario["nome"] = input(
                                    "Informe o novo nome: "
                                ).strip().title()

                                print("\nNome alterado com sucesso!")

                            case "2":

                                usuario["email"] = input(
                                    "Informe o novo e-mail: "
                                ).strip().lower()

                                print("\nE-mail alterado com sucesso!")

                            case "3":

                                usuario["telefone"] = input(
                                    "Informe o novo telefone: "
                                ).strip()

                                print("\nTelefone alterado com sucesso!")

                            case "4":

                                usuario["cpf"] = input(
                                    "Informe o novo CPF: "
                                ).strip()

                                print("\nCPF alterado com sucesso!")

                            case "5":

                                # Atualiza todos os campos do usuário
                                usuario["nome"] = input(
                                    "Informe o novo nome: "
                                ).strip().title()

                                usuario["email"] = input(
                                    "Informe o novo e-mail: "
                                ).strip().lower()

                                usuario["telefone"] = input(
                                    "Informe o novo telefone: "
                                ).strip()

                                usuario["cpf"] = input(
                                    "Informe o novo CPF: "
                                ).strip()

                                print(
                                    "\nTodos os dados foram alterados "
                                    "com sucesso!"
                                )

                            case _:

                                print("Opção de alteração inválida.")

                    else:

                        print("Índice inexistente.")

                except ValueError:

                    print(
                        "Entrada inválida! Informe um índice numérico."
                    )

            input("\nPressione Enter para voltar ao menu...")

        # ==============================
        # CASE 4 - Excluir usuário
        # ==============================
        case "4":

            print("\n=== EXCLUIR USUÁRIO ===")

            # Verifica se existem usuários cadastrados
            if not usuarios:

                print("Nenhum usuário disponível para exclusão.")

            else:

                # Exibe os usuários disponíveis
                for indice, usuario in enumerate(usuarios):

                    print(
                        f"Índice: {indice} | "
                        f"Nome: {usuario.get('nome', 'Sem nome')}"
                    )

                try:

                    # Solicita o índice do usuário
                    indice = int(
                        input("\nInforme o índice a ser excluído: ")
                    )

                    # Confere se o índice existe
                    if 0 <= indice < len(usuarios):

                        # Mostra o usuário selecionado
                        usuario = usuarios[indice]

                        print("\nUsuário selecionado:")
                        print(f"Nome: {usuario.get('nome', '')}")
                        print(f"E-mail: {usuario.get('email', '')}")
                        print(f"Telefone: {usuario.get('telefone', '')}")
                        print(f"CPF: {usuario.get('cpf', '')}")

                        # Solicita confirmação antes da exclusão
                        confirmar = input(
                            "\nConfirma a exclusão? (s/n): "
                        ).strip().lower()

                        if confirmar == "s":

                            # Remove o usuário da lista
                            usuario_removido = usuarios.pop(indice)

                            print(
                                "\nUsuário "
                                f"{usuario_removido.get('nome', '')} "
                                "excluído com sucesso!"
                            )

                        elif confirmar == "n":

                            print("\nExclusão cancelada.")

                        else:

                            print(
                                "\nOpção inválida. "
                                "A exclusão foi cancelada."
                            )

                    else:

                        print("Índice inexistente.")

                except ValueError:

                    print(
                        "Entrada inválida! Informe um índice numérico."
                    )

            input("\nPressione Enter para voltar ao menu...")

        # ==============================
        # CASE 5 - Gravar arquivo JSON
        # ==============================
        case "5":

            print("\n=== GRAVAR ARQUIVO JSON ===")

            # Exibe os usuários que serão gravados
            if not usuarios:

                print("A lista está vazia. O arquivo ficará sem usuários.")

            else:

                for indice, usuario in enumerate(usuarios):

                    print(f"\nUsuário {indice}")

                    for chave, valor in usuario.items():

                        print(f"{chave.capitalize()}: {valor}")

                    print("-" * 40)

            # Confirma se o usuário deseja continuar
            prosseguir = input(
                "\nDeseja gravar os dados? (s/n): "
            ).strip().lower()

            if prosseguir == "s":

                # Solicita o nome do arquivo
                arquivo = input(
                    "Informe o nome do arquivo JSON: "
                ).strip()

                # Impede o uso de um nome vazio
                if not arquivo:

                    print("O nome do arquivo não pode ficar vazio.")

                else:

                    # Evita acrescentar .json duas vezes
                    if arquivo.lower().endswith(".json"):

                        arquivo = arquivo[:-5]

                    if not arquivo:

                        print("Nome de arquivo inválido.")

                    else:

                        try:

                            # Grava os dados na pasta do programa
                            with open(
                                f"{arquivo}.json",
                                "w",
                                encoding="utf-8"
                            ) as f:

                                json.dump(
                                    usuarios,
                                    f,
                                    ensure_ascii=False,
                                    indent=4
                                )

                            print(
                                f"\nArquivo '{arquivo}.json' "
                                "gravado com sucesso!"
                            )

                        except OSError as erro:

                            print(
                                f"Não foi possível gravar o arquivo: {erro}"
                            )

            else:

                print("\nGravação cancelada.")

            input("\nPressione Enter para voltar ao menu...")

        # ==============================
        # CASE 6 - Abrir arquivo JSON
        # ==============================
        case "6":

            print("\n=== ABRIR ARQUIVO JSON ===")

            # Solicita o nome do arquivo
            abrir = input(
                "Informe o nome do arquivo JSON: "
            ).strip()

            if not abrir:

                print("O nome do arquivo não pode ficar vazio.")

            else:

                # Acrescenta a extensão, caso não tenha sido informada
                if not abrir.lower().endswith(".json"):

                    abrir += ".json"

                try:

                    # Abre o arquivo e carrega os dados
                    with open(
                        abrir,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        dados = json.load(f)

                    # Verifica se o arquivo contém uma lista de dicionários
                    if (
                        not isinstance(dados, list)
                        or not all(
                            isinstance(usuario, dict)
                            for usuario in dados
                        )
                    ):

                        print(
                            "O arquivo JSON não contém "
                            "uma lista válida de usuários."
                        )

                    else:

                        # Atualiza a lista atual com os dados do arquivo
                        usuarios = dados

                        print("\nArquivo JSON aberto com sucesso!")

                        if not usuarios:

                            print("O arquivo não contém usuários.")

                        else:

                            # Exibe os usuários carregados
                            for indice, usuario in enumerate(usuarios):

                                print(f"\nUsuário {indice}")

                                for chave, valor in usuario.items():

                                    print(
                                        f"{chave.capitalize()}: {valor}"
                                    )

                                print("-" * 40)

                            print(
                                f"Total de usuários carregados: "
                                f"{len(usuarios)}"
                            )

                except FileNotFoundError:

                    print(
                        "\nArquivo não encontrado. "
                        "Verifique o nome informado."
                    )

                except json.JSONDecodeError:

                    print(
                        "\nNão foi possível ler o arquivo. "
                        "O conteúdo JSON é inválido."
                    )

                except OSError as erro:

                    print(f"\nErro ao abrir o arquivo: {erro}")

            input("\nPressione Enter para voltar ao menu...")

        # ==============================
        # CASE 0 - Sair do programa
        # ==============================
        case "0":

            print("\nPrograma encerrado. Até mais!")
            break

        # ==============================
        # Opção inválida
        # ==============================
        case _:

            print("\nOpção inválida! Escolha uma opção do menu.")
            input("\nPressione Enter para tentar novamente...")