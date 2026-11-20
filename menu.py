def menu_inicial():
    print('\n---- CLINDONTO ----')
    print('1 - CADASTRAR')
    print('2 - FAZER LOGIN')
    print('3 - SAIR')
    op = input('Digite sua opcao: ')
    return op


def menu_cadastro():
    print('DESEJA SE CADASTAR COMO:')
    print('\n1 - PACIENTE')
    print('2 - ADMINISTRADOR')
    op = input('Digite sua opcao: ')
    return op


def menu_categoria_adm():
    print('\n1 - GESTAO/SECRETARIA')
    print('2 - ODONTOLOGO')
    op = input('Escolha: ')
    return op


def menu_tipo_login():
    print('FAZER LOGIN COMO: ')
    print('\n1 - PACIENTE')
    print('2 - GESTAO/SECRETARIA')
    print('3 - ODONTOLOGO')
    op = input('Tipo de usuario: ')
    return op
