# Passagem por Valor
def levelUp(idade):
    idade += 1
    # O += é a mesma coisa que escrever
    # idade = idade + 1
    print('Idade atual:', idade)
   
def levelDown(idade):
    idade = idade -1
    #A mesma coisa de idade - 1
    return idade 

idade = 10
levelUp(idade)
print('Idade depois da levelUp:', idade)
# Necessário que receba o valor do "return" na linha 11
# se não tiver a variável (a esquerda do igual)
# você perderá o valor
idade = levelDown(idade)
print('Idade depois da levelDown:', idade)