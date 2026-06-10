animais = [['Vaca',37,'femea','gravida',8]]
produtos = [['coalho',7,'kg',6.5]]
leite = [1000]
animal_existe = False
while True:
        print('\033[1;32m~'*100)
        print('~'*45,'MENU ADM','~'*45)
        print('~'*100)
        print('\033[m[\033[1;33m1\033[m]CADASTRAR ANIMAL\n[\033[1;33m2\033[m]VER ANIMAIS\n[\033[1;33m3\033[m]ALTERAR OU REMOVER ANIMAL\n[\033[1;33m4\033[m]CADASTRAR PRODUTO\n[\033[1;33m5\033[m]VER PRODUTOS\n[\033[1;33m6\033[m]ALTERAR OU REMOVER PRODUTO\n[\033[1;33m7\033[m]CONVERSOR DE FABRICAÇÃO\n[\033[1;33m8\033[m]PRODUÇÃO DIÁRIA\n[\033[1;33m9\033[m]SAIR')
        op_adm = int(input('Digite a opção que deseja para prosseguir: '))

        if op_adm == 1:
                    print('\033[1;32m~'*40,'CADASTRO DE ANIMAIS','~\033[m'*39)
                    animal = input('Digite o animal que você deseja cadastrar: ').capitalize()
                    while True:
                        peso = float(input('Digite o peso do animal: '))
                        if peso <= 0 :
                            print('Esse peso é inválido para o animal, tente novamente!')
                            continue
                        else:
                            break
                    genero = input('Digite o gênero do animal: ')
                    status = input('Digite o status do animal: ')
                    while True:
                        valor = float(input('Digite o valor do animal: '))
                        if valor <= 0 :
                            print('Esse valor é inválido para o animal, tente novamente!')
                            continue
                        else:
                            break 
                    animais.append([animal,peso,genero,status,valor])

        elif op_adm == 2:
            print('\033[1;32m~'*35,'~LISTA DE ANIMAIS CADASTRADOS~','~'*35)
            print('\033[1;32m~\033[m'*100)
            for animal, peso, genero, status, valor in animais:
                    print(f'\033[1;35mAnimal:\033[m {animal}')
                    print(f'\033[1;35mPeso:\033[m {peso}')
                    print(f'\033[1;35mGênero:\033[m {genero}')
                    print(f'\033[1;35mStatus:\033[m {status}')
                    print(f'\033[1;35mValor:\033[m R${valor}')
                    print('\033[1;32m~\033[m'*100)
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
                print('[\033[1;33m1\033[m]QUEIJOS\n[\033[1;33m2\033[m]LEITE\n[\033[1;33m3\033[m]DERIVADOS\n[\033[1;33m4\033[m]PRODUTOS ARTESANAIS\n[\033[1;33m5\033[m]VOLTAR')
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

                elif op_categoria == 4:
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
                elif op_categoria == 5:
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
            print('\033[1;32m~'*38,'CONVERSOR DE FABRICAÇÃO','~\033[m'*39)
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
            print('Voltando ao inicioo..')