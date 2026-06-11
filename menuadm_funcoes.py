# funções adm
animais = []
produtos = []
leite = {'Produto':'Leite','Volume':1000,'Valor':5.5}
def cadastro_animais():
    print('\033[1;32m~'*40,'CADASTRO DE ANIMAIS','~'*39, '\033[m')
    animal = input('Digite o animal que você deseja cadastrar: ').capitalize()
    while True:
        peso = float(input('Digite o peso do animal: '))
        if peso <= 0 :
            print('\033[1;31mEsse peso é inválido para o animal, tente novamente!\033[m')
            continue
        else:
            break
    genero = input('Digite o gênero do animal: ')
    status = input('Digite o status do animal: ')
    while True:
        valor = float(input('Digite o valor do animal: '))
        if valor <= 0 :
            print('\033[1;31mEsse valor é inválido para o animal, tente novamente!\033[m')
            continue
        else:
            break 
    animais.append({'Animal':animal,'Peso':peso,'Gênero':genero,'Status':status,'Valor':valor})
    print('\033[1;34mAnimal cadastrado com sucesso!\033[m')
    for item in animais:
        print(f"\033[1;35mAnimal:\033[m {item['Animal']}")
        print(f"\033[1;35mPeso:\033[m {item['Peso']}")
        print(f"\033[1;35mGênero:\033[m {item['Gênero']}")
        print(f"\033[1;35mStatus:\033[m {item['Status']}")
        print(f"\033[1;35mValor:\033[m R${item['Valor']}")
        print('\033[1;35m~' * 100,'\033[m')

def lista_animais():
    if len(animais) == 0:
        print('\033[1;31mNenhum animal cadastrado ainda!\033[m')
    else:
        print('\033[1;32m~'*100)
        print('~' *35,'LISTA DE ANIMAIS CADASTRADOS', '~' *35)
        print('~'*100, '\033[m')
        for item in animais:
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
                alteracao = input('Qual animal você deseja alterar? ').capitalize()
                for i in animais:
                    if i['Animal'] == alteracao:
                            print(f"\033[1;35mAnimal:\033[m {i['Animal']}")
                            print(f"\033[1;35mPeso:\033[m {i['Peso']}")
                            print(f"\033[1;35mGênero:\033[m {i['Gênero']}")
                            print(f"\033[1;35mStatus:\033[m {i['Status']}")
                            print(f"\033[1;35mValor:\033[m R${i['Valor']}")
                            print('\033[1;35m~\033[m'*100)
                            print('[\033[1;33m1\033[m]TIPO ANIMAL\n[\033[1;33m2\033[m]PESO\n[\033[1;33m3\033[m]GÊNERO\n[\033[1;33m4\033[m]STATUS\n[\033[1;33m5\033[m]VALOR')
                            escolha_alteracao = input('Digite o que você deseja alterar: ')
                            if escolha_alteracao == '1':
                                tipo_alteracao = input(f"Digite o nome que você deseja substituir no lugar de: {i['Animal']}>  ")
                                i['Animal'] = tipo_alteracao
                                print('\033[1;34mAnimal alterado com sucesso!\033[m')
                                break
                            elif escolha_alteracao == '2':
                                peso_alteracao = float(input(f"Digite o peso que você deseja substituir no lugar de: {i['Peso']}> "))
                                i['Peso'] = peso_alteracao
                                print('\033[1;34mAnimal alterado com sucesso!\033[m')
                                break
                            elif escolha_alteracao == '3':
                                genero_alteracao = input(f"Digite o gênero que você deseja substituir no lugar de: {i['Gênero']}>  ")
                                i['Gênero'] = genero_alteracao
                                print('\033[1;34mAnimal alterado com sucesso!\033[m')
                                break
                            elif escolha_alteracao == '4':
                                status_alteracao = input(f"Digite o status que você deseja substituir no lugar de: {i['Status']}>  ")
                                i['Status'] = status_alteracao
                                print('\033[1;34mAnimal alterado com sucesso!\033[m')
                                break
                            elif escolha_alteracao == '5':
                                valor_alteracao = float(input(f"Digite o valor que você deseja substituir no lugar de: {i['Valor']}>  "))
                                i['Valor'] = valor_alteracao
                                print('\033[1;34mAnimal alterado com sucesso!\033[m')
                                break
                else:
                    print('\033[1;31mAnimal não encontrado!\033[m')
            elif remover_alterar == '2':
                print('\033[1;32m~\033[m'*100)    
                print('\033[1;32m~'*43, 'MENU REMOÇÃO','~'*43,'\033[m')
                print('\033[1;32m~'*100,'\033[m')
                remover = input('Digite o animal que você deseja remover: ').capitalize()
                for i in animais:
                    if i['Animal'] == remover:
                        print(f"\033[1;35mAnimal:\033[m {i['Animal']}")
                        print(f"\033[1;35mPeso:\033[m {i['Peso']}")
                        print(f"\033[1;35mGênero:\033[m {i['Gênero']}")
                        print(f"\033[1;35mStatus:\033[m {i['Status']}")
                        print(f"\033[1;35mValor:\033[m R${i['Valor']}")
                        print('\033[1;35m~' * 100,'\033[m')
                        animais.remove(i)
                        print('\033[1;34mAnimal removido com sucesso!\033[m')
                        break
                else:
                    print('\033[1;31mAnimal não encontrado!\033[m')

# cadastro de produtos
def cadas_queijo():
    print('\033[1;32m~\033[m'*100)
    produto = input('Digite o tipo de queijo que você deseja cadastrar: ').capitalize()
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
    print('\033[1;34mProduto cadastrado com sucesso!\033[m')
    for i in produtos:
        print(f'\033[1;35mProduto:\033[m {i["Produto"]}')
        print(f'\033[1;35mQuantidade:\033[m {i["Quantidade"]} {i["Unidade"]}')
        print(f'\033[1;35mValor:\033[m R${i["Valor"]}')
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
    print('\033[1;34mProduto cadastrado com sucesso!\033[m')
    for i in produtos:
        print(f'\033[1;35mProduto:\033[m {i["Produto"]}')
        print(f'\033[1;35mQuantidade:\033[m {i["Quantidade"]} {i["Unidade"]}')
        print(f'\033[1;35mValor:\033[m R${i["Valor"]}')
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
    print('\033[1;34mProduto cadastrado com sucesso!\033[m')
    for i in produtos:
        print(f'\033[1;35mProduto:\033[m {i["Produto"]}')
        print(f'\033[1;35mQuantidade:\033[m {i["Quantidade"]} {i["Unidade"]}')
        print(f'\033[1;35mValor:\033[m R${i["Valor"]}')
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
        else:
            print('\033[1;32mProduto não encontrado!\033[m')

# conversor
def conversor_queijo():
    print('\033[1;32m~\033[m'*100)
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
                produtos.append(['Queijo Manteiga',quantidade_producao,'kg',valor_sub])
                print('Conversão realizada com sucesso!')
        else:
            print('Conversão cancelada!')
