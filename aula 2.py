#Exercicios
'''
1. Faça um programa que receba dois números e mostre o maior e o menor. Emita uma mensagem, caso os dois sejam iguais.
'''
a = float(input('Informe um número: '))
b = float(input('Informe outro número: '))

if a > b:
   print('{} é maior que {}'.format(a, b))
elif a < b:
   print('{} é maior que {}'.format(b, a))
else:
   print('Os números informados são iguais')


'''
2. Faça um programa que receba as duas notas de um aluno, calcule sua média, e que imprima a sua situação: 
>= 7 -> Aprovado
< 7 -> Reprovado
'''
nota_1 = float(input('Informe a 1ª nota: '))
nota_2 = float(input('Informe a 2ª nota: '))

media_1 = (nota_1 + nota_2) / 2
print(media_1)

if media_1 < 0 or media_1 > 10:
   print('Erro')
elif media_1 >= 7: 
   print('Aprovado')
else:
   print('Reprovado')

'''
3. Faça um programa que receba 3 notas de um aluno, calcule e mostre uma mensagem de acordo com sua média:
MÉDIA	MENSAGEM
>= 0 e < 3 	REPROVADO 
>= 3 e < 7 	EXAME 
>= 7 e <= 10 	APROVADO 
'''
nota1 = float(input('Informe a 1ª nota do aluno: '))
nota2 = float(input('Informe a 2ª nota do aluno: '))
nota3 = float(input('Informe a 3ª nota do aluno: '))

media = (nota1 + nota2 + nota3) / 3
print(media)

if media<0 or media>10:
   print('Erro')
elif media<3:
   print('Reprovado')
elif media <7:
   print('Exame')
else:
   print('Aprovado')
   
'''
if 3> media >=0:
   print('Reprovado') 
elif 7> media >=3:
   print('Exame')
elif 10>= media >=7:
   print('Aprovado')
'''
 
'''
4. Dados três valores X,Y,Z, verificar se eles podem ser os comprimentos dos lados de um triângulo. 
Se eles não formarem um triângulo escrever uma mensagem. 
Considerar que o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados.
'''

x = float(input('Informe o 1º lado do triângulo: '))
y = float(input('Informe o 2º lado do triângulo: '))
z = float(input('Informe o 3º lado do triângulo: '))

if x < y + z and y < x + z and z < x + y:
   print('É um triângulo')
else:
   print('Digite novamente outros valores.')

'''
5. Faça um programa que leia o sexo e a altura (H - em metros) de uma pessoa, calcule e apresente seu peso ideal utilizando as seguintes fórmulas: 
Peso ideal (homens) = (72,7 * H) – 58. 
Peso ideal (mulheres) = (62,1 * H) – 44,7
Sugestão: para identificar o sexo da pessoa, solicite ao usuário que informe 1 para homens, e 2 para mulheres
'''
sexo = input('Informe seu sexo biologico: \n'
             '[F] Feminino [M] Masculino \n').upper()
altura = float(input('Informe sua altura em metros: ').replace(',', '.'))
mulher = (62.1 * altura) - 44.7
homem = (72.7 * altura) - 58

if sexo == 'F': 
   print('Seu peso ideal é de {:.2f}kg'.format(mulher))
elif sexo == 'M':
   print('Seu peso ideal é de {:.2f}kg'.format(homem))
else:
   print('Erro')

'''
6. Construa um programa para determinar se o indivíduo está com um peso favorável. 
Essa situação é determinada através do IMC (Índice de Massa Corpórea), 
que é definida como sendo a relação entre o peso (PESO – em kg) e o quadrado da Altura (ALTURA – em m) do indivíduo. 
Ou seja,
IMC= PESO/ALTURA^2
e, a situação do peso é determinada pela tabela abaixo:
Condição	Situação
IMC abaixo de 20	Abaixo do peso
IMC de 20 até 25	Peso Normal
IMC de 25 até 30	Sobre Peso
IMC de 30 até 40	Obeso
IMC de 40 e acima	Obeso Mórbido
'''
w = float(input('Informe seu peso em quilos: ').replace(',', '.'))
h = float(input('Informe sua altura em metros: ').replace(',', '.'))

imc = (w) / (h**2)
print(imc)

if imc < 20:
   print('Abaixo do peso')
elif 20 < imc < 25:
   print('Peso Normal')
elif 25 < imc < 30:
   print('Sobrepeso')
elif 30 < imc < 40:
   print('Obeso')
else:
   print('Obeso Mórbido')

'''
Peso = float(input("digite seu peso:"))
Altura = float(input("Digite sua altura:"))

IMC = (Peso/Altura**2)

if IMC < 20:
  print("Abaixo do peso")
elif IMC < 25: 
    print("Peso Normal")
elif IMC < 30: 
    print("Sobre peso")
elif IMC < 40:
    print("Obeso")
else : 
    print("Obesidade mórbida")
'''

'''
7. Uma empresa decide dar aumento de 30% aos funcionários com salários inferiores a R$1000,00. 
Faça um programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem, 
caso o funcionário não tenha direito ao aumento.
'''
pay = float(input('Informe seu salário: ').replace(',', '.'))

if pay <=1000.00:
   in_pay = pay * 1.3
   print('Seu novo salário é R${:.2f}'.format(in_pay))
else:
   print(' ')

'''
8. Faça um programa que receba a idade de um nadador e mostre a sua categoria
IDADE	CATEGORIA
até 7 anos	INFANTIL
8 a 10 anos	JUVENIL
11 a 15 anos	ADOLESCENTE
16 a 30 anos	ADULTO
acima de 30 anos	SENIOR
'''
age = int(input('Informe sua idade: '))

if age <= 7:
   print('Categoria INFANTIL')
elif 8 >= age or age <=10:
   print('Categoria JUVENIL')
elif 11 >= age or age <= 15:
   print('Categoria ADOLESCENTE')
elif 16 >= age or age <= 30:
   print('Categoria ADULTA')
else:
   print('Categoria SENIOR')


'''
9. Faça um programa que leia a idade de uma pessoa e informe a sua classe eleitoral: 
- não eleitor (abaixo de 16 anos); 
- eleitor obrigatório (entre a faixa de 18 e menor de 65 anos); 
- eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive)
'''
idade = int(input('Informe sua idade: '))

if idade < 16:
   print('Não eleitor')
elif 16 >= idade < 18 or idade >= 65: 
   print('Voto facultativo')
else:
   print('Voto obrigatório')

'''
10. Faça um programa que leia o um número inteiro entre 1 e 7 e escreva o dia da semana correspondente. 
Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe dia da semana com esse número.
'''
week_day = int(input('Informe um número de 1 a 7: '))
week = [' ', 'Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']

if 1 <= week_day <= 7:
   week = week[week_day]
   print('O dia da semana correspondente ao número {} é {}'.format(week_day, week))
else:
   print('Não existe dia da semana para esse número')

'''
11. Faça um programa que leia um número inteiro entre 1 e 12 e escrever o mês correspondente. 
Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.
'''
month = int(input('Informe um número de 1 a 12: '))
year = [' ', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

if 1 <= month <= 12:
   year = year[month]
   print('O mês correspondente ao número {} é o mês de {}'.format(month, year))
else:
   print('Não existe mês para esse número')

'''
12. Faça um programa que solicite ao usuário que informe dois números e que exiba o seguinte menu:
1.Somar
2.Subtrair 
3.Multiplicar
4.Dividir
5.Sair
Em seguida, leia a opção escolhida e exiba o resultado de acordo com a opção.
'''
num_1 = float(input('Informe o 1º número: ').replace(',','.'))
num_2 = float(input('Informe o 2º número: ').replace(',','.'))

menu = input('[1] Somar\n'
             '[2] Subtrair\n'
             '[3] Multiplicar\n'
             '[4] Dividir\n'
             '[5] Sair\n')

if menu == '1':
   print('{} + {} = {}'.format(num_1, num_2, (num_1 + num_2)))
elif menu == '2':
   print('{} - {} = {}'.format(num_1, num_2, (num_1 - num_2)))
elif menu == '3':
   print('{} x {} = {}'.format(num_1, num_2, (num_1 * num_2)))
elif menu == '4':
   print('{} / {} = {}'.format(num_1, num_2, (num_1 / num_2)))
else:
   print('')

'''
13. Faça um programa para resolver equações de segundo grau (ax^2 + bx + c = 0)
delta = b^2 - 4*a*c
1. delta < 0 - não existe raiz real
2. delta = 0 - existe somente uma raiz real 
   x = (-b)/(2*a)
3. delta > 0 - existem duas raizes reais
   x1 = (-b + raiz de delta)/(2*a)
   x2 = (-b - raiz de delta)/(2*a)
'''
a = int(input('Informe o coeficiente a da equação: '))
b = int(input('Informe o coeficiente b da equação: '))
c = int(input('Informe o coeficiente c da equação: '))

print('{}x² + {}x + {} = 0'.format(a, b, c))

delta = b ** 2 - (4 * a * c)

if delta < 0:
   print('Não existe raiz real')
elif delta == 0:
   x = (-b) / (2*a)
   print('Apenas uma raíz satifaz esta equação, S = {:.2f}'.format(x))
else:
   x1 = (-b + (delta ** 0.5)) / (2 * a)
   x2 = (-b - (delta ** 0.5)) / (2 * a)
   print('As raízes que satisfazem esta equação são S = {:.2f}, {:.2f}'.format(x1, x2))