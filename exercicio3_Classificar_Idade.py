print("--------\n@fdcneto\n--------")

""" Exercício 3 – Classificação de Idade
Peça a idade de uma pessoa e classifique-a:
Menor de 12 → "Criança"
De 12 a 17 → "Adolescente"
De 18 a 59 → "Adulto"
60 ou mais → "Idoso" """

idade = int(input('Digite a sua idade: '))
if idade < 0:
    print('Idade inválida!\nTente outra vez.')
elif idade < 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
elif idade <= 125:
    print('Idoso')
else:
    print('Múmia detectada 🤣🤣😂😁')
