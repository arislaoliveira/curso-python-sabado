def imprimir_linha(qtd_linhas, caractere, qtd_caracteres):
    linha = ""
    for i in range(qtd_caracteres):
        linha = linha + caractere

    for i in range(qtd_linhas):
        print(linha) 

inicio = int(input("Digite a quantidade de linhas no inicio: "))
c_inicio = input('Digite a linha inicial: ')
qtd_inicio = int(input("Digite a quantidade de caracteres no inicio: "))
fim = int(input("Digite a quantidade de linhas no fim: "))
c_final = input('Digite a linha final: ')
qtd_final = int(input("Digite a quantidade de caracteres no final: "))

imprimir_linha(inicio, c_inicio, qtd_inicio)
print("FIM DO PROGRAMA!!")
imprimir_linha(fim, c_final, qtd_final)




def imprimir_linha(qtd_linhas = 5, caractere = '*', qtd_caracteres = 15):  
  linha = ""
  for i in range(qtd_caracteres):
    linha = linha + caractere

  for i in range(qtd_linhas):
    print(linha)

imprimir_linha(3, '*', 10)
imprimir_linha(4, '@')
imprimir_linha(2)
imprimir_linha()
imprimir_linha(qtd_caracteres = 3)


def menor(a, b):
  if (a < b):
    return a
  
  return b

def maior(a, b):
  if (a > b):
    return a
  
  return b

def dobro(numero):
  numero = numero * 2
  return numero
  
x = int(input("Digite o numero: "))
y = int(input("Digite o outro numero: "))

print("Maior:", maior(x, y))
print("Menor:", menor(x, y))
print("Dobro do maior", dobro(maior(x,y)))
print("Dobro do menor", dobro(menor(x,y)))

def menor_maior(a, b):
  if a < b:
    return a, b
  
  return b, a

def menor(a, b):
  if (a < b):
    return a
  
  return b

def maior(a, b):
  if (a > b):
    return a
  
  return b

def dobro(numero):
  numero = numero * 2
  return numero
  
x = int(input("Digite o numero: "))
y = int(input("Digite o outro numero: "))

menor, maior = menor_maior(x,y)
print("Menor", menor, "Maior", maior)


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
