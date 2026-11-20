def cadastrar_secretaria(adms):
    while True:
        cpf = input('Digite seu CPF (11 numeros): ')
        if len(cpf) != 11:
            print('CPF incorreto!')
        else:
            break
    nome = input('Digite seu nome: ').lower()
    user = input('Digite seu nome de usuario: ').lower()
    senha = input('Crie uma senha de 6 caracteres: ')
    while len(senha) != 6:
        print('A senha deve ter 6 caracteres!')
        senha = input('Crie uma senha: ')
    while True:
        num_id = int(input('Digite seu numero de identificaçao: '))
        if len(num_id) != 4:
            print('O numero de identificaçao esta incorreto!')
        else:
            break
    telefone = input('Digite seu telefone: ')
    while len(telefone) != 11:
        print('O telefone deve ter 11 caracteres!')
        telefone = input('Digite seu telefone: ')

    adms[cpf]= [nome, user, senha, num_id, telefone]
    print('O acesso da secretaria foi cadastrado com sucesso!')

def login_adm(adms):
    tentativas = 0

    while tentativas < 3:
        identificador = input('CPF ou usuario: ').lower()
        pos = -1

        for i in adms:
            if i == identificador or adms[i][2] == identificador:
                pos = i
                break

        if pos == -1:
            tentativas += 1
            print('Dados incorretos! Tentativas restantes:', 3 - tentativas)
            continue

        senha = input('Senha: ')

        if adms[pos][4] == senha:
            print('Login realizado com sucesso!')
            return pos
        else:
            tentativas += 1
            print('Dados incorretos! Tentativas restantes:', 3 - tentativas)

        print('Limite de tentativas excedidas!')

        recuperar = input('Deseja recuperar sua senha? \n1 - Sim \2 - Nao')

        if recuperar == '1':
            cpf_rec = input('Digite seu CPF: ')
            while len(cpf_rec) != 11:
                print('CPF inserido esta incorreto! Tente novamente!')
                cpf_rec = input('Digite seu CPF: ')

            telefone_rec = input('Digite seu telefone cadastrado: ')
            while len(telefone_rec) != 11:
                print('O telefone inserido esta incorreto! Tente novamente!')
                telefone_rec = input('Digite seu telefone: ')

            pos_rec = -1

            for i in adms:
                if adms[i][0] == cpf_rec and adms[i][5] == telefone_rec:
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

            adms[pos_rec][2] = novo_user
            adms[pos_rec][3] = nova_senha

            print('Sua senha nova foi cadastrada com sucesso!')

        else:
            print('Login encerrado')
