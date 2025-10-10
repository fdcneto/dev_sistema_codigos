# Descobrir o maior numero entre 3

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 >= numero2 and numero1 >= 3:
    print('O numero', numero1, 'é maior')
elif numero2 >= numero3:
    print('O numero', numero2, 'é maior')
else:
    print('O numero', numero3, 'é maior')