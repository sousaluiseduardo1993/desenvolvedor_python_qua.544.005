# Tupla
dias_da_semana = (
    "Domingo",
    "Segunda-Feira",
    "Terça-Feira",
    "Quarta-Feira",
    "Quinta-Feira",
    "Sexta-Feira",
    "Sábado"
)

for dia in dias_da_semana:
    print(dia)

# NOTE: se tentar alterar a tupla, o programa dá erro. Exemplo
try:
    dias_da_semana.sort()
    for dia in dias_da_semana:
        print(dia)
except Exception as e:
    print(f"Não foi possível ordenar. {e}.")
finally:
    print("Programa encerrado.")
