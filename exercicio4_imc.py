print("--------\n@fdcneto\n--------")
"""
Exercício 4 – Calculadora de IMC
Enunciado:
Peça ao usuário o peso (kg) e a altura (m).
Calcule o IMC = peso / (altura * altura).
Classifique o resultado com if/elif/else:
Menor que 18.5 → Abaixo do peso
De 18.5 até 24.9 → Peso normal
De 25 até 29.9 → Sobrepeso
De 30 até 39.9 → Obesidade
40 ou mais → Obesidade grave
Depois, com match-case, sugira uma categoria baseada no IMC arredondado:
IMC 18 ou 19 → Categoria Jovem Fit
IMC 20 a 24 → Categoria Saudável
IMC 25 a 29 → Categoria Plus
IMC 30 a 34 → Categoria Master
IMC 35 ou mais → Categoria Ultra
Qualquer outro → Categoria Mamute
"""

peso = float(input(f'Informe o seu peso (Kg): '))
altura = float(input(f'Informe a sua altura (m): '))

imc = peso / (altura * altura)

if imc > 0 and imc < 18.5:
    print(f'O seu IMC é {imc:.2f}\nVocê está abaixo do peso.')
elif imc <= 24.9:
    print(f'O seu IMC é {imc:.2f}\nVocê está no peso normal')
elif imc <= 29.9:
    print(f'O seu IMC é {imc:.2f}\nVocê está em sobrepeso')
elif imc <= 39.9:
    print(f'O seu IMC é {imc:.2f}\nVocê está em obesidade')
else:
    print(f'O seu IMC é {imc:.2f}\nVocê está em obesidade grave')