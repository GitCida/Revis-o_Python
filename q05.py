nome = input('Digite seu nome: ')
disc = input('Digite a disciplina: ')
nota = float(input('Agora digite sua nota: '))
if nota >= 0 and nota <= 10:
    if nota >= 5.5 and nota < 6:
        nota = 6
    if nota >= 6:
        status = 'aprovado'
    else:
        status = 'reprovado'
    print(f'{nome} está {status} em {disc} com nota {nota}.')
else:
    print('Nota inválida, tente novamente. ')