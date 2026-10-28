# Biblioteca
import math
import os

# Função
def raiz(n):
    return math.sqrt(n)

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# Algoritmo principal
def main():
    limpar()
    n = int(input("Informe um número inteiro: "))
    print(f"Raíz de {n} é {raiz(n)}.")

# Algoritmo principal protegido
if __name__ == "__main__":
    main
