compras = []
encomendas = []

def menu_cliente():
    while True:
        print('~' * 100)
        print('~' *43,'MENU CLIENTE', '~' *43)
        print('~' * 100)
        print('[1] VER PRODUTOS\n[2] COMPRAR PRODUTOS\n[3] ENCOMENDAR PRODUTOS\n[4] VER ANIMAIS\n[5] COMPRAR ANIMAL\n[6] ENCOMENDAR ANIMAL\n[7] VER ENCOMENDAS\n[8] COMPRAR LEITE\n[9] HISTÓRICOS DE COMPRAS\n[10] BENEFÍCIOS DO CLIENTE\n[11] FORMAS DE PAGAMENTO\n[12] VOLTAR')

        op_cliente = int(input('Digite a opção desejada: '))

        def ver_produtos():
            if len(produtos) == 0:
                print('Nenhum produto cadastrado!')

            else:
                print('~'*100)
                print('~' *41,'LISTA DE PRODUTOS', '~' *40)
                print('~'*100)
                for produto, quantidade, unidade, valor in produtos:
                    print(f'Produto: {produto}')
                    print(f'Quantidade: {quantidade} {unidade}')
                    print(f'Valor: R${valor}')
                    print('-' * 30)

        def comprar_produto():
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
                        valor_total = quantidade_compra * valor_compra
                        if len(compras) >= 3:
                            desconto = valor_total * 0.10
                            valor_final = valor_total - desconto
                            print(f'Desconto aplicado: {desconto}')

                        else:
                         valor_final = valor_total
                         print(f'Valor final: {valor_final}')
                         item[1] -= quantidade_compra
                         compras.append({'produto':produto_input,'quantidade':quantidade_compra,'unidade':unidade,'valor':valor_final})
                         print('Compra realizada com sucesso!')

                    break

            if encontrado == False:

                print('Produto não encontrado!')

        def encomendar_produto():
            print('~'*100)
            print('~' *40,'ENCOMENDAR PRODUTOS', '~' *39)
            print('~'*100)
            produto_input = input('Digite o produto que deseja encomendar: ').capitalize()
            encontrado = False 
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

            encomendas.append({'produto':produto_input,'quantidade':quantidade,'data':data,'horario':horario})

            print('Encomenda realizada com sucesso!')

        def ver_animais():
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

        def comprar_animal():
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
                        valor_total = quantidade_animal * valor_animal
                        if len(compras) >= 3:
                            desconto = valor_total * 0.10
                            valor_final = valor_total - desconto
                            print(f'Desconto aplicado: {desconto}')

                        else:
                            valor_final = valor_total
                            print(f'Valor final: {valor_final}')
                            item[1] -= quantidade_animal
                            compras.append({'animal':animal_input,'quantidade':quantidade_animal,'valor':valor_final})
                            print('Compra realizada com sucesso!')

                    break
            if encontrado == False:
                print('Animal não encontrado!')

        def ver_encomendas_animais():
            print('~'*100)
            print('~' *40,'ENCOMENDAR ANIMAIS', '~' *39)
            print('~'*100)
            animal_input = input('Digite o animal que deseja encomendar: ').capitalize()
            encontrado = False 
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

            encomendas.append({'animal':animal_input,'quantidade':quantidade,'data':data,'horario':horario})

            print('Encomenda realizada com sucesso!')

        def ver_encomendas():

            if len(encomendas) == 0:
                print('Nenhuma encomenda realizada!')

            else:
                print('~'*100)
                print('~' *40,'LISTA DE ENCOMENDAS', '~' *39)
                print('~'*100)

                for encomenda in encomendas:
                    if 'produto' in encomenda:
                        print(f"Produto: {encomenda['produto']}")

                    if 'animal' in encomenda:
                     print(f"Animal: {encomenda['animal']}")
                    print(f"Quantidade: {encomenda['quantidade']}")
                    print(f"Data: {encomenda['data']}")
                    print(f"Horário: {encomenda['horário']}")
                    print('-'*100)

        def comprar_leite():
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
                            compras.append({'produto':'LEITE','quantidade':quantidade_leite,'valor':valor_final})
                            print('Compra realizada com sucesso!')

        def historico_compras():
            print('~'*100)
            print('~'*40,'HISTÓRICOS DE COMPRAS','~'*37)
            print('~'*100)
            if len(compras) == 0:
                print('Nenhuma encomenda realizada!')
            else:
                for compra in compras:
                    print('-'*30)
                    if 'produto' in compra:
                        print(f"Produto:{compra['produto']}")
                    if 'animal' in compra:
                        print(f"Animal:{compra['animal']}")
                    print(f"Quantidade:{compra['quantidade']}")
                    print(f"Valor: R${compra['valor']}")

                        
        def beneficios_cliente():
            print('~'*100)
            print('~'*40,'BENEFÍCIOS DO CLIENTE','~'*37)
            print('~'*100)
            if len(compras) >= 3:
                print('Você já possui direito aos 10% de desconto nas compras.')
                
            else: 
                faltam = 3 - len(compras)
                print(f'Faltam {faltam} compras para liberar os 10% de desconto.')

        def formas_pagamento():
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
        
        
        def voltando_inicio():
            print('Voltando ao menu inicial...')
                   