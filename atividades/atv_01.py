# Biblioteca
import os

# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")

# Dados
nome = input("Informe seu nome: ").strip().title()
massa = float(input("Informe sua massa em kg: ").replace(",","."))
altura = float(input("Informe sua altura em metros: ").replace(",","."))

# Calcula o imc
imc = massa /(altura**2)

# Exibe o valor do imc
print(f"{nome}, seu IMC é {imc:.2f}")

# Informa o diagnóstico do usuário

if imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif imc < 25:
    print("Classificação: Peso normal.")
elif imc < 30:
    print("Classificação: Sobrepeso.")
elif imc < 35:
    print("Classificação: Obesidade grau I.")
elif imc < 40:
    print("Classificação: Obesidade grau II.")
else:
    print("Classificação: Obesidade grau III.")