print("--------\n@fdcneto\n--------")

''' Exercício 1 – Verificador de Número
Peça ao usuário um número inteiro e diga
se ele é positivo, negativo ou zero. '''

numero = int(input('Informe um número: '))
if numero > 0:
    print('O número', numero, 'é POSITIVO.')
elif numero < 0:
    print('O número', numero, 'é NEGATIVO.')
else:
    print('O número é ZERO.')