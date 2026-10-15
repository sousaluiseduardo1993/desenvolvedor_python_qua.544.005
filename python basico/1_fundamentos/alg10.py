nome = input("Digite o seu nome:")
idade = int(input("Digite a sua idade:"))

if idade >= 18:
     r = (f"O {nome} é maior de idade\n")
else:
     r= (f"O {nome} é menor de idade\n")

print(r)
print("Programa encerrado com sucesso...")

