import menu as mn
import paciente as pc
import administrador as adm
import odonto as odt

paci= {}
adms= {}
odonto= {}

esp = ['ortodontia', 'implantodontia', 'endodontia', 'clinica geral',
       'dentistica', 'odontopediatria', 'protese dentaria',
       'estomatologia', 'harmonizacao orofacial', 'bucomaxilo']

while True:
    op = mn.menu_inicial()

    if op == '1':
        tipo = mn.menu_cadastro()
        if tipo == '1':
            pc.cadastrar_paci(paci)
        elif tipo == '2':
            categoria = mn.menu_categoria_adm()
            if categoria == '1':
                adm.cadastrar_secretaria(adms)
            elif categoria == '2':
                odt.cadastrar_odonto(odt)
            else:
                print('Opcao invalida!')
        else:
            print('Opcao invalida!')

    elif op == '2':
        tipo = mn.menu_tipo_login()
        if tipo in ['1', '2', '3']:
            pc.login_paci(paci)
            adm.login_adm(adms)
            odt.login_odonto(odonto)
        else:
            print('Opcao invalida!')

    elif op == '3':
        print('Encerrando o sistema ClinDONTO...')
        break

    else:
        print('Opcao invalida!')

