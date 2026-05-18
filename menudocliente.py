compras = []
encomendas = []
produtos = [['Leite',5,'litros',8.0]]

while True:
    print('~' * 100)
    print('~' *43,'MENU CLIENTE', '~' *43)
    print('~' * 100)
    print('[1] VER PRODUTOS')
    print('[2] COMPRAR PRODUTOS')
    print('[3] ENCOMENDAR PRODUTOS')
    print('[4] VER ENCOMENDAS')
    print('[5] HISTÓRICOS DE COMPRAS')
    print('[6] BENEFÍCIOS DO CLIENTE')
    print('[7] FORMAS DE PAGAMENTO')
    print('[8] VOLTAR')

    op_cliente = int(input('Digite a opção desejada: '))

    if op_cliente == 1:
        if len(produtos) == 0:
            print('Nenhum produto cadastrado!')

        else:
            print('~'*100)
            print('~' *41,'LISTA DE PRODUTOS', '~' *40)
            print('~'*100)
            for produto, quantidade, unidade, valor in produtos:
                print(f'Produto: {produto}')
                print(f'Quantidade: {quantidade} {unidade}')
                print(f'Valor: {valor}')
                print('-' * 30)

    elif op_cliente == 2:
        print('~'*100)
        print('~' *41,'COMPRAR PRODUTOS', '~' *41)
        print('~'*100)
        produto = input('Digite o produto que deseja comprar: ')
        produto_input = input('Digite o produto que deseja comprar: ')

    encontrado = False

    for item in produtos:

        if item[0].lower() == produto_input.lower():

            encontrado = True

            quantidade = int(input('Digite a quantidade desejada: '))

            if quantidade > item[1]:

                print('Quantidade indisponível em estoque!')

                print(f'Estoque disponível: {item[1]} {item[2]}')

            else:

                unidade = item[2]

                valor = item[3]

                valor_total = quantidade * valor

                if len(compras) >= 3:

                    desconto = valor_total * 0.10

                    valor_final = valor_total - desconto

                    print(f'Desconto aplicado: {desconto}')

                else:

                    valor_final = valor_total

                print(f'Valor final: {valor_final}')

                item[1] -= quantidade

                compras.append([produto_input, quantidade, unidade, valor_final])

                print('Compra realizada com sucesso!')

            break

    if encontrado == False:

        print('Produto não encontrado!')

    elif op_cliente == 3:
        print('~'*100)
        print('~' *40,'ENCOMENDAR PRODUTOS', '~' *39)
        print('~'*100)
        produto = input('Digite o produto que deseja encomendar: ')
        quantidade = int(input('Digite a quantidade desejada: '))
        data = input('Digite a data desejada: ')
        horario = input('Digite o horário desejado: ')

        encomendas.append([produto, quantidade, data, horario])

        print('Encomenda realizada com sucesso!')

    elif op_cliente == 4:

        if len(encomendas) == 0:
            print('Nenhuma encomenda realizada!')

        else:
            print('~'*100)
            print('~' *40,'LISTA DE ENCOMENDAS', '~' *39)
            print('~'*100)

            for produto, quantidade, data, horario in encomendas:
                print(f'Produto: {produto}')
                print(f'Quantidade: {quantidade}')
                print(f'Data: {data}')
                print(f'Horário: {horario}')
                print('-' * 30)

    elif op_cliente == 5:
        print('~'*100)
        print('~'*40,'HISTÓRICOS DE COMPRAS','~'*37)
        print('~'*100)
        if len(compras) == 0:
            print('Nenhuma encomenda realizada!')
        else:
            for i in compras:
                print(i)

    elif op_cliente == 6:
        print('~'*100)
        print('~'*40,'BENEFÍCIOS DO CLIENTE','~'*37)
        print('~'*100)
        if len(compras) >= 3:
            print('Você já possui direito aos 10% de desconto nas compras.')
            
        else: 
            faltam = 3 - len(compras)
            print(f'Faltam {faltam} compras para liberar os 10% de desconto.')

    elif op_cliente == 7:
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
    
    
    elif op_cliente == 8:
        print('Voltar ao menu inicial...')
        break