from modulo import limpar, peso_astro


def main():
    astros = {
        'Mercurio': 3.70,
        'Venus': 8.87,
        'Terra': 9.81,
        'Lua': 1.62,
        'Marte': 3.71,
        'Jupiter': 24.79,
        'Saturno': 10.44,
        'Urano': 8.69,
        'Netuno': 11.15,
        'Plutao': 0.62
    }

    limpar()

    massa = float(input("Informe sua massa em kg: ").replace(",", "."))

    for chave, valor in astros.items():
        print(f"\n{chave.upper()}:")
        print(f"Gravidade: {valor} m/s²")
        print(f"Peso: {peso_astro(massa, valor):.2f} N")
        print("-" * 40)


if __name__ == "__main__":
    main()