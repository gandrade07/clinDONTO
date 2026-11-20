esp = ['ortodontia', 'implantodontia', 'endodontia', 'clinica geral',
       'dentistica', 'odontopediatria', 'protese dentaria',
       'estomatologia', 'harmonizacao orofacial', 'bucomaxilo']

def cadastrar_odonto(odonto):
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
            num_id = input('Digite seu numero de identificaçao: ')
            if len(num_id) != 4:
                print('O numero de identificaçao esta incorreto!')
            else:
                break
        while True:
            cro = input('CRO: ')
            if len(cro) != 4 and len(cro) != 5:
                print('O numero de CRO esta incorreto!')
            else:
                break
        print('\nEspecialidades: ')
        for i in range(len(esp)):
            print(i+1, '-', esp[i])
        escolha= input('Qual a sua especialidade: ')
        if escolha and int(escolha) >= 1 and int(escolha) <= len(esp):
            especialidade= esp[int(escolha) - 1]
        telefone = input('Digite seu telefone: ')
        odonto[cpf] = [nome, user, senha, num_id, cro, telefone, escolha]
        print('O acesso do(a) odontologo(a) foi cadastrado com sucesso!')

def login_odonto(odonto):
    tentativas = 0

    while tentativas < 3:
        identificador = input('CPF ou usuario: ').lower()
        pos = -1

        for i in odonto:
            if i == identificador or odonto[i][2] == identificador:
                pos = i
                break

        if pos == -1:
            tentativas += 1
            print('Dados incorretos! Tentativas restantes:', 3 - tentativas)
            continue

        senha = input('Senha: ')

        if odonto[pos][4] == senha:
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

            for i in odonto:
                if odonto[i][0] == cpf_rec and odonto[i][6] == telefone_rec:
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

            odonto[pos_rec][2] = novo_user
            odonto[pos_rec][3] = nova_senha

            print('Sua senha nova foi cadastrada com sucesso!')

        else:
            print('Login encerrado')