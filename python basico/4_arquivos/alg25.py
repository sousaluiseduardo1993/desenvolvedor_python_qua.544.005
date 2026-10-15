
mensagem = input("Digite a mensagem: ")


with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
	arquivo.write(mensagem)

print("Mensagem salva em mensagem.txt!")
