def cadastrar_paci(paci):
    while True:
        cpf = input('Digite seu CPF (11 numeros): ')
        if len(cpf) != 11:
            print('CPF incorreto!')

        else:
            break

    nome = input('Digite seu nome: ').lower()
    idade = input('Digite sua idade: ')
    user = input('Digite seu nome de usuario: ').lower()

    senha = input('Crie uma senha de 6 caracteres: ')
    while len(senha) != 6:
        print('A senha deve ter 6 caracteres!')
        senha = input('Crie uma senha: ')

    telefone = input('Digite seu telefone: ')
    while len(telefone) != 11:
        print('O telefone deve ter 11 caracteres!')
        telefone = input('Digite seu telefone: ')

    paci[cpf]= [nome, idade, user, senha, telefone]

    print('Sua conta foi cadastrado com sucesso!')

def login_paci(paci):
    tentativas = 0

    while tentativas < 3:
        identificador = input('\nCPF ou usuario: \n').lower()
        pos = -1

        for i in paci:
            if i == identificador or paci[i][3] == identificador:
                pos = i
                break

        if pos != -1:
            senha = input('Senha: \n')

            if paci[pos][4] == senha:
                print('\nLogin realizado com sucesso!')
                return pos

        tentativas += 1
        if tentativas < 3:
            print('Dados incorretos! Tentativas restantes: ', 3 - tentativas, '\n')
        else:
            print('Limite de tentativas excedidas!')

        recuperar= input('Deseja recuperar sua senha? \n1 - Sim \n2 - Nao \n')

        if recuperar == '1':
            cpf_rec= input('Digite seu CPF: ')
            while len(cpf_rec) != 11:
                print('CPF inserido esta incorreto! Tente novamente!')
                cpf_rec = input('Digite seu CPF: ')

            telefone_rec= input('Digite seu telefone cadastrado: ')
            while len(telefone_rec) != 11:
                print('O telefone inserido esta incorreto! Tente novamente!')
                telefone_rec = input('Digite seu telefone: ')

            pos_rec = -1

            for i in paci:
                if paci[i][0] == cpf_rec and paci[i][5] == telefone_rec:
                    pos_rec = i
                    break
            if pos_rec == -1:
                print('CPF ou telefone estao incorretos!')
                return

            novo_user = input('Digite seu novo nome de usuario: ')

            nova_senha = input('Digite seu nova senha de usuario: ')
            while len(nova_senha) != 6:
                print('Nova senha deve ter 6 caracteres!')
                nova_senha = input('Digite seu nova senha de usuario: ')

            paci[pos_rec][3]= novo_user
            paci[pos_rec][4]= nova_senha

            print('Sua senha nova foi cadastrada com sucesso!')

        else:
            print('Login encerrado')
