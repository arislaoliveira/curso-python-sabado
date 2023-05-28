data = input("Digite uma data no formato dd/mm/aaaa ")

print(data)
l_data = data.split('/')
print(l_data)

data = input("Digite uma data no formato dd/mm/aaaa ")

print(data)
l_data = data.split('/')

dia, mes, ano = l_data
print(dia, mes, ano)

data = input("Digite uma data no formato dd/mm/aaaa ")

print(data)
l_data = data.split('/')

dia, mes, ano = l_data

dia = l_data[0]
mes = l_data[1]
ano = l_data[2]

print(dia, mes, ano)

#Exercícios – Estruturas de Dados - Lista 

'''
1.	Crie uma lista contendo 10 valores inteiros aleatórios, entre 1 e 20. Imprima:
    a.	O maior valor, o menor valor, a soma e a média dos valores na lista
    b.	Ordene a lista, e em seguida, a imprima em ordem crescente
    c.	Imprima a lista em ordem decrescente
    d.	Solicite ao usuário que informe um valor e imprima a quantidade de ocorrências do valor na lista. 
    Imprima uma mensagem, caso o valor não se encontre na lista
'''
import random
lista_aleatoria = random.sample(range(1,21),10)

#a)
print(max(lista_aleatoria))
print(min(lista_aleatoria))
print(sum(lista_aleatoria))
print((sum(lista_aleatoria))/10)

#b)
print(sorted(lista_aleatoria))

#c)
print(sorted(lista_aleatoria, reverse = True))

#d)
lista_usuario = int(input('Informe um valor: '))

oc = lista_aleatoria.count(lista_usuario)
if oc > 0:
    print('{} aparece {} vezes na lista.'.format(lista_usuario, oc))
else:
    print('Não há ocorrência do número {} na lista')

'''
2.	Crie duas listas com 10 valores inteiros aleatórios (escolha uma faixa qualquer). 
Crie outras duas listas: uma que contenha a soma dos elementos de mesma posição das duas listas originais, 
e outra que contenha a multiplicação dos valores de mesma posição. Imprima em seguida as 3 listas.
'''
import random

lista1 = random.sample(range(1,100),10)
lista2 = random.sample(range(1,100),10)

lista3 = [lista1[i] + lista2[i] for i in range(len(lista1))]
lista4 = [lista1[i] * lista2[i] for i in range(len(lista1))]

print(lista1)
print(lista2)
print(lista3)
print(lista4)

'''
3.	Considere a seguinte lista: [10, 20, 30, 30, 30, 40, 10, 20]
	Faça um programa que exclua todas as ocorrências do número 30 da lista
'''
lista30 = [10, 20, 30, 30, 30, 40, 10, 20]

lista_30 = [i for i in lista30 if i != 30]

print(lista_30)
'''
4.	Crie uma lista contendo 10 valores inteiros aleatórios (escolha uma faixa qualquer). 
Crie outras duas listas: uma para armazenar os valores pares da primeira lista, e outra para armazenar os valores ímpares. 
Imprima em seguida as 3 listas.
'''
import random

lista1 = random.sample(range(1,100),10)
lista2 = random.sample(range(1,100),10)

lista_par = [i for i in lista1 if i % 2 == 0]
lista_impar = [i for i in lista1 if i % 2 !=0]

print(lista1)
print(lista_par)
print(lista_impar)

'''
5.	Solicite ao usuário que digite uma data no formato DD/MM/AAAA e imprima a data por extenso. Por exemplo:
1/11/2022 – 08 de novembro de 2022
(dica: crie uma lista contendo o nome de cada mês do ano)
'''
data = input("Digite uma data no formato dd/mm/aaaa: ")

month = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

l_data = data.split('/')

dia = l_data[0]
mes = int(l_data[1])
ano = l_data[2]

print('{} de {} de {}'.format(dia, month[mes], ano))

'''
6.	Faça um programa que gere uma lista contendo 6 números aleatórios, de 1 a 60, que serão jogados na Mega-Sena. 
Em seguida, solicite ao usuário os 6 números sorteados. Imprima a lista contendo os números jogados, e a quantidade de números acertados no sorteio.
'''
import random

resultado = random.sample(range(1,60),6)
print(resultado)

usuario = input('Digite seus 6 números da Mega-Sena separados por , ')
s_usuario = usuario.split(',')
l_usuario = [int(usuario) for usuario in s_usuario]

acertos = set(l_usuario) & set(resultado)

print(sorted(l_usuario))
print(sorted(resultado))
print(len(acertos))



alunos = {3035: 'Alexandre', 8965: 'Maria', 7674: 'Carlos', 6758: 'Lucas'}

for RA, nome in alunos.items():
    print('RA:', RA, 'nome:', nome)

search = 'Alexandre'
print('Procurando Alexandre...')

for RA, nome in alunos.items():
    if (search == nome):
        print('RA:', RA, 'nome:', nome)

import requests

res = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacoes = res.json()

cotacoes['USDBRL']['bid']


# Exercícios – Manipulação de Strings 
'''
1. Solicite ao usuário que digite uma frase. Imprima:
	- o tamanho (em caracteres) da frase
	- a frase toda em maiúscula
	- a frase toda em minúscula
	- a frase na vertical(letra por letra)
	- solicite ao usuário que informe uma posição inicial e final na frase, 
    e imprima a parte da frase que se encontra dentro das posições informadas pelo usuário
	- a frase em ordem inversa
	- solicite ao usuário que informe duas palavras. Substitua, na frase informada,
    a primeira palavra informada pelo usuário, pela segunda palavra informada. 
    Armazene a nova frase em uma nova variável, e imprima o conteúdo da nova variável.
'''
frase = input('Escreva uma frase: ')

print(len(frase.replace(' ', '')))
print(frase.upper())
print(frase.lower())

for i in range(len(frase)):
    print(frase[i])

inicial = int(input('Informe uma posição inicial da frase: '))
final = int(input('Informe a parte final da frase: '))

frase_sep = frase.split(' ')

frase_nova = frase_sep[inicial:final]
frase_junta = ' '.join(frase_nova)
print(frase_junta)

print(frase[::-1])

palavra1 = input('Escreva uma palavra da frase: ')
palavra2 = input('Escreva a palavra que vai substitui-lá: ')

frase_nova1 = frase.replace(palavra1, palavra2)
print(frase_nova1)

'''
2. Solicite ao usuário que digite uma frase. Em seguida, solicite ao mesmo que digite uma palavra. 
Imprima uma mensagem informando a quantidade de vezes em que a palavra se encontra na frase 
(considere que a palavra pode estar em maiúscula ou minúscula na frase).
'''
frase = input('Escreva uma frase: ').lower()
palavra = input('Escreva uma palavra: ').lower()

qnt = frase.count(palavra)

print('A palavra {} aparece {} vezes na frase {}.'.format(palavra, qnt, frase))

'''
3. Solicite ao usuário que digite uma frase. 
Em seguida, solicite ao mesmo que informe um caractere de maneira que a frase seja dividida em partes
 de acordo com o caractere informado. Imprima na tela a frase dividida.
'''
frase = input('Digite uma frase: ')
sep = input('Informe um separador: ')

separador = frase.split(sep)

print(separador)

'''
4. Solicite ao usuário que digite uma palavra. 
Em seguida, solicite ao mesmo que informe um caractere separador, 
de maneira que o separador seja incluído na palavra, separando cada letra da palavra digitada. 
'''
palavra = input('Digite uma palavra: ')
sep = input('Informe um separador: ')

incluido = sep.join(palavra)

print(incluido)

'''
5. Solicite ao usuário que digite uma palavra e imprima uma mensagem informando
 se a palavra é ou não um palíndromo (uma palavra que se lê da mesma maneira nos dois sentidos. 
 Por exemplo: OVO, RADAR, OSSO etc.)
'''
palavra = input('Escreva uma palavra: ').lower()

if palavra == palavra[::-1]:
    print('A palavra {} é um palíndromo'.format(palavra))
else:
    print('A palavra {} não é um palíndromo'.format(palavra))
