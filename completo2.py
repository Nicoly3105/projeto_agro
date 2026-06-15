from colorama import Fore, init



init()
#LOGIN
import login_funcoes
menu_login = []
login_cliente = []
login_adm = []
login_encontrado_cliente = False
login_encontrado_adm = False
tipo = None
while True:
        
    print(Fore.GREEN + """                                       ██           ██          ██         ▀██ 
▄ ▄▄ ▄▄▄     ▄▄▄  ▄ ▄▄▄   ▄▄▄ ▄▄      ▄▄▄  ▄ ▄▄▄   ▄▄▄    ▄▄▄  ▄▄▄   ▄▄▄    ██ 
 ██ ██ ██  ▄██ ██  ██ ██   ██ █        ██   ██ ██   ██  ▄██ ▀█  ██  ▀▀▄██   ██ 
 ██ ██ ██  ██▀▀▀▀  ██ ██   ██ █        ██   ██ ██   ██  ███     ██  ▄█ ██   ██ 
▄██ ██ ██▄  ▀█▄▄▀ ▄██ ██▄  ▀█▄▀▄      ▄██▄ ▄██ ██▄ ▄██▄  ▀█▄▄▀ ▄██▄ ▀█▄▀▀▄ ▄██▄ """)
    print('\033[1;32m~'*100)
    print('~'*47,'LOGIN','~'*46)
    print('~'*100)
    print('\033[m[\033[1;33m1\033[m] LOGIN')
    print('[\033[1;33m2\033[m] CADASTRAR CLIENTE NOVO')
    print('[\033[1;33m3\033[m] CADASTRAR NOVO ADM')
    print('[\033[1;33m4\033[m] SAIR\033[m')
    op = input('Digite a opção que deseja para prosseguir: ')

    if op == '1':
        tipo = login_funcoes.verificação_login()
        break

    elif op == '2':
        login_funcoes.cadastro_cliente()
            
    elif op == '3':
        login_funcoes.cadastro_adm()

    elif op == '4':
        print('\033[1;33mPROGRAMA ENCERRADO!\033[m')
        break
    else:
        print('\033[1;31mOpção inválida!\033[m')

#MENU ADM
import menuadm_funcoes

if tipo == 'adm':
    
    init()

    animais = [ {'Brinco':'002','Animal': 'Vaca','Peso': 37,'Gênero': 'Fêmea','Status': 'Grávida','Valor': 8}]
    produtos = [{'Produto': 'Coalho','Quantidade': 7,'Unidade': 'kg','Valor': 6.5}]
    leite = {'Produto':'Leite','Volume':1000,'Valor':5.5}
    historico = []

while True:
        print(Fore.GREEN + """                                                 ▀██            
▄ ▄▄ ▄▄▄     ▄▄▄  ▄ ▄▄▄   ▄▄▄ ▄▄       ▄▄▄     ▄▄ ██  ▄ ▄▄ ▄▄▄  
 ██ ██ ██  ▄██ ██  ██ ██   ██ █       ▀▀▄██  ▄██ ▀██   ██ ██ ██ 
 ██ ██ ██  ██▀▀▀▀  ██ ██   ██ █       ▄█ ██  ██▌  ██   ██ ██ ██ 
▄██ ██ ██▄  ▀█▄▄▀ ▄██ ██▄  ▀█▄▀▄      ▀█▄▀▀▄  ▀█▄▀██▄ ▄██ ██ ██▄  """)
        print('\033[m[\033[1;33m1\033[m]CADASTRAR ANIMAL\n[\033[1;33m2\033[m]VER ANIMAIS\n[\033[1;33m3\033[m]ALTERAR OU REMOVER ANIMAL\n[\033[1;33m4\033[m]CADASTRAR PRODUTO\n[\033[1;33m5\033[m]VER PRODUTOS\n[\033[1;33m6\033[m]ALTERAR OU REMOVER PRODUTO\n[\033[1;33m7\033[m]CONVERSOR DE FABRICAÇÃO\n[\033[1;33m8\033[m]PRODUÇÃO DIÁRIA\n[\033[1;33m9\033[m]HISTÓRICO DE MOVIMENTAÇÕES\n[\033[1;33m10[\033[m]RELATÓRIO GERAL\n[\033[1;33m11\033[m]SAIR')
        op_adm = int(input('Digite a opção que deseja para prosseguir: '))

        if op_adm == 1:
            menuadm_funcoes.cadastro_animais()

        elif op_adm == 2:
            menuadm_funcoes.lista_animais()

        elif op_adm == 3:
            menuadm_funcoes.alterar_remover_animal()

        elif op_adm == 4:
            while True:
                print('\033[1;32m~'*100)
                print('~'*44,'CATEGORIAS','~'*44)
                print('~\033[m'*100)
                print('[\033[1;33m1\033[m]QUEIJOS\n[\033[1;33m2\033[m]LEITE\n[\033[1;33m3\033[m]DERIVADOS\n[\033[1;33m4\033[m]PRODUTOS ARTESANAIS\n[\033[1;33m5\033[m]VOLTAR')
                op_categoria = int(input('Digite a opção que deseja para prosseguir: '))

                if op_categoria == 1:
                    menuadm_funcoes.cadas_queijo()

                elif op_categoria == 2:
                    menuadm_funcoes.cadas_leite()

                elif op_categoria == 3:
                    menuadm_funcoes.cadas_derivado()

                elif op_categoria ==4:
                    menuadm_funcoes.cadas_artesanal()

                elif op_categoria == 5:
                    login_funcoes.voltando_inicio()
                
                else:
                    print('\033[1;31mOpção inválida!\033[m')

        elif op_adm == 5:
            menuadm_funcoes.lista_produtos()

        elif op_adm == 6:
            menuadm_funcoes.alterar_remover_produto()

        elif op_adm == 7:
            print('\033[1;32m~'*100,'\033[m')
            print('\033[1;32m~'*38,'CONVERSOR DE FABRICAÇÃO','~\033[m'*39)
            print('\033[1;32m~'*100,'\033[m')
            print('[\033[1;33m1\033[m]QUEIJO\n[\033[1;33m2\033[m]DERIVADOS\n[\033[1;33m3\033[m]ARTESANAIS')
            escolha = input('Qual produto você deseja fabricar? ')

            if escolha == '1':
                menuadm_funcoes.conversor_queijo()

            elif escolha == '2':
                menuadm_funcoes.conversor_derivados()

            elif escolha == '3':
                menuadm_funcoes.conversor_artesanais()
            
            else:
                print('\033[1;31mOpção inválida!\033[m')

        elif op_adm == 8:
            menuadm_funcoes.producao_diaria()
        
        elif op_adm ==9:
            menuadm_funcoes.historico_movimentacao()

        elif op_adm == 10:
            menuadm_funcoes.relatorio_geral()

        elif op_adm == 11:
            login_funcoes.voltando_inicio()
            break
        else:
            print('\033[1;31mOpção inválida!\033[m')

#menu cliente
import menudocliente_funcoes
if tipo == 'cliente':

    compras = []
    encomendas = []
    produtos = [{'Produto':'Leite','Quantidade':15,'Unidade':'L','Valor':8}]
    animais = [{'Animal':'Porco','Quantidade':25,'Unidade:':'kg','Valor': 89}]
    leite = {'Volume': 100, 'Valor': 5}
    historico = []
    while True:
        
        print(Fore.GREEN + """                                          ▀██                    ▀██   ██                   ▄         
▄ ▄▄ ▄▄▄     ▄▄▄  ▄ ▄▄▄   ▄▄▄ ▄▄        ▄▄ ██   ▄▄▄         ▄▄▄   ██  ▄▄▄    ▄▄▄  ▄ ▄▄▄    ██     ▄▄▄ 
 ██ ██ ██  ▄██ ██  ██ ██   ██ █       ▄██ ▀██  ██ ██      ▄██ ▀█  ██   ██  ▄██ ██  ██ ██  ▀██▀  ▄██ ██
 ██ ██ ██  ██▀▀▀▀  ██ ██   ██ █       ██▌  ██  ██ ██      ███     ██   ██  ██▀▀▀▀  ██ ██   ██   ██▀▀▀▀
▄██ ██ ██▄  ▀█▄▄▀ ▄██ ██▄  ▀█▄▀▄       ▀█▄▀██▄ ▀█▄█▀       ▀█▄▄▀ ▄██▄ ▄██▄  ▀█▄▄▀ ▄██ ██▄  ▀█▄▀  ▀█▄▄▀  """)
        
        print('\033[m[\033[1;33m1\033[m] VER PRODUTOS\n[\033[1;33m2\033[m] COMPRAR PRODUTOS\n[\033[1;33m3\033[m] ENCOMENDAR PRODUTOS\n[\033[1;33m4\033[m] VER ANIMAIS\n[\033[1;33m5\033[m] COMPRAR ANIMAL\n[\033[1;33m6\033[m] ENCOMENDAR ANIMAL\n[\033[1;33m7\033[m] VER ENCOMENDAS\n[\033[1;33m8\033[m] COMPRAR LEITE\n[\033[1;33m9\033[m] RECIBO DE COMPRAS\n[\033[1;33m10\033[m] BENEFÍCIOS DO CLIENTE\n[\033[1;33m11\033[m] FORMAS DE PAGAMENTO\n[\033[1;33m12\033[m] VOLTAR')
        op_cliente = int(input('Digite a opção desejada: '))

        if op_cliente == 1:
            menudocliente_funcoes.ver_produtos()

        elif op_cliente == 2:
            menudocliente_funcoes.comprar_produto()
            
        elif op_cliente == 3:
            menudocliente_funcoes.encomendar_produto()

        elif op_cliente == 4:
            menudocliente_funcoes.ver_animais()

        elif op_cliente == 5:
            menudocliente_funcoes.comprar_animal()

        elif op_cliente == 6:
            menudocliente_funcoes.encomendar_animais()

        elif op_cliente == 7:
            menudocliente_funcoes.ver_encomendas()

        elif op_cliente == 8:
            menudocliente_funcoes.comprar_leite()

        elif op_cliente == 9:
            menudocliente_funcoes.recibo_compras()

        elif op_cliente == 10:
            menudocliente_funcoes.beneficios_cliente()

        elif op_cliente == 11:
            menudocliente_funcoes.formas_pagamento()  
        
        elif op_cliente == 12:
            login_funcoes.voltando_inicio()
            break

        else:
            print('Opção indisponível!')