from app.input_handler import ler_numero
from app.calculator import calcular

def run():
    while True:
        try:
            num1 = ler_numero("Digite um numero: ")
            num2 = ler_numero("Digite outro numero:")

            resultados = calcular(num1, num2)

            print("\nResultado")
            for op, valor in resultados.items():
                print(f"{op.capitalize()} : {valor:.2f}")

    
        except ValueError:
            print("\nDigite um valor valido.")
            continue
        except ZeroDivisionError:
            print("Erro:Nao é possivel divisao por zero.")
            continue

        resp = input("\nDeseja continuar? (s/n): ").strip().lower()
        if resp not in {"s", "sim", "y", "yes"}:
            break



