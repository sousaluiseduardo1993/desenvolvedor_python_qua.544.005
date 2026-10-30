# Biblioteca
import os

# Classe
class Pessoa:
    os.system("cls" if os.name == "nt" else "clear")
    # Contrutor
    def __init__(self,nome,idade,email,cpf):
        #Atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"E-mail: {self.email}")
        print(f"CPF: {self.cpf}")

def main():
    # Instaciar a classe
    usuario = Pessoa(nome="",idade=0,email="",cpf="")

    # Insere valores nos atributos
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: "))
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.cpf = input("Informe o CPF: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    # Exibe os atributos na tela
    usuario.exibir_dados()


if __name__ == "__main__":
    main()
