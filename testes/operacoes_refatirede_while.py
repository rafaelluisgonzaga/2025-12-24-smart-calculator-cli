def ler_numero(msg):
    return float(input(msg).replace(",", "."))

RESPOSTAS_CONTINUAR = {
    "s", "sim", "ss", "sii",
    "y", "yes", "yeah", "yep", "yup",
    "ok", "okay", "okey",
    "1", "true", "t",
    "continuar", "continua", "continue",
    "go", "again", "retry",
    "claro", "certeza", "bora", "vamo"
}

RESPOSTAS_SAIR = {
    "n", "nao", "não", "nn",
    "no", "nope", "nah",
    "0", "false", "f",
    "sair", "exit", "quit", "close",
    "parar", "stop", "cancel",
    "fim", "end"
}

while True:
    try:
        num1 = ler_numero("Digite um número: ")
        num2 = ler_numero("Digite outro número: ")

        print("\nResultado:")
        print(f"Soma: {num1 + num2}")
        print(f"Subtração: {num1 - num2}")
        print(f"Multiplicação: {num1 * num2}")
        print(f"Divisão: {num1 / num2}")

    except ValueError:
        print("\nErro: número inválido.")
        continue

    except ZeroDivisionError:
        print("\nErro: divisão por zero.")
        continue

    resposta = input("\nDeseja tentar novamente? ").strip().lower()

    if resposta in RESPOSTAS_CONTINUAR:
        continue
    elif resposta in RESPOSTAS_SAIR:
        print("Encerrando o programa 👋")
        break
    else:
        print("Resposta inválida, encerrando por segurança.")
        break