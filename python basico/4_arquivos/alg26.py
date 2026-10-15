mensagem = input("Digite uma mensagem: ")

with open("mensagens.txt", "a", encoding="utf-8") as arquivo:
	arquivo.write(mensagem + "\n")
