'''
1.	Faça um programa contendo funções que recebam:
●	Um número inteiro e que retorne o dobro deste número
●	Dois números inteiros e que retorne o maior entre eles
●	Um número inteiro e que retorne o valor do fatorial deste número
●	Um número inteiro e positivo, que retorne a soma dos elementos inteiros existentes entre 1 e o número (inclusive)
●	Um número inteiro e que retorne True se o número for par, e False caso contrário
'''

def dobro(number_a):
  return number_a * 2

def maior(number_a, number_b):
  if (number_a > number_b):
    return number_a
  
  return number_b

def fatorial(number_a):
  fatorial = 1
  for n in range(1, number_a + 1):
    fatorial *= n
  return fatorial

def soma(number_a):
  soma = 0
  for s in range(number_a + 1):
    soma += s
  return soma

def par(number_a):
  return number_a % 2 == 0

number_a = int(input('Digite um número: '))
number_b = int(input('Digite outro número: '))

print("Dobro de {}: {}".format(number_a, dobro(number_a)))

maior = maior(number_a, number_b)
print('O maior número é', maior)

print('Fatorial de {} é {}'.format(number_a, fatorial(number_a)))

print('Soma dos números entre 1 e {} é {}'.format(number_a, soma(number_a)))

print('O número {} é par: {} '.format(number_a, par(number_a)))
