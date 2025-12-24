'''
  Crie um programa que solicite dois números ao usuário e exiba a soma, subtração, multiplicação e divisão desses números.

  1 - Quais sao os dados de entrada necessarios?
  R - Pedir dois numeros ao usuario

  2 - O que fazer com esses dados?
  R - Fazer as 4 operacoes essenciais basicas

  3 - Quais sao as restricoes desse probelma? (Pergunta, Pesquisa)
  - REFAZER  a pergunta: Quais sao as restricoes ao se fazer  operacoes basicas na matematica em relacao aos numeros?
  
  R -   

1. Overflow - (Java)
	•	Operação (soma, subtração, multiplicação) ultrapassa o valor máximo do tipo.
	•	Ex.: int32 vai de −2³¹ a 2³¹−1
	•	Resultado pode dar wrap around ou comportamento indefinido.

2. Underflow (Java)
	•	Valor fica abaixo do mínimo representável.
	•	Comum em ponto flutuante, levando a 0 ou perda de precisão.
	•	Em inteiros, pode causar wrap around (dependendo da linguagem).

3. Divisão por zero  
	•	Pode gerar:
	•	Exceção (Java, Python)
	•	Infinity ou NaN (IEEE 754, JavaScript)

4. Perda de precisão em ponto flutuante (Java)
	•	Representação binária ≠ decimal.
	•	Ex.: 0.1 + 0.2 != 0.3
	•	Causa: padrão IEEE 754.

5. Raiz quadrada de número negativo
	•	Em reais → NaN
	•	Em complexos → válido, mas nem toda lib aceita automaticamente.

6. Exponenciação com base negativa e expoente fracionário
	•	Ex.: (-8)^(1/3)
	•	Pode falhar ou retornar NaN dependendo da implementação.

7. Logaritmo de zero ou número negativo
	•	Matemáticamente indefinido.
	•	Normalmente resulta em erro ou NaN.

8. Fatorial de número negativo
	•	Não definido matematicamente.
	•	Deve gerar erro ou exceção.

9. Tipos incompatíveis 
	•	Operações entre tipos não compatíveis.
	•	Ex.: string + int, None + número
	•	Resultado típico: TypeError.

10. Limite de memória ou recursão
	•	Ex.: fatorial recursivo de 10.000.
	•	Pode causar:
	•	StackOverflow
	•	RecursionError
	•	Falta de memória.

11. Valores NaN e Infinity
	•	Qualquer operação com NaN → NaN
	•	Infinity * 0 → NaN
	•	Propagam erros silenciosamente.

12. Inteiros “infinitos” (falsamente seguros)
	•	Linguagens como Python suportam inteiros arbitrários.
	•	Problema aparece ao:
	•	Serializar (JSON)
	•	Persistir em banco
	•	Enviar para outra linguagem.

13. Unsigned vs Signed
	•	Subtração em unsigned não gera negativo.
	•	Ex.: 0 - 1 → número gigante por wrap around.

14. Erro de arredondamento em divisão
	•	Divisão inteira:
	•	1 / 3 = 0
	•	Pode quebrar lógica se você esperava decimal.

15. Conversão implícita perigosa
	•	Ex.:
	•	JavaScript: true + 1 = 2
	•	Python: true + 1 → erro
	•	Comportamento varia brutalmente entre linguagens.


= Checar: Overflow - Estourar o limite pra cima. (Java, Swift)
          Underflow - Menor que o limite pra baixo. (Java, Swift)
          Divisão por zero - ZeroDivisionError
          Tipos incompatíveis - TypeError
          Perda de precisão em ponto flutuante - Nao guarda o valor exato

  4 - Qual o resultado esperado?
  R - Exibir o resultado das  operacoes

  5 - Qual a sequencia de passos a ser feita para chegar no resultado?

  - Pedir que o user digite um numero
  - Pedir que o user digute outro numero
  - Fazer as 4 operacoes matematicas basicas
  soma = num1 + num2
  sub = num1 = num2
  mult = num1 * num2
  div = num1 /num2

  - Exibir o resultado
'''

try:
    # 1. O código que você QUER executar
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))

    soma = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    resultado = f"Soma: {soma}, Subtração: {sub}, Multiplicação: {mult}, Divisão: {div}"


except ValueError:
    # 2. O que fazer se o usuário digitar uma LETRA (erro de valor)
    print("Erro: Você precisa digitar um número inteiro, não letras.")

except ZeroDivisionError:
    # 3. O que fazer se o usuário digitar ZERO
    print("Erro: Não é possível dividir por zero.")

except Exception as erro:
    # 4. O "Coringa": Captura qualquer outro erro que não previmos
    print(f"Ocorreu um erro inesperado: {erro}")

else:
    # 5. Opcional: Só executa se o código do 'try' der 100% CERTO
    print(f"Sucesso! O resultado é {resultado}")

finally:
    # 6. Opcional: Executa SEMPRE, dando erro ou não (bom para fechar arquivos/bancos)
    print("Operação finalizada.")



 
 



