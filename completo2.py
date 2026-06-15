from colorama import Fore, init

init()

print(Fore.GREEN + """                                                     ████▄            ████▄           ████▄            ████        
████▀▀██▀███▄▄  ▄▄██▀▀████████▀▀███▄▄ ████   ▄▄▄▄    ███▀ ████▀▀███▄▄ ███▀  ▄▄██▀▀███████▀  ▄▄██▀▀▀███▀████        
▓▓▓▓  ▓▓  ▓▓▓▓▌▐██▓▄▄▄▓▓▓▓▓▓▓▓   ▓▓▓▓▌▓▓▓▓   ▓▓▓▓    ▄▄▓█ ▓▓▓▓   ▓▓▓▓▌▄▄▓█ ▐██▓       ▄▄▓█ ▐██▓   ▐▓▓▓ ▐▓▓▓        
▐▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒   ▄▄▄▄▐▒▒▒   ▒▒▒▒▒▒▒▒▒   ▒▒▒▒    ▐▒▒▒ ▐▒▒▒   ▒▒▒▒▒▐▒▒▒ ▒▒▒▒   ▄▄▄▄▐▒▒▒ ▒▒▒▒   ▐▒▒▒▌▐▒▒▒        
▐░░░  ░░  ░░░░░░░░░   ░░░░▐░░░   ░░░░░▐░░░   ░░░░    ▐░░░ ▐░░░   ░░░░░▐░░░ ░░░░   ░░░░▐░░░ ░░░░▌  ▐░░░▌▐░░░   ░░░░░
▀▀▀▀      ████▌ ▀▀▀▀▀▀████▀▀▀▀   ████▌ ▀▀▀▀▀▀████    ▀▀███▀▀▀▀   ████▌▀▀███ ▀▀▀▀▀▀████▀▀███ ▀▀▀▀▀▀▀▀▀▀▀▀▀███▄▄██▀▀ """)

#LOGIN
import login_funcoes
menu_login = []
login_cliente = []
login_adm = []
login_encontrado_cliente = False
login_encontrado_adm = False

while True:
    print('\033[1;32m~'*100)
    print('~'*47,'MENU','~'*47)
    print('~'*100)
    print('\033[m[\033[1;33m1\033[m]LOGIN \n[\033[1;33m2\033[m]CADASTRAR CLIENTE NOVO\n[\033[1;33m3\033[m]CADASTRAR NOVO ADM\n[\033[1;33m4\033[m]SAIR')
    op_login = int(input('Digite a opção que deseja para prosseguir: '))

    if op_login == 1:
        login_funcoes.verificação_login()

    elif op_login == 2:
        login_funcoes.cadastro_cliente()
            
    elif op_login == 3:
        login_funcoes.cadastro_adm()
    elif op_login == 4:
        print('\033[1;34mPROGRAMA ENCERRADO!\033[m')
        break

#MENU ADM
import menuadm_funcoes
if login_encontrado_adm == True:
    from colorama import Fore, init
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
        print('\033[m[\033[1;33m1\033[m]CADASTRAR ANIMAL\n[\033[1;33m2\033[m]VER ANIMAIS\n[\033[1;33m3\033[m]ALTERAR OU REMOVER ANIMAL\n[\033[1;33m4\033[m]CADASTRAR PRODUTO\n[\033[1;33m5\033[m]VER PRODUTOS\n[\033[1;33m6\033[m]ALTERAR OU REMOVER PRODUTO\n[\033[1;33m7\033[m]CONVERSOR DE FABRICAÇÃO\n[\033[1;33m8\033[m]PRODUÇÃO DIÁRIA\n[\033[1;33m9\033[m]SAIR')
        op_adm = int(input('Digite a opção que deseja para prosseguir: '))

        if op_adm == 1:
            menuadm_funcoes.cadastro_animais()

        elif op_adm == 2:
            menuadm_funcoes.lista_animais()
        elif op_adm == 3:
            print('\033[1;32m~\033[m'*100)
            print('[\033[1;33m1\033[m]ALTERAR\n[\033[1;33m2\033[m]REMOVER') 
            remover_alterar = input('Digite a opção que você deseja: ')
            if remover_alterar == '1':
                alteracao = input('Qual animal você deseja alterar? ').capitalize()
                for i in animais:
                    if i[0] == alteracao:
                            print(i)
                            print('\033[1;32m~\033[m'*100)
                            print('[\033[1;33m1\033[m]TIPO ANIMAL\n[\033[1;33m2\033[m]PESO\n[\033[1;33m3\033[m]GÊNERO\n[\033[1;33m4\033[m]STATUS\n[\033[1;33m5\033[m]VALOR')
                            escolha_alteracao = input('Digite o que você deseja alterar: ')
                            if escolha_alteracao == '1':
                                tipo_alteracao = input(f'Digite o nome que você deseja substituir no lugar de {i[0]}: ')
                                i[0] = tipo_alteracao
                                print('Animal alterado com sucesso!')
                                break
                            elif escolha_alteracao == '2':
                                peso_alteracao = float(input(f'Digite o peso que você deseja substituir no lugar de {i[1]}:'))
                                i[1] = peso_alteracao
                                print('Animal alterado com sucesso!')
                                break
                            elif escolha_alteracao == '3':
                                genero_alteracao = input(f'Digite o gênero que você deseja substituir no lugar de {i[2]}: ')
                                i[2] = genero_alteracao
                                print('Animal alterado com sucesso!')
                                break
                            elif escolha_alteracao == '4':
                                status_alteracao = input(f'Digite o status que você deseja substituir no lugar de {i[3]}: ')
                                i[3] = status_alteracao
                                print('Animal alterado com sucesso!')
                                break
                            elif escolha_alteracao == '5':
                                valor_alteracao = float(input(f'Digite o valor que você deseja substituir no lugar de {i[4]}: '))
                                i[4] = valor_alteracao
                                print('Animal alterado com sucesso!')
                                break
                            else:
                                print('Animal não encontrado!')
            elif remover_alterar == '2':
                remover = input('Digite o animal que você deseja remover: ').capitalize()
                for i in animais:
                    if i[0] == remover:
                        print(i)
                        print('\033[1;32m~\033[m'*100)
                        animais.remove(i)
                        print('Animal removido com sucesso!')
                        break
                    else:
                        print('Animal não encontrado!')
  
        elif op_adm == 4:
            while True:
                print('\033[1;32m~'*100)
                print('~'*44,'CATEGORIAS','~'*44)
                print('~\033[m'*100)
                print('[\033[1;33m1\033[m]QUEIJOS\n[\033[1;33m2\033[m]LEITE\n[\033[1;33m3\033[m]DERIVADOS\n[\033[1;33m4\033[m]PRODUTOS PARA VENDA EM LOTE\n[\033[1;33m5\033[m]PRODUTOS ARTESANAIS\n[\033[1;33m6\033[m]VOLTAR')
                op_categoria = int(input('Digite a opção que deseja para prosseguir: '))
                if op_categoria == 1:
                        produto = input('Digite o tipo de queijo que você deseja cadastrar: ').capitalize()
                        while True:
                            peso = float(input('Digite o peso do produto: '))
                            if peso <= 0 :
                                print('Esse peso é inválido para o produto, tente novamente!')
                                continue
                            else:
                                break
                        unidade = input('Qual seria a unidade de medida desse produto? ')
                        while True:
                            valor = float(input('Digite o valor do produto: '))
                            if valor <= 0 :
                                    print('Esse valor é inválido para o produto, tente novamente!')
                                    continue
                            else:
                                break 
                        produtos.append([produto,peso,unidade,valor])
                        
                elif op_categoria == 2:
                        while True:
                            volume = float(input('Digite o volume do leite em litros: '))
                            if volume <= 0 :
                                print('Esse volume é inválido para o produto, tente novamente!')
                                continue
                            else:
                                break
                        while True:
                            valor = float(input('Digite o valor do produto: '))
                            if valor <= 0 :
                                    print('Esse valor é inválido para o produto, tente novamente!')
                                    continue
                            else:
                                break 
                        leite.append(volume,valor)

                elif op_categoria == 3:
                        produto = input('Digite o tipo de derivado que você deseja cadastrar: ').capitalize()
                        while True:
                            quantidade = float(input('Digite a quantidade do produto: '))
                            if quantidade <= 0 :
                                print('Essa quantidade é inválida para o produto, tente novamente!')
                                continue
                            else:
                                break
                        unidade = input('Qual seria a unidade de medida desse produto? ')
                        while True:
                            valor = float(input('Digite o valor do produto: '))
                            if valor <= 0 :
                                    print('Esse valor é inválido para o produto, tente novamente!')
                                    continue
                            else:
                                break 
                        produtos.append([produto,quantidade,unidade,valor])
                elif op_categoria == 3:
                        produto = input('Digite o tipo de derivado que você deseja cadastrar: ').capitalize()
                        while True:
                            quantidade = float(input('Digite a quantidade do produto: '))
                            if quantidade <= 0 :
                                print('Essa quantidade é inválida para o produto, tente novamente!')
                                continue
                            else:
                                break
                        unidade = input('Qual seria a unidade de medida desse produto? ')
                        while True:
                            valor = float(input('Digite o valor do produto: '))
                            if valor <= 0 :
                                    print('Esse valor é inválido para o produto, tente novamente!')
                                    continue
                            else:
                                break 
                        produtos.append([produto,quantidade,unidade,valor])

                elif op_categoria == 4:
                        produto = input('Digite o tipo de produto para venda em lote que você deseja cadastrar: ').capitalize()
                        while True:
                            volume = float(input('Digite o volume do produto: '))
                            if volume <= 0 :
                                print('Esse volume é inválido para o produto, tente novamente!')
                                continue
                            else:
                                break
                        unidade = input('Qual seria a unidade de medida desse produto? ')
                        while True:
                            valor = float(input('Digite o valor do produto: '))
                            if valor <= 0 :
                                    print('Esse valor é inválido para o produto, tente novamente!')
                                    continue
                            else:
                                break 
                        produtos.append([produto,volume,unidade,valor])
                elif op_categoria == 4:
                        produto = input('Digite o tipo de produto para venda em lote que você deseja cadastrar: ').capitalize()
                        while True:
                            volume = float(input('Digite o volume do produto: '))
                            if volume <= 0 :
                                print('Esse volume é inválido para o produto, tente novamente!')
                                continue
                            else:
                                break
                        unidade = input('Qual seria a unidade de medida desse produto? ')
                        while True:
                            valor = float(input('Digite o valor do produto: '))
                            if valor <= 0 :
                                    print('Esse valor é inválido para o produto, tente novamente!')
                                    continue
                            else:
                                break 
                        produtos.append([produto,volume,unidade,valor])

                elif op_categoria == 5:
                        produto = input('Digite o tipo de produto artesanal que você deseja cadastrar: ').capitalize()
                        while True:
                            quantidade = float(input('Digite o quantidade do produto: '))
                            if quantidade <= 0 :
                                print('Esse quantidade é inválido para o produto, tente novamente!')
                                continue
                            else:
                                break
                        unidade = input('Qual seria a unidade de medida desse produto? ')
                        while True:
                            valor = float(input('Digite o valor do produto: '))
                            if valor <= 0 :
                                    print('Esse valor é inválido para o produto, tente novamente!')
                                    continue
                            else:
                                break 
                        produtos.append([produto,quantidade,unidade,valor])
                elif op_categoria == 6:
                    break
                elif op_categoria == 5:
                        produto = input('Digite o tipo de produto artesanal que você deseja cadastrar: ').capitalize()
                        while True:
                            quantidade = float(input('Digite o quantidade do produto: '))
                            if quantidade <= 0 :
                                print('Esse quantidade é inválido para o produto, tente novamente!')
                                continue
                            else:
                                break
                        unidade = input('Qual seria a unidade de medida desse produto? ')
                        while True:
                            valor = float(input('Digite o valor do produto: '))
                            if valor <= 0 :
                                    print('Esse valor é inválido para o produto, tente novamente!')
                                    continue
                            else:
                                break 
                        produtos.append([produto,quantidade,unidade,valor])
                elif op_categoria == 6:
                    break

        elif op_adm == 5:
            print('\033[1;32m~'*100)
            print('~' *41,'LISTA DE PRODUTOS', '~' *40)
            print('\033[1;32m~\033[m'*100)
            for produto, quantidade, unidade, valor in produtos:
                print(f'\033[1;35mProduto:\033[m {produto}')
                print(f'\033[1;35mQuantidade:\033[m {quantidade} {unidade}')
                print(f'\033[1;35mValor:\033[m R${valor}')
                print('\033[1;32m~\033[m'*100)

        elif op_adm == 6:
            print('\033[1;32m~\033[m'*100)
            print('[\033[1;33m1\033[m]ALTERAR\n[\033[1;33m2\033[m]REMOVER') 
            remover_alterar = input('Digite a opção que você deseja: ')
            if remover_alterar == '1':
                alteracao = input('Qual produto você deseja alterar? ').capitalize()
                for i in produtos:
                    if i[0] == alteracao:
                            print(i)
                            print('\033[1;32m~\033[m'*100)
                            print('[\033[1;33m1\033[m]PRODUTO\n[\033[1;33m2\033[m]PESO/VOLUME\n[\033[1;33m3\033[m]UNIDADE\n[\033[1;33m4\033[m]VALOR')
                            escolha_alteracao = input('Digite o que você deseja alterar: ')
                            if escolha_alteracao == '1':
                                tipo_alteracao = input(f'Digite o produto que você deseja substituir no lugar de {i[0]}: ').capitalize()
                                i[0] = tipo_alteracao
                                print('Produto alterado com sucesso!')
                                break
                            elif escolha_alteracao == '2':
                                peso_alteracao = float(input(f'Digite o peso/volume que você deseja substituir no lugar de {i[1]}:'))
                                i[1] = peso_alteracao
                                print('Produto alterado com sucesso!')
                                break
                            elif escolha_alteracao == '3':
                                unidade_alteracao = input(f'Digite a unidade que você deseja substituir no lugar de {i[2]}: ')
                                i[2] = unidade_alteracao
                                print('Produto alterado com sucesso!')
                                break
                            elif escolha_alteracao == '4':
                                valor_alteracao = input(f'Digite o valor que você deseja substituir no lugar de {i[3]}: ')
                                i[3] = valor_alteracao
                                print('Produto alterado com sucesso!')
                                break
                            else:
                                print('Produto não encontrado!')
            elif remover_alterar == '2':
                remover = input('Digite o produto que você deseja remover: ').capitalize()
                for i in produtos:
                    if i[0] == remover:
                        print(i)
                        print('\033[1;32m~\033[m'*100)
                        produtos.remove(i)
                        print('Produto removido com sucesso!')
                        break
                    else:
                        print('Produto não encontrado!')
        elif op_adm == 7:
            print('\033[1;32m~'*100,'\033[m')
            print('\033[1;32m~'*38,'CONVERSOR DE FABRICAÇÃO','~\033[m'*39)
            print('\033[1;32m~'*100,'\033[m')
            print('[\033[1;33m1\033[m]QUEIJO\n[\033[1;33m2\033[m]DERIVADOS\n[\033[1;33m3\033[m]ARTESANAIS')
            escolha = input('Qual produto você deseja fabricar? ')
            if escolha == '1':
                    print('\033[1;32m~\033[m'*100)
                    print('[\033[1;33m1\033[m]COALHO\n[\033[1;33m2\033[m]QUEIJO MANTEIGA\n[\033[1;33m3\033[m]MUSSARELA\n[\033[1;33m4\033[m]REQUEIJÃO')
                    decisao = input('Digite a opção de queijo que deseja fabricar: ')
                    if decisao == '1':
                        while True:
                            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                            if quantidade_producao <=0:
                                print('Quantidade inexistente! Tente novamente.')
                                continue
                            else:
                                break
                        leite_necessario = quantidade_producao * 10
                        print(f'Para fabricar {quantidade_producao} kg de queijo, serão necessários {leite_necessario:.2f} litros de leite!')
                        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                        if confirmacao == 'S':
                            if leite[0] < leite_necessario:
                                print('Quantidade no estoque indisponível para fabrição!')
                            elif leite[0] >= leite_necessario:
                                leite[0] -= leite_necessario
                                valor_sub = float(input('Qual o valor para venda desse produto? '))
                                produtos.append(['Coalho',quantidade_producao,'kg',valor_sub])
                                print('Conversão realizada com sucesso!')
                                # 
                        else:
                            print('Conversão cancelada!')
                            break
                    elif decisao == '2':
                        while True:
                            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                            if quantidade_producao <=0:
                                print('Quantidade inexistente! Tente novamente.')
                                continue
                            else:
                                break
                        leite_necessario = quantidade_producao * 10
                        print(f'Para fabricar {quantidade_producao} kg de queijo, serão necessários {leite_necessario:.2f} litros de leite!')
                        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                        if confirmacao == 'S':
                            if leite[0] < leite_necessario:
                                print('Quantidade no estoque indisponível para fabrição!')
                            elif leite[0] >= leite_necessario:
                                leite[0] -= leite_necessario
                                valor_sub = float(input('Qual o valor para venda desse produto? '))
                                produtos.append(['Queijo Manteiga',quantidade_producao,'kg',valor_sub])
                                print('Conversão realizada com sucesso!')
                        else:
                            print('Conversão cancelada!')
                            break
                    elif decisao == '3':
                        while True:
                            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                            if quantidade_producao <=0:
                                print('Quantidade inexistente! Tente novamente.')
                                continue
                            else:
                                break
                        leite_necessario = quantidade_producao * 10
                        print(f'Para fabricar {quantidade_producao} kg de queijo, serão necessários {leite_necessario:.2f} litros de leite!')
                        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                        if confirmacao == 'S':
                            if leite[0] < leite_necessario:
                                print('Quantidade no estoque indisponível para fabrição!')
                            elif leite[0] >= leite_necessario:
                                leite[0] -= leite_necessario
                                valor_sub = float(input('Qual o valor para venda desse produto? '))
                                produtos.append(['Mussarela',quantidade_producao,'kg',valor_sub])
                                print('Conversão realizada com sucesso!')
                        else:
                            print('Conversão cancelada!')
                            break
                    elif decisao == '4':
                        while True:
                            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                            if quantidade_producao <=0:
                                print('Quantidade inexistente! Tente novamente.')
                                continue
                            else:
                                break
                        leite_necessario = quantidade_producao * 10
                        print(f'Para fabricar {quantidade_producao} kg de queijo, serão necessários {leite_necessario:.2f} litros de leite!')
                        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                        if confirmacao == 'S':
                            if leite[0] < leite_necessario:
                                print('Quantidade no estoque indisponível para fabrição!')
                            elif leite[0] >= leite_necessario:
                                leite[0] -= leite_necessario
                                valor_sub = float(input('Qual o valor para venda desse produto? '))
                                produtos.append(['Requeijão',quantidade_producao,'kg',valor_sub])
                                print('Conversão realizada com sucesso!')
                        else:
                            print('Conversão cancelada!')
                            break
            elif escolha == '2':
                print('\033[1;32m~\033[m'*100)
                print('[\033[1;33m1\033[m]MANTEIGA COMUM\n[\033[1;33m2\033[m]CREME DE LEITE[\033[1;33m3\033[m]IOGURTE\n[\033[1;33m4\033[m]DOCE DE LEITE\n[\033[1;33m5\033[m]COALHADA')
                decisao = input('Digite a opção de queijo que deseja fabricar: ')
                if decisao == '1':
                            while True:
                                quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                                if quantidade_producao <=0:
                                    print('Quantidade inexistente! Tente novamente.')
                                    continue
                                else:
                                    break
                            leite_necessario = quantidade_producao * 5
                            print(f'Para fabricar {quantidade_producao} kg de manteiga, serão necessários {leite_necessario:.2f} litros de leite!')
                            confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                            if confirmacao == 'S':
                                if leite[0] < leite_necessario:
                                    print('Quantidade no estoque indisponível para fabrição!')
                                elif leite[0] >= leite_necessario:
                                    leite[0] -= leite_necessario
                                    valor_sub = float(input('Qual o valor para venda desse produto? '))
                                    produtos.append(['Manteiga',quantidade_producao,'kg',valor_sub])
                                    print('Conversão realizada com sucesso!')
                            else:
                                print('Conversão cancelada!')
                                break
                elif decisao == '2':
                            while True:
                                quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                                if quantidade_producao <=0:
                                    print('Quantidade inexistente! Tente novamente.')
                                    continue
                                else:
                                    break
                            leite_necessario = quantidade_producao * 5
                            print(f'Para fabricar {quantidade_producao} litros de creme de leite, serão necessários {leite_necessario:.2f} litros de leite!')
                            confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                            if confirmacao == 'S':
                                if leite[0] < leite_necessario:
                                    print('Quantidade no estoque indisponível para fabrição!')
                                elif leite[0] >= leite_necessario:
                                    leite[0] -= leite_necessario
                                    valor_sub = float(input('Qual o valor para venda desse produto? '))
                                    produtos.append(['Creme de Leite',quantidade_producao,'L',valor_sub])
                                    print('Conversão realizada com sucesso!')
                            else:
                                print('Conversão cancelada!')
                                break
                elif decisao == '3':
                            while True:
                                quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                                if quantidade_producao <=0:
                                    print('Quantidade inexistente! Tente novamente.')
                                    continue
                                else:
                                    break
                            leite_necessario = quantidade_producao * 1
                            print(f'Para fabricar {quantidade_producao} litro de iogurte, serão necessários {leite_necessario:.2f} litros de leite!')
                            confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                            if confirmacao == 'S':
                                if leite[0] < leite_necessario:
                                    print('Quantidade no estoque indisponível para fabrição!')
                                elif leite[0] >= leite_necessario:
                                    leite[0] -= leite_necessario
                                    valor_sub = float(input('Qual o valor para venda desse produto? '))
                                    produtos.append(['Iogurte',quantidade_producao,'L',valor_sub])
                                    print('Conversão realizada com sucesso!')
                            else:
                                print('Conversão cancelada!')
                                break
                elif decisao == '4':
                            while True:
                                quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                                if quantidade_producao <=0:
                                    print('Quantidade inexistente! Tente novamente.')
                                    continue
                                else:
                                    break
                            leite_necessario = quantidade_producao * 5
                            print(f'Para fabricar {quantidade_producao} kg de doce de leite, serão necessários {leite_necessario:.2f} litros de leite!')
                            confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                            if confirmacao == 'S':
                                if leite[0] < leite_necessario:
                                    print('Quantidade no estoque indisponível para fabrição!')
                                elif leite[0] >= leite_necessario:
                                    leite[0] -= leite_necessario
                                    valor_sub = float(input('Qual o valor para venda desse produto? '))
                                    produtos.append(['Doce de Leite',quantidade_producao,'kg',valor_sub])
                                    print('Conversão realizada com sucesso!')
                            else:
                                print('Conversão cancelada!')
                                break
                elif decisao == '5':
                            while True:
                                quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                                if quantidade_producao <=0:
                                    print('Quantidade inexistente! Tente novamente.')
                                    continue
                                else:
                                    break
                            leite_necessario = quantidade_producao * 1.25
                            print(f'Para fabricar {quantidade_producao} kg de coalhada, serão necessários {leite_necessario:.2f} litros de leite!')
                            confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                            if confirmacao == 'S':
                                if leite[0] < leite_necessario:
                                    print('Quantidade no estoque indisponível para fabrição!')
                                elif leite[0] >= leite_necessario:
                                    leite[0] -= leite_necessario
                                    valor_sub = float(input('Qual o valor para venda desse produto? '))
                                    produtos.append(['Coalhada',quantidade_producao,'kg',valor_sub])
                                    print('Conversão realizada com sucesso!')
                            else:
                                print('Conversão cancelada!')
                                break
            elif escolha == '3':
                print('\033[1;32m~\033[m'*100)
                print('[\033[1;33m1\033[m]MANTEIGA DA TERRA\n[\033[1;33m2\033[m]QUEIJO DEFUMADO[\033[1;33m3\033[m]NATA')
                decisao = input('Digite a opção de queijo que deseja fabricar: ')
                if decisao == '1':
                            while True:
                                quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                                if quantidade_producao <=0:
                                    print('Quantidade inexistente! Tente novamente.')
                                    continue
                                else:
                                    break
                            leite_necessario = quantidade_producao * 10
                            print(f'Para fabricar {quantidade_producao} kg de manteiga da terra, serão necessários {leite_necessario:.2f} litros de leite!')
                            confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                            if confirmacao == 'S':
                                if leite[0] < leite_necessario:
                                    print('Quantidade no estoque indisponível para fabrição!')
                                elif leite[0] >= leite_necessario:
                                    leite[0] -= leite_necessario
                                    valor_sub = float(input('Qual o valor para venda desse produto? '))
                                    produtos.append(['Manteiga da Terra',quantidade_producao,'kg',valor_sub])
                                    print('Conversão realizada com sucesso!')
                            else:
                                print('Conversão cancelada!')
                                break 
                elif decisao == '2':
                            while True:
                                quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                                if quantidade_producao <=0:
                                    print('Quantidade inexistente! Tente novamente.')
                                    continue
                                else:
                                    break
                            leite_necessario = quantidade_producao * 11.1
                            print(f'Para fabricar {quantidade_producao} kg de queijo defumado, serão necessários {leite_necessario:.2f} litros de leite!')
                            confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                            if confirmacao == 'S':
                                if leite[0] < leite_necessario:
                                    print('Quantidade no estoque indisponível para fabrição!')
                                elif leite[0] >= leite_necessario:
                                    leite[0] -= leite_necessario
                                    valor_sub = float(input('Qual o valor para venda desse produto? '))
                                    produtos.append(['Queijo Defumado',quantidade_producao,'kg',valor_sub])
                                    print('Conversão realizada com sucesso!')
                            else:
                                print('Conversão cancelada!')
                                break
                elif decisao == '3':
                            while True:
                                quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                                if quantidade_producao <=0:
                                    print('Quantidade inexistente! Tente novamente.')
                                    continue
                                else:
                                    break
                            leite_necessario = quantidade_producao * 6.6
                            print(f'Para fabricar {quantidade_producao} kg de nata, serão necessários {leite_necessario} litros de leite!')
                            confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
                            if confirmacao == 'S':
                                if leite[0] < leite_necessario:
                                    print('Quantidade no estoque indisponível para fabrição!')
                                elif leite[0] >= leite_necessario:
                                    leite[0] -= leite_necessario
                                    valor_sub = float(input('Qual o valor para venda desse produto? '))
                                    produtos.append(['Nata',quantidade_producao,'kg',valor_sub])
                                    print('Conversão realizada com sucesso!')
                            else:
                                print('Conversão cancelada!')
                                break 
        elif op_adm == 8:
            print('\033[1;32m~'*100)
            print('~'*42,'PRODUÇÃO DIÁRIA','~'*41)
            print('~\033[m'*100)
            print(f'Estoque atual:{leite}')
            while True:
                print('\033[1;32m~\033[m'*100)
                print('[\033[1;33m1\033[m]ADICIONAR\n[\033[1;33m2\033[m]REMOVER\n[\033[1;33m3\033[m]SAIR')
                escolha_leite = input('Digite a opção que deseja: ')
                if escolha_leite == '1':
                    while True:
                        producao_diaria = float(input('Digite a quantidade de leite ordenhado do dia: '))
                        if producao_diaria <= 0 :
                            print('Quantidade inexistente! Tente novamente.')
                            continue
                        else:
                            break
                    leite[0] += producao_diaria
                    valor_diaria = float(input('Digite o valor do leite atualizado: '))
                    leite.append[1](valor_diaria)
                    print(f'Produção diária cadastrada com sucesso!\nEstoque atual: {leite[0]}')
                elif escolha_leite == '2':
                    leite_remover = float(input('Digite a quantidade de leite que você deseja remover: '))
                    leite[0] -= leite_remover
                    print(f'Quantidade de leite removida com sucesso!\nEstoque atual: {leite[0]}')
                elif escolha_leite == '3':
                    break
        elif op_adm == 9:
            login_funcoes.voltando_inicio()
#menu cliente
if login_encontrado_cliente == True:
    compras = []
    encomendas = []
    while True:
        print('~' * 100)
        print('~' *43,'MENU CLIENTE', '~' *43)
        print('~' * 100)
        print('[1] VER PRODUTOS\n[2] COMPRAR PRODUTOS\n[3] ENCOMENDAR PRODUTOS\n[4] VER ANIMAIS\n[5] COMPRAR ANIMAL\n[6] ENCOMENDAR ANIMAL\n[7] VER ENCOMENDAS\n[8] COMPRAR LEITE\n[9] HISTÓRICOS DE COMPRAS\n[10] BENEFÍCIOS DO CLIENTE\n[11] FORMAS DE PAGAMENTO\n[12] VOLTAR')

        op_cliente = int(input('Digite a opção desejada: '))

        if op_cliente == 1:
            if len(produtos) == 0:
                print('Nenhum produto cadastrado!')

            else:
                print('\033[1;32m~\033[m'*100)
                print('~' *41,'LISTA DE PRODUTOS', '~' *40)
                print('~'*100)
                for produto, quantidade, unidade, valor in produtos:
                    print(f'Produto: {produto}')
                    print(f'Quantidade: {quantidade} {unidade}')
                    print(f'Valor: R${valor}')
                    print('\033[1;32m~\033[m'*100)

        elif op_cliente == 2:
            print('~'*100)
            print('~' *41,'COMPRAR PRODUTOS', '~' *41)
            print('~'*100)
            produto_input = input('Digite o produto que deseja comprar: ').strip().capitalize()
            encontrado = False
            for item in produtos:

                if item[0].capitalize() == produto_input:

                    encontrado = True

                    quantidade_compra = int(input('Digite a quantidade desejada: '))

                    if quantidade_compra > item[1]:

                        print('Quantidade indisponível em estoque!')

                        print(f'Estoque disponível: {item[1]}{item[2]}')

                    else:

                        unidade = item[2]

                        valor_compra = item[3]

                        valor_total = quantidade * valor_compra

                        if len(compras) >= 3:

                            desconto = valor_total * 0.10

                            valor_final = valor_total - desconto

                            print(f'Desconto aplicado: {desconto}')

                        else:

                            valor_final = valor_total

                        print(f'Valor final: {valor_final}')

                        item[1] -= quantidade_compra

                        compras.append([produto_input, quantidade_compra, unidade, valor_final])

                        print('Compra realizada com sucesso!')

                    break

            if encontrado == False:

                print('Produto não encontrado!')

        elif op_cliente == 3:
            print('~'*100)
            print('~' *40,'ENCOMENDAR PRODUTOS', '~' *39)
            print('~'*100)
            produto_input = input('Digite o produto que deseja encomendar: ').capitalize()
            for item in produtos:
                if item[0].capitalize() == produto_input:
                    encontrado = True
                    break
                else:
                    print('Produto não encontrado!')
            while True:
                quantidade = int(input('Digite a quantidade desejada: '))
                if quantidade <= 0:
                    print('Quantidade inexistente! Tente novamente.')
                    continue
                else:
                    break
            data = input('Digite a data desejada:\n(DD/MM/AA)\n ')
            horario = input('Digite o horário desejado: ')

            encomendas.append([produto_input, quantidade, data, horario])

            print('Encomenda realizada com sucesso!')

        elif op_cliente == 4:
            if len(animais) == 0:
                print('Nenhum animal cadastrado!')
            else:
                print('~'*100)
                print('~' *40,'LISTA DE ANIMAIS', '~' *40)
                print('~'*100)
                for animal, peso, genero, status, valor in animais:
                    print(f'Animal: {animal}')
                    print(f'Peso: {peso}')
                    print(f'Gênero: {genero}')
                    print(f'Status: {status}')
                    print(f'Valor: R${valor}')
                    print('-' * 100)

        elif op_cliente == 5:
            print('~'*100)
            print('~' *40,'COMPRAR ANIMAIS', '~' *40)
            print('~'*100)
            animal_input = input('Digite o animal que deseja comprar: ').strip().capitalize()
            encontrado = False
            for item in animais:

                if item[0].capitalize() == animal_input:

                    encontrado = True

                    quantidade_animal = int(input('Digite a quantidade desejada: '))

                    if quantidade_animal > item[1]:

                        print('Quantidade indisponível em estoque!')

                        print(f'Estoque disponível: 1')

                    else:
                        valor_animal = item[4]

                        valor_total = quantidade * valor_animal

                        if len(compras) >= 3:

                            desconto = valor_total * 0.10

                            valor_final = valor_total - desconto

                            print(f'Desconto aplicado: {desconto}')

                        else:

                            valor_final = valor_total

                        print(f'Valor final: {valor_final}')

                        item[1] -= quantidade_animal

                        compras.append([animal_input, quantidade_animal, valor_final])

                        print('Compra realizada com sucesso!')

                    break
            if encontrado == False:
                print('Animal não encontrado!')

        elif op_cliente == 6:
            print('~'*100)
            print('~' *40,'ENCOMENDAR ANIMAIS', '~' *39)
            print('~'*100)
            animal_input = input('Digite o animal que deseja encomendar: ').capitalize()
            for item in animais:
                if item[0].capitalize() == animal_input:
                    encontrado = True
                    break
                else:
                    print('Animal não encontrado!')
                    break
            while True:
                quantidade = int(input('Digite a quantidade desejada: '))
                if quantidade <= 0:
                    print('Quantidade inexistente! Tente novamente.')
                    continue
                else:
                    break
            data = input('Digite a data desejada:\n(DD/MM/AA)\n ')
            horario = input('Digite o horário desejado: ')

            encomendas.append([animal_input, quantidade, data, horario])

            print('Encomenda realizada com sucesso!')

        elif op_cliente == 7:

            if len(encomendas) == 0:
                print('Nenhuma encomenda realizada!')

            else:
                print('~'*100)
                print('~' *40,'LISTA DE ENCOMENDAS', '~' *39)
                print('~'*100)

                for produto_input, quantidade, data, horario in encomendas:
                    print(f'Produto: {produto_input}')
                    print(f'Quantidade: {quantidade}')
                    print(f'Data: {data}')
                    print(f'Horário: {horario}')
                    print('-' * 100)

                for animal_input, quantidade, data, horario in encomendas:
                    print(f'Animal: {animal_input}')
                    print(f'Quantidade: {quantidade}')
                    print(f'Data: {data}')
                    print(f'Horário: {horario}')
                    print('-' * 100)

        elif op_cliente == 8:
            print('~'*100)
            print('~' *42,'COMPRAR LEITE', '~' *42)
            print('~'*100)
            quantidade_leite = int(input('Digite a quantidade desejada: '))
            if quantidade_leite > leite[0]:
                        print('Quantidade indisponível em estoque!')
                        print(f'Estoque disponível: {leite[0]}')

            else:
                        valor_leite = leite[1]

                        valor_total = quantidade_leite * valor_leite

                        if len(compras) >= 3:

                            desconto = valor_total * 0.10

                            valor_final = valor_total - desconto

                            print(f'Desconto aplicado: {desconto}')

                        else:

                            valor_final = valor_total

                        print(f'Valor final: {valor_final}')

                        leite[0] -= quantidade_leite

                        compras.append(['LEITE',quantidade_leite, valor_final])

                        print('Compra realizada com sucesso!')

        elif op_cliente == 9:
            print('~'*100)
            print('~'*40,'HISTÓRICOS DE COMPRAS','~'*37)
            print('~'*100)
            if len(compras) == 0:
                print('Nenhuma encomenda realizada!')
            else:
                for i in compras:
                    print(i)

        elif op_cliente == 10:
            print('~'*100)
            print('~'*40,'BENEFÍCIOS DO CLIENTE','~'*37)
            print('~'*100)
            if len(compras) >= 3:
                print('Você já possui direito aos 10% de desconto nas compras.')
                
            else: 
                faltam = 3 - len(compras)
                print(f'Faltam {faltam} compras para liberar os 10% de desconto.')

        elif op_cliente == 11:
            print('~'*100)
            print('~'*40,'FORMAS DE PAGAMENTO','~'*39)
            print('~'*100)
            print('[1] PIX')
            print('[2] BOLETO')

            pagamento = input('Escolha a forma de pagamento: ')

            if pagamento == '1':
                print('Pagamento via PIX selecionado!')
                print('Chave PIX: fazendasertao@gmail.com')
            elif pagamento == '2':
                print('Pagamento via BOLETO selecionado!')
                print('Boleto gerado com sucesso!')
            else:
                print('Opção invalida!')    
        
        
        elif op_cliente == 12:
            login_funcoes.voltando_inicio()
        else:
            print('Opção indisponível!')