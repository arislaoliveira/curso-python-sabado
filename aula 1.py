'''
Exercícios 
Introdução à Linguagem Python
Estrutura Sequencial

1.	Leia três números inteiros e imprima a média aritmética entre esses números.
'''
num1 = int(input('Digite o 1º número inteiro: '))
num2 = int(input('Digite o 2º número inteiro: '))
num3 = int(input('Digite o 3º número inteiro: '))

media = int((num1 + num2 + num3) / 3)

print('A média aritmética entre esses 3 número é: {}'.format(media))

'''
2.	Faça um programa que receba o ano de nascimento de uma pessoa, o ano atual e imprima:
a.	A idade da pessoa no ano atual
b.	A idade que a pessoa terá em 2050
'''
nasc = int(input('Informe seu ano de nascimento: '))

#a
from datetime import datetime
hoje = datetime.now()
idade_hoje = hoje.year - nasc

print('Sua idade hoje é {} anos.'.format(idade_hoje))

#b
idade_2050 = 2050 - nasc

print('Sua idade em 2050 será {} anos.'.format(idade_2050))

'''
3.	Faça um programa que solicite ao usuário que informe os coeficientes a, b e c de uma equação de segundo grau,
e que imprima as raízes desta equação (considere que os valores informados sempre retornarão raízes reais para a equação).
'''
a = int(input('Informe o coeficiente a da equação: '))
b = int(input('Informe o coeficiente b da equação: '))
c = int(input('Informe o coeficiente c da equação: '))

print('{}x² + {}x + {} = 0'.format(a, b, c))

delta = b ** 2 - (4 * a * c)
x1 = (-b + (delta ** 0.5)) / (2 * a)
x2 = (-b - (delta ** 0.5)) / (2 * a)

print('As raízes que satisfazem esta equação são S = {:.2f}, {:.2f}'.format(x1, x2))

'''
4.	Leia um número e imprima a tabuada de multiplicar deste número. Por exemplo, para o número 5:
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
'''
x = int(input('Informe o número qual deseja a tabuada: '))

x1 = x*1
x2 = x*2
x3 = x*3
x4 = x*4
x5 = x*5
x6 = x*6
x7 = x*7
x8 = x*8
x9 = x*9
x10 = x*10

print('{} x 1 = {}\n'.format(x, x1),
      '{} x 2 = {}\n'.format(x, x2),
      '{} x 3 = {}\n'.format(x, x3),
      '{} x 4 = {}\n'.format(x, x4),
      '{} x 5 = {}\n'.format(x, x5),
      '{} x 6 = {}\n'.format(x, x6),
      '{} x 7 = {}\n'.format(x, x7),
      '{} x 8 = {}\n'.format(x, x8),
      '{} x 9 = {}\n'.format(x, x9),
      '{} x 10 = {}'.format(x, x10),)

'''
5.	Receba um número positivo, calcule e mostre:
a.	O número digitado ao quadrado
b.	O número digitado ao cubo
c.	A raiz quadrada do número digitado
d.	A raiz cúbica do número digitado.
'''
y = float(input('Informe um número positivo: '))
quadrado = int(y**2)
cubo = int(y**3)
raiz = int(y**(1/2))
raiz_cubo = int(y**(1/3))

print('{}² = {}\n'.format(y, quadrado),
      '{}³ = {}\n'.format(y, cubo),
      '√{} = {}\n'.format(y, raiz),
      '³√{} = {}'.format(y, raiz_cubo))

'''
6.	Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% para o garçom.
Faça um programa que leia o valor gasto pelo cliente e informe o valor a ser pago de gorjeta.
'''
gasto = float(input('Informe o total gasto pelo cliente: '))
gorjeta = gasto * 0.10

print('O valor a ser pago de gorjeta é R${:.2f}'.format(gorjeta))

'''
7. Faça um programa que receba um número inteiro e que imprima o antecessor, o sucessor, o dobro e a metade do número informado. 
'''
z = float(input('Informe um número: '))
ant = int(z - 1)
suc = int(z + 1)
dobro = int(z * 2)
metade = int(z / 2)

print('Antecessor: {}\n'.format(ant),
      'Sucessor: {}\n'.format(suc),
      'Dobro: {}\n'.format(dobro),
      'Metade: {}\n'.format(metade))

'''
8. Faça um programa que, tendo como dados de entrada a altura (H - em metros) de um homem, calcule e apresente seu peso ideal 
utilizando a seguinte fórmula: 
Peso ideal (P) = (72,7 * H) – 58. 
'''
h_h = float(input('Informe sua altura H em metros: '))
peso_ideal_h = (72.7 * h_h) - 58

print('Seu peso ideal é: {:.2f} kg'.format(peso_ideal_h))

'''
9. Faça o mesmo programa do item anterior, utilizando a fórmula para o cálculo do peso ideal para mulheres:
Peso ideal (P) = (62,1 * H) – 44,7
'''
h_m = float(input('Informe sua altura H em metros: '))
peso_ideal_m = (62.1 * h_m) - 44.7

print('Seu peso ideal é: {:.2f} kg'.format(peso_ideal_m))
'''
10. Faça um programa que leia duas variáveis e troque o conteúdo dessas duas variáveis.
Em seguida, imprima o valor dessas variáveis invertido. Exemplo: A = 7, B = 9. Saída: A = 9, B = 7.
'''
a = input('Digite a variável A: ')
b = input('Digite a variável B: ')

troca = a
a = b
b = troca

print('A =', a)
print('B =', b)

'''
11. Considerando uma eleição de apenas dois candidatos, faça um programa que leia o número total de eleitores, 
o número de votos do primeiro candidato e o número de votos do segundo candidato. 
Em seguida, o programa deverá apresentar o percentual de votos de cada um dos candidatos e o percentual de votos nulos.
'''
eleitores = int(input('Informe a quantidade de eleitores: '))
candidato1 = int(input('Informe a quantidade de votos no Candidato 1: '))
candidato2 = int(input('Informe a quantidade de votos no Candidato 2: '))

p_1 = (candidato1 * 100) / eleitores
p_2 = (candidato2 * 100) / eleitores
nulos = eleitores - (candidato1 + candidato2)
p_nulos = (nulos * 100) / eleitores

print('Candidato 1: {} % dos votos\n'.format(p_1),
      'Candidato 2: {} % dos votos\n'.format(p_2),
      'Nulos: {} % dos votos\n'.format(p_nulos))
