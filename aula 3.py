#Exercicios
#WHILE

'''
1. Faça um programa que solicite ao usuário que informe a matrícula e as três notas de um conjunto de alunos. 
O programa deverá exibir a mensagem informando se o aluno foi aprovado (média maior ou igual a 70),
exame (nota maior ou igual a 60 e menor que 70) ou reprovado (nota inferior a 60). O programa irá terminar 
quando o usuário informar uma matrícula negativa. 
'''
print('Digite um número abaixo de 0 para sair')
matricula = int(input('Matrícula: '))

while (matricula > 0):
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    nota3 = float(input('3ª nota: '))
    nota = (nota1 + nota2 + nota3) / 3
    if nota >= 70:
        print('Aluno {} aprovado com média {:.2f}!'.format(matricula, nota))
    elif 60<= nota < 70:
        print('Aluno {} em exame com média {:.2f}!'.format(matricula, nota))
    else:
        print('Aluno {} reprovado com média {:.2f}!'.format(matricula, nota))

    matricula = int(input('Matrícula: '))

print('Fim do programa!')


'''
2. Leia a idade de um número indeterminado de pessoas. Imprima:
- Quantas pessoas possuem idade acima de 50 anos
- A média de idade das pessoas
- O percentual de pessoas com idade abaixo de 40 anos
A leitura será encerrada quando o usuário informar uma idade negativa.
'''
print('Digite um número abaixo de 0 para sair')

idade1 = int(input('Digite a idade: '))
cont_50 = 0
soma = 0
cont = 0
cont_40 = 0

while (idade1 > 0 ):
    cont += 1
    soma = soma +idade1

    if(idade1 < 40):
        cont_40 += 1

    elif(idade1 > 50):
        cont_50 += 1

    idade1 = int(input('Digite a idade: '))

print('Pessoas acima de 50 anos:', cont_50)

if (cont > 0):
    x40 = (100* cont_40) / (cont)
    media = soma / cont
else:
    x40 = 0
    media = 0

print('Média das idades: %.2f ' %(media))
print('Percentual de pessoas com menos de 40 anos: %.2f %%'%(x40))


'''
3. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber: 
a ) A média do salário da população; 
b ) A média do número de filhos. 
O final da leitura de dados dar-se-á com a entrada de salários negativos. 
'''
print('Digite um número menor que 0 para sair.')
salario = float(input('Salário: '))
filhos = int(input('Quantidade de filhos: '))

cont_pop = 0
cont_sal = 0
cont_filhos = 0

while salario > 0:
    cont_pop +=1
    cont_sal += salario
    cont_filhos +=filhos

    salario = float(input('Salário: '))
    filhos = int(input('Quantidade de filhos: '))

if cont_pop > 0:
    media_sal = cont_sal / cont_pop
    media_filhos = cont_filhos / cont_pop

    print('A média dos salário da cidade é de R${:.2f}'.format(media_sal))
    print('A média de filhos na cidade é de {:.2f} filhos.'.format(media_filhos))

else:
    print('')

print('Fim do programa!')

#FOR
'''
1. Faça um programa que faça a leitura de 5 valores, e para cada valor, mostre o seu dobro na tela. 
'''
for i in range(5):
  numero = int(input("Digite o número: "))
  dobro = numero * 2
  print("Dobro: ", dobro)

'''
2. Faça um programa que leia um número e que imprima os números ímpares de 1 até o número informado. 
'''
n = int(input('Digite um número: '))

for imp in range(1, n+1,2):
    #if(imp%2 != 0):
        print(imp)

'''
3. Leia um número e imprima a tabuada de multiplicar deste número. Por exemplo, para o número 5:
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
m = int(input('Informe o número da tabuada: '))

for t in range(1,11):
    mult = m * t
    print('{} x {} = {}'.format(m, t, mult))

'''
4. Faça um programa que leia dois números inteiros e que imprima todos os números inteiros existentes entre o menor e o maior número informados.
'''
n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))

#if n1 < n2:
#    for n in range(n1, n2+1):
#        print(n)
#elif n2 < n1:
#    for n in range(n2, n1+1):
#        print(n)
#else:
#    print('Os números são iguais')

if (n1>n2):
    min = n2
    max = n1
else:
    min = n1
    max = n2

for n in range (min, max+1):
    print(n)

'''
5. Faça um programa que leia um número que calcule a soma dos números inteiros entre 1 e o número informado.
'''
num = int(input('Informe um número inteiro: '))

soma = 0
for s in range(1, num + 1):
    soma += s

print('A soma dos números inteiros entre 1 e {} é: {}'.format(num, soma))

'''
6. Faça um programa que leia um número e que calcule o fatorial deste número.
'''
num_f = int(input('Informe o número fatorial: '))

fatorial = 1

for f in range(1, num_f + 1):
    fatorial *= f

print('O resultado do número {}! é: {}'.format(num_f, fatorial))

'''
7. Faça um programa que solicite ao usuário que informe o peso, em kg, de 10 pessoas, e em seguida, exiba a média desses pesos.
'''
peso = float(input('Peso em kg: '))

c_peso = 0

for p in range(10):
    c_peso += peso
    media = c_peso / 10
    peso = float(input('Peso em kg: '))

print('A média do peso entre essas 10 pessoas é de: {} kg'.format(media))

'''
8. Faça um programa que leia o sexo e o peso de 10 pessoas, e mostre quantas pessoas do sexo masculino possuem peso entre 60 e 80 kg, 
bem como a quantidade de mulheres que possuem peso entre 50 e 70 kg.
'''
sexo = input('Informe seu sexo biológico:\n [F] Feminino\n [M] Masculino ').upper()
peso1 = float(input('Informe seu peso em kg: '))

cont_m = 0
cont_h = 0

for k in range(10):
    sexo = input('Informe seu sexo biológico:\n [F] Feminino\n [M] Masculino ').upper()
    peso1 = float(input('Informe seu peso em kg: '))
    if sexo == 'M':
        if 60 <= peso1 <= 80:
            cont_h += 1

    elif sexo == 'F':
        if 50 <= peso1 <= 70:
            cont_m += 1

print('A quantidade de homens com o peso entre 60 e 80kg é: ', cont_h)
print('A quantidade de mulheres com o peso entre 50 e 70kg é: ', cont_m)

'''
9. Faça um programa que leia a idade e peso de sete pessoas. Calcule e mostre:
	- a quantidade de pessoas com mais de 90 kg
	- a média das idades das sete pessoas
'''
peso2 = float(input('Informe o peso em kg: '))
idade = int(input('Informe a idade: '))

cont_peso2 = 0
cont_idade = 0

for z in range(7):
    if peso2 > 90:
        cont_peso2 += 1
    cont_idade += idade

    peso2 = float(input('Informe o peso em kg: '))
    idade = int(input('Informe a idade: '))

    media_idade = cont_idade / 7

print('A quantidade de pessoas com mais de 90kg é:', cont_peso2) 
print('A média das idades é: {:.2f} anos'.format(media_idade))


'''
10. Faça um programa que leia um número e que imprima na tela se o número é primo ou não.
'''

