'''
  Crie um programa que solicite dois números ao usuário e exiba a soma, subtração, multiplicação e divisão desses números.

  1 - Quais sao os dados de entrada necessarios?
  R - Pedir dois numeros ao usuario

  2 - O que fazer com esses dados?
  R - Fazer as 4 operacoes essenciais basicas

  3 - Quais sao as restricoes desse probelma?
  R - 
  
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

print("Digite um numero:")
num1 = int(input())

print("Digite outro numero:")
num2 = int(input())

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print("Resultado:")
print("Soma", soma)
print("Subtracao: ", sub)
print("Multiplicacao", mult)
print("Divisao", div)

                                                                                