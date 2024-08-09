login = 'admin'
senha = '123'
login1 = input('Digite seu login: ')
senha1 = (input('Agora, digite sua senha: '))
if login1 == login and senha1 == senha:
    print(f'Olá {login}, seja bem-vindo!')
else:
    print('Login ou senha incorretos, tente novamente.')