calc = '7'
while calc != '0':
    calc = input('''
----------Calculadora----------

1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Elevar ao quadrado
0 - Sair da Calculadora

-------------------------------
Escolha o que deseja realizar: ''')
    if calc == '0':
        break
    if calc == '1':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print(f'{n1} + {n2} = {n1 + n2}')
    elif calc == '2':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print(f'{n1} - {n2} = {n1 - n2}')
    elif calc == '3':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print(f'{n1} * {n2} = {n1 * n2}')
    elif calc == '4':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print(f'{n1} / {n2} = {n1 / n2}')
    elif calc == '5':
        n1 = float(input('Digite o número: '))
        print(f'{n1}² = {n1**2}')
    else:
        print('Você digitou algo inválido, tente novamente. ')
print('Calculadora encerrada. ')