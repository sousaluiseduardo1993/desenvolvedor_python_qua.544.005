# declaração de variáveis

nome = input("Digite seu nome: ").strip().title()
idade = int(input("Digite sua idade: "))

# operador ternário

print(f"{nome} {'é maior de idade' if idade >=18 else 'é menor de idade'}.")