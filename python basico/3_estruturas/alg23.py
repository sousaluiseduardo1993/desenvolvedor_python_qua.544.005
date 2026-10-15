import time


segundos=20

for restante in range(segundos, 0, -1):
		print(f"SIMULAÇÃO: {restante} segundos restantes", flush=True)
		time.sleep(1)

print("SIMULAÇÃO: contagem encerrada.")


