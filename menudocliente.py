compras = []
encomendas = []
produtos = []

while True:
    print('~' * 100)
    print('~' * 43, 'MENU CLIENTE', '~' * 43)
    print('~' * 100)

    print('[1] Ver produtos')
    print('[2] Comprar produtos')
    print('[3] Encomendar produtos')
    print('[4] Ver encomendas')
    print('[5] Voltar')

    op_cliente = int(input('Digite a opção desejada: '))

    # VER PRODUTOS
    if op_cliente == 1:

        if len(produtos) == 0:
            print('Nenhum produto cadastrado!')

        else:
            print('~' * 35, 'LISTA DE PRODUTOS', '~' * 35)

            for produto, quantidade in produtos:
                print(f'Produto: {produto}')
                print(f'Quantidade: {quantidade}')
                print('-' * 30)

    # COMPRAR PRODUTOS
    elif op_cliente == 2:
        produto = input('Digite o produto que deseja comprar: ')
        quantidade = int(input('Digite a quantidade desejada: '))

        produtos.append([produto, quantidade])
        compras.append([produto, quantidade])

        print('Compra realizada com sucesso!')

    # ENCOMENDAR PRODUTOS
    elif op_cliente == 3:
        produto = input('Digite o produto que deseja encomendar: ')
        quantidade = float(input('Digite a quantidade desejada: '))
        data = input('Digite a data desejada: ')
        horario = input('Digite o horário desejado: ')

        encomendas.append([produto, quantidade, data, horario])

        print('Encomenda realizada com sucesso!')

    # VER ENCOMENDAS
    elif op_cliente == 4:

        if len(encomendas) == 0:
            print('Nenhuma encomenda realizada!')

        else:
            print('~' * 35, 'LISTA DE ENCOMENDAS', '~' * 35)

            for produto, quantidade, data, horario in encomendas:
                print(f'Produto: {produto}')
                print(f'Quantidade: {quantidade}')
                print(f'Data: {data}')
                print(f'Horário: {horario}')
                print('-' * 30)

    # VOLTAR
    elif op_cliente == 5:
        print('Voltando ao menu inicial...')
        break

    else:
        print('Opção inválida!')