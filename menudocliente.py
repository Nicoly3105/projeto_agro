compras = []
encomendas = []
produtos = []

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
    print('[7] VOLTAR')

    op_cliente = int(input('Digite a opção desejada: '))

    if op_cliente == 1:
        if len(produtos) == 0:
            print('Nenhum produto cadastrado!')

        else:
            print('~' *35,'LISTA DE PRODUTOS', '~' *35)
            for produto, quantidade in produtos:
                print(f'Produto: {produto}')
                print(f'Quantidade: {quantidade}')
                print('-' * 30)

    # COMPRAR PRODUTOS
    elif op_cliente == 2:
        print('~' *35,'COMPRAR PRODUTOS', '~' *35)
        produto = input('Digite o produto que deseja comprar: ')
        quantidade = int(input('Digite a quantidade desejada: '))

        produtos.append([produto, quantidade])
        compras.append([produto, quantidade])

        print('Compra realizada com sucesso!')


    # ENCOMENDAR PRODUTOS
    elif op_cliente == 3:
        print('~' *35,'ENCOMENDAR PRODUTOS', '~' *35)
        produto = input('Digite o produto que deseja encomendar: ')
        quantidade = int(input('Digite a quantidade desejada: '))
        data = input('Digite a data desejada: ')
        horario = input('Digite o horário desejado: ')

        encomendas.append([produto, quantidade, data, horario])

        print('Encomenda realizada com sucesso!')

    # VER ENCOMENDAS
    elif op_cliente == 4:

        if len(encomendas) == 0:
            print('Nenhuma encomenda realizada!')

        else:
            print('~' *35,'LISTA DE ENCOMENDAS', '~' *35)

            for produto, quantidade, data, horario in encomendas:
                print(f'Produto: {produto}')
                print(f'Quantidade: {quantidade}')
                print(f'Data: {data}')
                print(f'Horário: {horario}')
                print('-' * 30)

    elif op_cliente == 5:
        print('~'*35,'HISTÓRICOS DE COMPRAS','~'*35)
        if len(compras) == 0:
            print('Nenhuma encomenda realizada!')
        else:
            for i in compras:
                print(i)
    elif op_cliente == 6:
        print('~'*35,'BENEFÍCIOS DO CLIENTE','~'*35)
        if len(compras) >= 3:
            print('Parabéns! Você possui 10% de desconto nas compras.')
        else: 
            faltam = 3 - len(compras)
            print(f'Faltam {faltam} compras para liberar os 10% de desconto.')
    elif op_cliente == 7:
        print('Voltando ao menu inicial...')
        break
                   