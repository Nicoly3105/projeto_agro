from colorama import Fore, init
init()

animais = [ {'Brinco':'002','Animal': 'Vaca','Peso': 37,'Gênero': 'Fêmea','Status': 'Grávida','Valor': 8}]
produtos = [{'Produto': 'Coalho','Quantidade': 7,'Unidade': 'kg','Valor': 6.5}]
leite = {'Produto':'Leite','Volume':1000,'Valor':5.5}
historico = []
def cadastro_animais():
    print('\033[1;32m~'*40,'CADASTRO DE ANIMAIS','~'*39, '\033[m')
    brinco = int(input('Digite a numeração do brinco do animal: ')).capitalize()
    animal = input('Digite o animal que você deseja cadastrar: ').capitalize()
    while True:
        peso = float(input('Digite o peso do animal: '))
        if peso <= 0 :
            print('\033[1;31mEsse peso é inválido para o animal, tente novamente!\033[m')
            continue
        else:
            break
    print('[\033[1;33m1\033[m]FÊMEA\n[\033[1;33m2\033[m]MACHO')
    genero = input('Digite a opção do gênero do animal: ')
    if genero == 1:
        genero == 'Fêmea'
    elif genero == 2:
        genero == 'Macho'
    else:
        print('\033[1;31mOpção inválida!\033[m')
    status = input('Digite o status do animal: ')
    while True:
        valor = float(input('Digite o valor do animal: '))
        if valor <= 0 :
            print('\033[1;31mEsse valor é inválido para o animal, tente novamente!\033[m')
            continue
        else:
            break 
    animais.append({'Brinco':brinco,'Animal':animal,'Peso':peso,'Gênero':genero,'Status':status,'Valor':valor})
    historico.append({'Ação':'Cadastro Animal', 'Item': animal, 'Quantidade': 1,'Valor':valor})
    print('\033[1;34mAnimal cadastrado com sucesso!\033[m')
    ultimo = produtos[-1]
    print(f"\033[1;35mBrinco:\033[m {ultimo['Brinco']}")
    print(f"\033[1;35mAnimal:\033[m {ultimo['Animal']}")
    print(f"\033[1;35mPeso:\033[m {ultimo['Peso']}")
    print(f"\033[1;35mGênero:\033[m {ultimo['Gênero']}")
    print(f"\033[1;35mStatus:\033[m {ultimo['Status']}")
    print(f"\033[1;35mValor:\033[m R${ultimo['Valor']}")
    print('\033[1;35m~' * 100,'\033[m')

def lista_animais():
    if len(animais) == 0:
        print('\033[1;31mNenhum animal cadastrado ainda!\033[m')
    else:
        print('\033[1;32m~'*100)
        print('~' *35,'LISTA DE ANIMAIS CADASTRADOS', '~' *35)
        print('~'*100, '\033[m')
        for item in animais:
            print(f"\033[1;35mBrinco:\033[m {item['Brinco']}")
            print(f"\033[1;35mAnimal:\033[m {item['Animal']}")
            print(f"\033[1;35mPeso:\033[m {item['Peso']}")
            print(f"\033[1;35mGênero:\033[m {item['Gênero']}")
            print(f"\033[1;35mStatus:\033[m {item['Status']}")
            print(f"\033[1;35mValor:\033[m R${item['Valor']}")
            print('\033[1;35m~' * 100,'\033[m')

def alterar_remover_animal():
            print('\033[1;32m~\033[m'*100)
            print('[\033[1;33m1\033[m]ALTERAR\n[\033[1;33m2\033[m]REMOVER')
            print('\033[1;32m~'*100,'\033[m') 
            remover_alterar = input('Digite a opção que você deseja: ')
            if remover_alterar == '1':
                print('\033[1;32m~\033[m'*100)    
                print('\033[1;32m~'*42, 'MENU ALTERAÇÃO','~'*42,'\033[m')
                print('\033[1;32m~'*100,'\033[m')
                alteracao = input('Qual o brinco do animal você deseja alterar? ').capitalize()
                for i in animais:
                    if i['Brinco'] == alteracao:
                            print(f"\033[1;35mBrinco:\033[m {i['Brinco']}")
                            print(f"\033[1;35mAnimal:\033[m {i['Animal']}")
                            print(f"\033[1;35mPeso:\033[m {i['Peso']}")
                            print(f"\033[1;35mGênero:\033[m {i['Gênero']}")
                            print(f"\033[1;35mStatus:\033[m {i['Status']}")
                            print(f"\033[1;35mValor:\033[m R${i['Valor']}")
                            print('\033[1;35m~\033[m'*100)
                            print('[\033[1;33m1\033[m]BRINCO\n[\033[1;33m2\033[m]TIPO ANIMAL\n[\033[1;33m3\033[m]PESO\n[\033[1;33m4\033[m]GÊNERO\n[\033[1;33m5\033[m]STATUS\n[\033[1;33m6\033[m]VALOR')
                            escolha_alteracao = input('Digite o que você deseja alterar: ')
                            if escolha_alteracao == '1':
                                tipo_alteracao = input(f"Digite o nome que você deseja substituir no lugar de: {i['Animal']}>  ")
                                i['Brinco'] = tipo_alteracao
                                print('\033[1;34mBrinco alterado com sucesso!\033[m')
                                break
                            elif escolha_alteracao == '2':
                                tipo_alteracao = input(f"Digite o nome que você deseja substituir no lugar de: {i['Animal']}>  ")
                                i['Animal'] = tipo_alteracao
                                print('\033[1;34mAnimal alterado com sucesso!\033[m')
                                break
                            elif escolha_alteracao == '3':
                                peso_alteracao = float(input(f"Digite o peso que você deseja substituir no lugar de: {i['Peso']}> "))
                                i['Peso'] = peso_alteracao
                                print('\033[1;34mPeso alterado com sucesso!\033[m')
                                break
                            elif escolha_alteracao == '4':
                                genero_alteracao = input(f"Digite o gênero que você deseja substituir no lugar de: {i['Gênero']}>  ")
                                i['Gênero'] = genero_alteracao
                                print('\033[1;34mGênero alterado com sucesso!\033[m')
                                break
                            elif escolha_alteracao == '5':
                                status_alteracao = input(f"Digite o status que você deseja substituir no lugar de: {i['Status']}>  ")
                                i['Status'] = status_alteracao
                                print('\033[1;34mStatus alterado com sucesso!\033[m')
                                break
                            elif escolha_alteracao == '6':
                                valor_alteracao = float(input(f"Digite o valor que você deseja substituir no lugar de: {i['Valor']}>  "))
                                i['Valor'] = valor_alteracao
                                print('\033[1;34mValor alterado com sucesso!\033[m')
                                break
                            historico.append({'Ação':'Alteração do Animal', 'Item': i['Animal'], 'Quantidade': 1 , 'Valor': i['Valor']})
                else:
                    print('\033[1;31mAnimal não encontrado!\033[m')
            elif remover_alterar == '2':
                print('\033[1;32m~\033[m'*100)    
                print('\033[1;32m~'*43, 'MENU REMOÇÃO','~'*43,'\033[m')
                print('\033[1;32m~'*100,'\033[m')
                remover = input('Qual o brinco do animal você deseja alterar? ').capitalize()
                for i in animais:
                    if i['Brinco'] == remover:
                        print(f"\033[1;35mBrinco:\033[m {i['Brinco']}")
                        print(f"\033[1;35mAnimal:\033[m {i['Animal']}")
                        print(f"\033[1;35mPeso:\033[m {i['Peso']}")
                        print(f"\033[1;35mGênero:\033[m {i['Gênero']}")
                        print(f"\033[1;35mStatus:\033[m {i['Status']}")
                        print(f"\033[1;35mValor:\033[m R${i['Valor']}")
                        print('\033[1;35m~' * 100,'\033[m')
                        animais.remove(i)
                        print('\033[1;34mAnimal removido com sucesso!\033[m')
                        historico.append({'Ação':'Remoção Animal', 'Item': i['Animal'], 'Quantidade': 1 , 'Valor': i['Valor']})
                        break
                else:
                    print('\033[1;31mAnimal não encontrado!\033[m')
            else:
                print('\033[1;31mOpção inválida!\033[m')

# cadastro de produtos
def cadas_queijo():
    print('\033[1;32m~\033[m'*100)
    produto = str(input('Digite o tipo de queijo que você deseja cadastrar: ')).capitalize()
    while True:
        peso = float(input('Digite o peso do produto: '))
        if peso <= 0 :
            print('\033[1;31mEsse peso é inválido para o produto, tente novamente!\033[m')
            continue
        else:
            break
    unidade = input('Qual seria a unidade de medida desse produto? ')
    while True:
        valor = float(input('Digite o valor do produto: '))
        if valor <= 0 :
            print('\033[1;31mEsse valor é inválido para o produto, tente novamente!\033[m')
            continue
        else:
            break 
    produtos.append({'Produto':produto,'Quantidade':peso,'Unidade':unidade,'Valor':valor})
    historico.append({'Ação':'Cadastro Queijo', 'Item': produto, 'Quantidade': peso , 'Valor':valor})
    print('\033[1;34mProduto cadastrado com sucesso!\033[m')
    ultimo = produtos[-1]
    print('\033[1;35m~'*100,'\033[m')
    print(f"\033[1;35mProduto:\033[m {ultimo['Produto']}")
    print(f"\033[1;35mQuantidade:\033[m {ultimo['Quantidade']} {ultimo['Unidade']}")
    print(f"\033[1;35mValor:\033[m R${ultimo['Valor']}")
    print('\033[1;35m~'*100,'\033[m')

def cadas_leite():
    while True:
        print('\033[1;32m~\033[m'*100)
        volume = float(input('Digite o volume do leite em litros: '))
        if volume <= 0 :
            print('\033[1;31mEsse volume é inválido para o produto, tente novamente!\033[m')
            continue
        else:
            break
    while True:
        valor = float(input('Digite o valor do produto: '))
        if valor <= 0 :
            print('\033[1;31mEsse valor é inválido para o produto, tente novamente!\033[m')
            continue
        else:
            break 
    leite['Volume'] += volume
    leite['Valor'] += valor
    historico.append({'Ação':'Cadastro Leite', 'Item': leite['Produto'], 'Quantidade': volume , 'Valor':valor})
    print('\033[1;34mProduto cadastrado com sucesso!\033[m')
    print(f'\033[1;35mProduto:\033[m Leite')
    print(f'\033[1;35mQuantidade:\033[m {leite["Volume"]} litros')
    print(f'\033[1;35mValor:\033[m R${leite["Valor"]}')
    print('\033[1;35m~'*100,'\033[m')


def cadas_derivado():
    print('\033[1;32m~\033[m'*100)
    produto = input('Digite o tipo de derivado que você deseja cadastrar: ').capitalize()
    while True:
        quantidade = float(input('Digite a quantidade do produto: '))
        if quantidade <= 0 :
            print('\033[1;31mEssa quantidade é inválida para o produto, tente novamente!\033[m')
            continue
        else:
            break
    unidade = input('Qual seria a unidade de medida desse produto? ')
    while True:
        valor = float(input('Digite o valor do produto: '))
        if valor <= 0 :
            print('\033[1;31mEsse valor é inválido para o produto, tente novamente!\033[m')
            continue
        else:
            break 
    produtos.append({'Produto':produto,'Quantidade':quantidade,'Unidade':unidade,'Valor':valor})
    historico.append({'Ação':'Cadastro Derivado', 'Item': produto, 'Quantidade': quantidade, 'Valor':valor})
    print('\033[1;34mProduto cadastrado com sucesso!\033[m')
    ultimo = produtos[-1]
    print('\033[1;35m~'*100,'\033[m')
    print(f"\033[1;35mProduto:\033[m {ultimo['Produto']}")
    print(f"\033[1;35mQuantidade:\033[m {ultimo['Quantidade']} {ultimo['Unidade']}")
    print(f"\033[1;35mValor:\033[m R${ultimo['Valor']}")
    print('\033[1;35m~'*100,'\033[m')

def cadas_artesanal():
    print('\033[1;32m~\033[m'*100)
    produto = input('Digite o tipo de produto artesanal que você deseja cadastrar: ').capitalize()
    while True:
        quantidade = float(input('Digite o quantidade do produto: '))
        if quantidade <= 0 :
            print('\033[1;31mEsse quantidade é inválido para o produto, tente novamente!\033[m')
            continue
        else:
            break
    unidade = input('Qual seria a unidade de medida desse produto? ')
    while True:
        valor = float(input('Digite o valor do produto: '))
        if valor <= 0 :
            print('\033[1;31mEsse valor é inválido para o produto, tente novamente!\033[m')
            continue
        else:
            break 
    produtos.append({'Produto':produto,'Quantidade':quantidade,'Unidade':unidade,'Valor':valor})
    historico.append({'Ação':'Cadastro Artesanal', 'Item': produto, 'Quantidade': quantidade, 'Valor':valor})
    print('\033[1;34mProduto cadastrado com sucesso!\033[m')
    ultimo = produtos[-1]
    print('\033[1;35m~'*100,'\033[m')
    print(f"\033[1;35mProduto:\033[m {ultimo['Produto']}")
    print(f"\033[1;35mQuantidade:\033[m {ultimo['Quantidade']} {ultimo['Unidade']}")
    print(f"\033[1;35mValor:\033[m R${ultimo['Valor']}")
    print('\033[1;35m~'*100,'\033[m')
# 
def lista_produtos():
    if len(animais) == 0:
        print('\033[1;31mNenhum produto cadastrado ainda!\033[m')
    else:
        for i in produtos:
            print(f'\033[1;35mProduto:\033[m {i["Produto"]}')
            print(f'\033[1;35mQuantidade:\033[m {i["Quantidade"]} {i["Unidade"]}')
            print(f'\033[1;35mValor:\033[m R${i["Valor"]}')
            print('\033[1;35m~'*100,'\033[m')

def alterar_remover_produto():
    print('\033[1;32m~\033[m'*100)
    print('[\033[1;33m1\033[m]ALTERAR\n[\033[1;33m2\033[m]REMOVER')
    print('\033[1;32m~\033[m'*100) 
    remover_alterar = input('Digite a opção que você deseja: ')
    if remover_alterar == '1':
        print('\033[1;32m~\033[m'*100)    
        print('\033[1;32m~'*42, 'MENU ALTERAÇÃO','~'*42,'\033[m')
        print('\033[1;32m~'*100,'\033[m')
        alteracao = input('Qual produto você deseja alterar? ').capitalize()
        for i in produtos:
            if i['Produto'] == alteracao:
                print(f'\033[1;35mProduto:\033[m {i["Produto"]}')
                print(f'\033[1;35mQuantidade:\033[m {i["Quantidade"]} {i["Unidade"]}')
                print(f'\033[1;35mValor:\033[m R${i["Valor"]}')
                print('\033[1;35m~'*100,'\033[m')
                print('[\033[1;33m1\033[m]PRODUTO\n[\033[1;33m2\033[m]PESO/VOLUME\n[\033[1;33m3\033[m]UNIDADE\n[\033[1;33m4\033[m]VALOR')
                escolha_alteracao = input('Digite o que você deseja alterar: ')
                if escolha_alteracao == '1':
                    tipo_alteracao = input(f'Digite o produto que você deseja substituir no lugar de {i["Produto"]}: ').capitalize()
                    i['Produto'] = tipo_alteracao
                    print('Produto alterado com sucesso!')
                    break
                elif escolha_alteracao == '2':
                    peso_alteracao = float(input(f'Digite o peso/volume que você deseja substituir no lugar de {i["Quantidade"]}:'))
                    i['Quantidade'] = peso_alteracao
                    print('\033[1;34mProduto alterado com sucesso!\033[m')
                    break
                elif escolha_alteracao == '3':
                    unidade_alteracao = input(f'Digite a unidade que você deseja substituir no lugar de {i["Unidade"]}: ')
                    i['Unidade'] = unidade_alteracao
                    print('\033[1;34mProduto alterado com sucesso!\033[m')
                    break
                elif escolha_alteracao == '4':
                    valor_alteracao = input(f'Digite o valor que você deseja substituir no lugar de {i["Valor"]}: ')
                    i['Valor'] = valor_alteracao
                    print('\033[1;34mProduto alterado com sucesso!\033[m')
                    break
                historico.append({'Ação':'Alteração Produto', 'Item': i['Produto'], 'Quantidade': 1, 'Valor':i['Valor']})
        else:
            print('\033[1;31mProduto não encontrado!\033[m')
    elif remover_alterar == '2':
        print('\033[1;32m~\033[m'*100)    
        print('\033[1;32m~'*43, 'MENU REMOÇÃO','~'*43,'\033[m')
        print('\033[1;32m~'*100,'\033[m')
        remover = input('Digite o produto que você deseja remover: ').capitalize()
        for i in produtos:
            if i['Produto'] == remover:
                print(f'\033[1;35mProduto:\033[m {i["Produto"]}')
                print(f'\033[1;35mQuantidade:\033[m {i["Quantidade"]} {i["Unidade"]}')
                print(f'\033[1;35mValor:\033[m R${i["Valor"]}')
                print('\033[1;35m~'*100,'\033[m')
                produtos.remove(i)
                print('\033[1;34mProduto removido com sucesso!\033[m')
                break
            historico.append({'Ação':'Remoção Produto', 'Item': i['Produto'], 'Quantidade': 1, 'Valor':i['Valor']})
        else:
            print('\033[1;32mProduto não encontrado!\033[m')
    else:
        print('\033[1;31mOpção inválida!\033[m')

# conversor
def conversor_queijo():
    print('\033[1;32m~'*100,'\033[m')
    print('[\033[1;33m1\033[m]COALHO\n[\033[1;33m2\033[m]QUEIJO MANTEIGA\n[\033[1;33m3\033[m]MUSSARELA\n[\033[1;33m4\033[m]REQUEIJÃO')
    decisao = input('Digite a opção de queijo que deseja fabricar: ')
    if decisao == '1':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 10
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao} \033[1;35mkg de queijo, serão necessários\033[m {leite_necessario:.2f} \033[1;35mlitros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite["Volume"] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite["Volume"] >= leite_necessario:
                leite["Volume"] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Coalho','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Queijo', 'Item': 'Coalho', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
# 

    elif decisao == '2':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('Quantidade inexistente! Tente novamente.')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 10
        print(f'\033[1;35mPara fabricar \033[m{quantidade_producao} \033[1;35mkg de queijo, serão necessários\033[m {leite_necessario:.2f} \033[1;35mlitros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite["Volume"] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite["Volume"] >= leite_necessario:
                leite["Volume"] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Queijo Manteiga','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Queijo', 'Item': 'Manteiga', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
# 
    elif decisao == '3':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('Quantidade inexistente! Tente novamente.')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 10
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao}\033[1;35m kg de queijo, serão necessários\033[m {leite_necessario:.2f} \033[1;35mlitros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite['Volume'] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite['Volume'] >= leite_necessario:
                leite['Volume'] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Mussarela','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Queijo', 'Item': 'Mussarela', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
# 
    elif decisao == '4':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('Quantidade inexistente! Tente novamente.')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 10
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao}\033[1;35m kg de queijo, serão necessários\033[m {leite_necessario:.2f} \033[1;35mlitros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite['Volume'] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite['Volume'] >= leite_necessario:
                leite['Volume'] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Requeijão','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Queijo', 'Item': 'Requeijão', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
    else:
        print('\033[1;31mOpção inválida!\033[m')
# 

def conversor_derivados():
    print('\033[1;32m~'*100,'\033[m')
    print('[\033[1;33m1\033[m]MANTEIGA COMUM\n[\033[1;33m2\033[m]CREME DE LEITE\n[\033[1;33m3\033[m]IOGURTE\n[\033[1;33m4\033[m]DOCE DE LEITE\n[\033[1;33m5\033[m]COALHADA')
    decisao = input('Digite a opção de queijo que deseja fabricar: ')
    if decisao == '1':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 5
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao}\033[1;35m kg de manteiga, serão necessários\033[m {leite_necessario:.2f}\033[1;35m litros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite["Volume"] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite["Volume"] >= leite_necessario:
                leite["Volume"] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Manteiga','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Derivado', 'Item': 'Manteiga', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
# 
    elif decisao == '2':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 5
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao} \033[1;35mlitros de creme de leite, serão necessários \033[m{leite_necessario:.2f} \033[1;35mlitros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite['Volume'] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite['Volume'] >= leite_necessario:
                leite['Volume'] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produtos':'Creme de Leite','Unidade':quantidade_producao,'Unidade':'L','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Derivado', 'Item': 'Creme de Leite', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
# 
    elif decisao == '3':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 1
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao}\033[1;35m litro de iogurte, serão necessários \033[m{leite_necessario:.2f}\033[1;35m litros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite['Volume'] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite['Volume'] >= leite_necessario:
                leite['Volume'] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Iogurte','Quantidade':quantidade_producao,'Unidade':'L','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Derivado', 'Item': 'Iorgute', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
# 
    elif decisao == '4':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 5
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao}\033[1;35m kg de doce de leite, serão necessários\033[m {leite_necessario:.2f}\033[1;35m litros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite['Volume'] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite['Volume'] >= leite_necessario:
                leite['Volume'] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Doce de Leite','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Derivado', 'Item': 'Doce de Leite', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
# 
    elif decisao == '5':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 1.25
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao} \033[1;35mkg de coalhada, serão necessários\033[m {leite_necessario:.2f}\033[1;35m litros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite['Volume'] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite['Volume'] >= leite_necessario:
                leite['Volume'] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Coalhada','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Derivado', 'Item': 'Coalhada', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
    else:
        print('\033[1;31mOpção inválida!\033[m')
# 
def conversor_artesanais():
    print('\033[1;32m~\033[m'*100)
    print('[\033[1;33m1\033[m]MANTEIGA DA TERRA\n[\033[1;33m2\033[m]QUEIJO DEFUMADO[\033[1;33m3\033[m]NATA')
    decisao = input('Digite a opção de queijo que deseja fabricar: ')
    if decisao == '1':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 10
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao}\033[1;35m kg de manteiga da terra, serão necessários\033[m {leite_necessario:.2f}\033[1;35m litros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite['Volume'] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite['Volume'] >= leite_necessario:
                leite['Volume'] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Manteiga da Terra','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Artesanais', 'Item': 'Manteiga da Terra', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
# 
    elif decisao == '2':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 11.1
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao}\033[1;35m kg de queijo defumado, serão necessários\033[m {leite_necessario:.2f}\033[1;35m litros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite['Volume'] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite['Volume'] >= leite_necessario:
                leite['Volume'] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Queijo Defumado','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Artesanais', 'Item': 'Queijo Defumado', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
# 
    elif decisao == '3':
        while True:
            quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
            if quantidade_producao <=0:
                print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                continue
            else:
                break
        leite_necessario = quantidade_producao * 6.6
        print(f'\033[1;35mPara fabricar\033[m {quantidade_producao}\033[1;35m kg de nata, serão necessários\033[m {leite_necessario} \033[1;35mlitros de leite!\033[m')
        print(f'\033[1;35mQuantidade no estoque:\033[m {leite["Volume"]}')
        confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip().upper()
        if confirmacao == 'S':
            if leite['Volume'] < leite_necessario:
                print('\033[1;31mQuantidade no estoque indisponível para fabrição!\033[m')
            elif leite['Volume'] >= leite_necessario:
                leite['Volume'] -= leite_necessario
                valor_sub = float(input('Qual o valor para venda desse produto? '))
                produtos.append({'Produto':'Nata','Quantidade':quantidade_producao,'Unidade':'kg','Valor':valor_sub})
                historico.append({'Ação':'Conversão de Artesanais', 'Item': 'Nata', 'Quantidade':quantidade_producao, 'Valor':valor_sub})
                print('\033[1;34mConversão realizada com sucesso!\033[m')
        else:
            print('\033[1;31mConversão cancelada!\033[m')
    else:
        print('\033[1;31mOpção inválida!\033[m')
# 
def producao_diaria():
    print('\033[1;32m~'*100)
    print('~'*42,'PRODUÇÃO DIÁRIA','~'*41)
    print('~'*100,'\033[m')
    print(f'\033[1;35mEstoque atual:\033[m{leite["Volume"]}')
    while True:
        print('\033[1;32m~\033[m'*100)
        print('[\033[1;33m1\033[m]ADICIONAR\n[\033[1;33m2\033[m]REMOVER\n[\033[1;33m3\033[m]SAIR')
        escolha_leite = input('Digite a opção que deseja: ')
        if escolha_leite == '1':
            while True:
                producao_diaria = float(input('Digite a quantidade de leite ordenhado do dia: '))
                if producao_diaria <= 0 :
                    print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                    continue
                else:
                    break
            leite['Volume'] += producao_diaria
            valor_diaria = float(input('Digite o valor do leite atualizado: '))
            leite['Valor']+= valor_diaria 
            historico.append({'Ação':'Produção D. de Leite', 'Item':'Leite', 'Quantidade': producao_diaria,'Valor': valor_diaria})      
            print(f'\033[1;34mProdução diária cadastrada com sucesso!\033[m\n\033[1;35mEstoque atual:\033[m {leite["Volume"]}')
        elif escolha_leite == '2':
            leite_remover = float(input('Digite a quantidade de leite que você deseja remover: '))
            leite['Volume'] -= leite_remover
            historico.append({'Ação':'Remoção de Leite', 'Item':'Leite', 'Quantidade': producao_diaria,'Valor': valor_diaria})
            print(f'\033[1;34mQuantidade de leite removida com sucesso!\033[m\n\033[1;35mEstoque atual:\033[m {leite["Volume"]}')
        elif escolha_leite == '3':
            break
        else:
            print('\033[1;31mOpção inválida!\033[m')

def historico_movimentacao():
    print('\033[1;32m~'*100)
    print('~'*36,'HISTÓRICO DE MOVIMENTAÇÃO','~'*37)
    print('~'*100,'\033[m')
    if len(historico) == 0:
        print('\033[1;31mNenhuma movimentação registrada!\033[m')
    else:
        for item in historico:
            print('\033[1;35m~'*100,'\033[m')
            print(f"\033[1;35mAção:\033[m {item['Ação']}")
            print(f"\033[1;35mItem:\033[m {item['Item']}")
            print(f"\033[1;35mQuantidade:\033[m {item['Quantidade']}")
            print(f"\033[1;35mValor:\033[m R${item['Valor']}")
    print('\033[1;35m~'*100,'\033[m')

def relatorio_geral():
    print('\033[1;32m~'*100)
    print('~'*37,'RELATÓRIO GERAL','~'*37)
    print('~'*100,'\033[m')
    print('\n\033[1;35mESTOQUE DE ANIMAIS\033[m')
    print(f'\033[1;35mTotal de animais cadastrados:\033[m {len(animais)}')
    if len(animais) == 0:
        print('\033[1;31mNenhum produto cadastrado.\033[m')
    else:
        for item in animais:
            print('\033[1;35m~'*100,'\033[m')
            print(f"\033[1;35mBrinco:\033[m {item['Brinco']}")
            print(f"\033[1;35mAnimal:\033[m {item['Animal']}")
            print(f"\033[1;35mPeso:\033[m {item['Peso']}")
            print(f"\033[1;35mGênero:\033[m {item['Gênero']}")
            print(f"\033[1;35mStatus:\033[m {item['Status']}")
            print(f"\033[1;35mValor:\033[m R${item['Valor']}")
            print('\033[1;35m~' * 100,'\033[m')

    print('\n\033[1;35mESTOQUE DE LEITE\033[m')
    print('\033[1;35m~'*100)
    print(f'\033[1;35mVolume: \033[m{leite["Volume"]} litros\033[m')
    print(f'\033[1;35mValor: \033[mR$ {leite["Valor"]}')
    print('\033[1;35m~'*100)

    print('\n\033[1;35mESTOQUE DE PRODUTOS\033[m')
    print(f'\033[1;35mTotal de produtos cadastrados:\033[m {len(produtos)}')
    if len(produtos) == 0:
        print('\033[1;31mNenhum produto cadastrado.\033[m')
    else:
        for produto in produtos:
            print('\033[1;35m~'*100,'\033[m')
            print(f"\033[1;35mProduto:\033[m {produto['Produto']}")
            print(f"\033[1;35mQuantidade:\033[m {produto['Quantidade']}")
            print(f"\033[1;35mUnidade:\033[m {produto['Unidade']}")
            print(f"\033[1;35mValor:\033[m R$ {produto['Valor']}")
    print('\033[1;35m~'*100,'\033[m')

def voltar():
    print('\033[1;31mVoltando ao menu anterior...\033[m')
'''

while True:
        
        print(Fore.GREEN + """                                                 ▀██            
▄ ▄▄ ▄▄▄     ▄▄▄  ▄ ▄▄▄   ▄▄▄ ▄▄       ▄▄▄     ▄▄ ██  ▄ ▄▄ ▄▄▄  
 ██ ██ ██  ▄██ ██  ██ ██   ██ █       ▀▀▄██  ▄██ ▀██   ██ ██ ██ 
 ██ ██ ██  ██▀▀▀▀  ██ ██   ██ █       ▄█ ██  ██▌  ██   ██ ██ ██ 
▄██ ██ ██▄  ▀█▄▄▀ ▄██ ██▄  ▀█▄▀▄      ▀█▄▀▀▄  ▀█▄▀██▄ ▄██ ██ ██▄  """)

        print('\033[m[\033[1;33m1\033[m] CADASTRAR ANIMAIS\n''[\033[1;33m2\033[m] LISTAR ANIMAIS\n''[\033[1;33m3\033[m] ALTERAR/REMOVER ANIMAIS\n''[\033[1;33m4\033[m] CADASTRAR QUEIJOS\n''[\033[1;33m5\033[m] CADASTRAR LEITE\n''[\033[1;33m6\033[m] CADASTRAR DERIVADOS\n''[\033[1;33m7\033[m] CADASTRAR ARTESANAIS\n''[\033[1;33m8\033[m] LISTAR PRODUTOS\n''[\033[1;33m9\033[m] ALTERAR/REMOVER PRODUTOS\n''[\033[1;33m10\033[m] CONVERSOR DE QUEIJOS\n''[\033[1;33m11\033[m] CONVERSOR DE DERIVADOS\n''[\033[1;33m12\033[m] CONVERSOR ARTESANAIS\n''[\033[1;33m13\033[m] PRODUÇÃO DIÁRIA\n''[\033[1;33m14\033[m] HISTÓRICO DE MOVIMENTAÇÃO\n''[\033[1;33m15\033[m] RELATÓRIO GERAL\n'
              '[\033[1;33m16\033[m] VOLTAR')
        op_adm = int(input('\nDigite a opção desejada: '))
        if op_adm == 1:
            cadastro_animais()
        elif op_adm == 2:
            lista_animais()
        elif op_adm == 3:
            alterar_remover_animal()
        elif op_adm == 4:
            cadas_queijo()
        elif op_adm == 5:
            cadas_leite()
        elif op_adm == 6:
            cadas_derivado()
        elif op_adm == 7:
            cadas_artesanal()
        elif op_adm == 8:
            lista_produtos()
        elif op_adm == 9:
            alterar_remover_produto()
        elif op_adm == 10:
            conversor_queijo()
        elif op_adm == 11:
            conversor_derivados()
        elif op_adm == 12:
            conversor_artesanais()
        elif op_adm == 13:
            producao_diaria()
        elif op_adm == 14:
            historico_movimentacao()
        elif op_adm == 15:
            relatorio_geral()
        elif op_adm == 16:
            voltar()
'''
            