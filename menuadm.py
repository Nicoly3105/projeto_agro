animais = [['vaca',37,'femea','gravida',8]]
produtos = [['coalho',7,'kg',6.5]]
leite = [1000]
while True:
    print('~'*100)
    print('~'*45,'MENU ADM','~'*45)
    print('~'*100)
    print('[1]CADASTRAR ANIMAL\n[2]VER ANIMAIS\n[3]CADASTRAR PRODUTO\n[4]VER PRODUTOS\n[5]CONVERSOR DE FABRICAÇÃO\n[6]VOLTAR')
    op_adm = int(input('Digite a opção que deseja para prosseguir: ')).strip

    if op_adm == 1:
                print('~'*40,'CADASTRO DE ANIMAIS','~'*39)
                animal = input('Digite o animal que você deseja cadastrar: ')
                while True:
                    peso = float(input('Digite o peso do animal: '))
                    if peso <= 0 :
                        print('Esse peso é inválido para o animal, tente novamente!')
                        continue
                    else:
                          break
                genero = input('Digite o gênero do animal: ')
                while True:
                    quantidade = int(input('Digite a quantidade de animais que você quer cadastrar: '))
                    if quantidade <= 0:
                          print('Essa quantidade é inválida para o animal, tente novamente!')
                          continue
                    else:
                          break
                status = input('Digite o status do animal: ')
                while True:
                    valor = float(input('Digite o valor do animal: '))
                    if valor <= 0 :
                          print('Esse valor é inválido para o animal, tente novamente!')
                          continue
                    else:
                       break 
                animais.append([animal,peso,genero,quantidade,status,valor])

    elif op_adm == 2:
            print('~'*35,'~LISTA DE ANIMAIS CADASTRADOS~','~'*35)
            for i in animais:
                print(i)

    elif op_adm == 3:
        while True:
            print('~'*100)
            print('~'*44,'CATEGORIAS','~'*44)
            print('~'*100)
            print('[1]QUEIJOS\n[2]LEITE\n[3]DERIVADOS\n[4]PRODUTOS PARA VENDA EM LOTE\n[5]PRODUTOS ARTESANAIS\n[6]VOLTAR')
            op_categoria = int(input('Digite a opção que deseja para prosseguir: ')).strip
            if op_categoria == 1:
                    produto = input('Digite o tipo de queijo que você deseja cadastrar: ')
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
                    produto = input('Digite o tipo de derivado que você deseja cadastrar: ')
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
                    produto = input('Digite o tipo de produto para venda em lote que você deseja cadastrar: ')
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
                    produto = input('Digite o tipo de produto artesanal que você deseja cadastrar: ')
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

    elif op_adm == 4:
        for i in produtos:
            print(i)

    elif op_adm == 5:
         print('~'*38,'CONVERSOR DE FABRICAÇÃO','~'*39)
         print('[1]QUEIJO\n[2]DERIVADOS\n[3]ARTESANAIS')
         escolha = input('Qual produto você deseja fabricar? ').strip
    if escolha == '1':
                print('~'*100)
                print('[1]COALHO\n[2]QUEIJO MANTEIGA[3]MUSSARELA\n[4]REQUEIJÃO')
                decisao = input('Digite a opção de queijo que deseja fabricar: ').strip
                if decisao == '1':
                    while True:
                        quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                        if quantidade_producao <=0:
                            print('Quantidade inexistente! Tente novamente.')
                            continue
                        else:
                            break
                    leite_necessario = quantidade_producao * 10
                    print(F'Para fabricar {quantidade_producao} kg de queijo, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
                    print(F'Para fabricar {quantidade_producao} kg de queijo, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
                    print(F'Para fabricar {quantidade_producao} kg de queijo, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
                    print(F'Para fabricar {quantidade_producao} kg de queijo, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
        print('~'*100)
        print('[1]MANTEIGA COMUM\n[2]CREME DE LEITE[3]IOGURTE\n[4]DOCE DE LEITE\n[5]COALHADA')
        decisao = input('Digite a opção de queijo que deseja fabricar: ').strip
        if decisao == '1':
                    while True:
                        quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                        if quantidade_producao <=0:
                            print('Quantidade inexistente! Tente novamente.')
                            continue
                        else:
                            break
                    leite_necessario = quantidade_producao * 5
                    print(F'Para fabricar {quantidade_producao} kg de manteiga, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
                    print(F'Para fabricar {quantidade_producao} litros de creme de leite, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
                    print(F'Para fabricar {quantidade_producao} litro de iogurte, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
                    print(F'Para fabricar {quantidade_producao} kg de doce de leite, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
                    print(F'Para fabricar {quantidade_producao} kg de coalhada, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
        print('~'*100)
        print('[1]MANTEIGA DA TERRA\n[2]QUEIJO DEFUMADO[3]NATA')
        decisao = input('Digite a opção de queijo que deseja fabricar: ').strip
        if decisao == '1':
                    while True:
                        quantidade_producao = float(input('Qual a quantidade que você deseja fabricar? '))
                        if quantidade_producao <=0:
                            print('Quantidade inexistente! Tente novamente.')
                            continue
                        else:
                            break
                    leite_necessario = quantidade_producao * 10
                    print(F'Para fabricar {quantidade_producao} kg de manteiga da terra, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
                    print(F'Para fabricar {quantidade_producao} kg de queijo defumado, serão necessários {leite_necessario:2f} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
                    print(F'Para fabricar {quantidade_producao} kg de nata, serão necessários {leite_necessario} litros de leite!')
                    confirmacao = input('Deseja fabricar mesmo assim?(S/N): ').strip.upper
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
    elif op_adm == 6:
         break