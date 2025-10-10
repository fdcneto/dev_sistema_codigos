print("--------\n@fdcneto\n--------")

""" Exercício 2 – Calculadora Simples
Peça dois números ao usuário e depois uma operação (+, -, *, /).
Mostre o resultado de acordo com a operação escolhida. """

numero1 = float(input("Informe o 1º número: "))
numero2 = float(input("Informe o 2º número: "))
print('Escolha um símbolo para a operação desejada: ')
escolha = input('[ + ] -> Adição \n[ - ] -> Subtração \n[ * ] -> Multiplicação \n[ / ] -> Divisão ').strip()

match escolha:
    case '+':
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    
    case '-':
        print(f'{numero1} - {numero2} = {numero1 - numero2}')

    case '*':
        print(f'{numero1} x {numero2} = {numero1 * numero2}')
    
    case '/':
        if numero2 == 0:
            print(f'Não é possível divisão por {numero2}')
        else:
            print(f'{numero1} ÷ {numero2} = {numero1 / numero2}')
    case _:
        print('Opção inválida!')