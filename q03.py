nome = input('Digite seu nome: ')
idade = int(input('Agora digite sua idade: '))
if idade <= 15:
    print(f'Olá {nome}! Você ainda não está apto a votar nas eleições.')
else:
    print(f'Olá {nome}! Você já está apto a votar nas eleições.')