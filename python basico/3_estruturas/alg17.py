#DADOS
#LER O NOME DO ALUNO
#LER O NUMERO DA TURMA
# LER TRÊS NOTAS

#ENTRADA
# Calcula a media
#Verificar Status (média >= 70 é aprovado)

#SAÍDA
#MOSTRAR A SOMA DAS NOTAS
#MOSTRAR A MÉDIA DAS NOTAS
#MOSTRAR SE FOI "APROVADO" OU "REPROVADO"

'''------------------------------------'''

nome = str(input("Digite seu nome: "))
turma = str(input("Digite sua turma: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 70:
    print(f"{nome}, você foi aprovado!")
else:
    print(f"{nome}, você foi reprovado.")

print(f"Média: {media:.2f}")
print(f"Total das notas: {nota1 + nota2 + nota3}")