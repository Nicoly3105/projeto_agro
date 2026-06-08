import qrcode_terminal
compras = []
encomendas = []
produtos = []
animais = []
leite = []

print('\033[1;32m~' * 100)
print('~' *43,'MENU CLIENTE', '~' *43)
print('~' * 100)
print('\033[m[\033[1;33m1\033[m] VER PRODUTOS\n[\033[1;33m2\033[m] COMPRAR PRODUTOS\n[\033[1;33m3\033[m] ENCOMENDAR PRODUTOS\n[\033[1;33m4\033[m] VER ANIMAIS\n[\033[1;33m5\033[m] COMPRAR ANIMAL\n[\033[1;33m6\033[m] ENCOMENDAR ANIMAL\n[\033[1;33m7\033[m] VER ENCOMENDAS\n[\033[1;33m8\033[m] COMPRAR LEITE\n[\033[1;33m9\033[m] HISTÓRICOS DE COMPRAS\n[\033[1;33m10\033[m] BENEFÍCIOS DO CLIENTE\n[\033[1;33m11\033[m] FORMAS DE PAGAMENTO\n[\033[1;33m12\033[m] VOLTAR')

op_cliente = int(input('Digite a opção desejada: '))

def ver_produtos():
            if len(produtos) == 0:
                print('Nenhum produto cadastrado!')

            else:
                print('\033[1;32m~'*100)
                print('~' *41,'LISTA DE PRODUTOS', '~' *40)
                print('~'*100, '\033[m')
                for produto, quantidade, unidade, valor in produtos:
                    print(f'\033[1;35mProduto:\033[m {produto}')
                    print(f'\033[1;35mQuantidade:\033[m {quantidade} {unidade}')
                    print(f'\033[1;35mValor:\033[m R${valor}')
                    print('\033[1;35m~' * 30,'\033[m')
ver_produtos()
def comprar_produto():
            print('\033[1;32m~'*100)
            print('~' *41,'COMPRAR PRODUTOS', '~' *41)
            print('~'*100, '\033[m')
            produto_input = input('Digite o produto que deseja comprar: ').strip().capitalize()
            encontrado = False
            for item in produtos:

                if item[0].capitalize() == produto_input:
                    encontrado = True
                    quantidade_compra = int(input('Digite a quantidade desejada: '))
                    if quantidade_compra > item[1]:
                        print('\033[1;31mQuantidade indisponível em estoque!\033[m')
                        print(f'\033[1;35mEstoque disponível:\033[m {item[1]}{item[2]}')

                    else:
                        unidade = item[2]
                        valor_compra = item[3]
                        valor_total = quantidade_compra * valor_compra
                        if len(compras) >= 3:
                            desconto = valor_total * 0.10
                            valor_final = valor_total - desconto
                            print(f'\033[1;35mDesconto aplicado:\033[m {desconto}')

                        else:
                         valor_final = valor_total
                         print(f'\033[1;35mValor final:\033[m {valor_final}')
                         item[1] -= quantidade_compra
                         compras.append({'Produto':produto_input,'Quantidade':quantidade_compra,'Unidade':unidade,'Valor':valor_final})
                         print('\033[1;34mCompra realizada com sucesso!\033[m')
                    break
            if encontrado == False:
                print('\033[1;31mProduto não encontrado!\033[m')

comprar_produto()
def encomendar_produto():
            print('\033[1;32m~'*100)
            print('~' *40,'ENCOMENDAR PRODUTOS', '~' *39)
            print('~'*100,'\033[m')
            produto_input = input('Digite o produto que deseja encomendar: ').capitalize()
            encontrado = False 
            for item in produtos:
                if item[0].capitalize() == produto_input:
                    encontrado = True 
                    break
                else:
                    print('\033[1;31mProduto não encontrado!\033[m')
            while True:
                quantidade = int(input('Digite a quantidade desejada: '))
                if quantidade <= 0:
                    print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                    continue
                else:
                    break
            data = input('Digite a data desejada:\n(DD/MM/AA)\n ')
            horario = input('Digite o horário desejado: ')

            encomendas.append({'Produto':produto_input,'Quantidade':quantidade,'Data':data,'Horário':horario})

            print('\033[1;34mEncomenda realizada com sucesso!\033[m')
encomendar_produto()
def ver_animais():
            if len(animais) == 0:
                print('\033[1;31mNenhum animal cadastrado!\033[m')
            else:
                print('\033[1;32m~'*100)
                print('~' *40,'LISTA DE ANIMAIS', '~' *40)
                print('~'*100, '\033[m')
                for animal, peso, genero, status, valor in animais:
                    print(f'\033[1;35mAnimal:\033[m {animal}')
                    print(f'\033[1;35mPeso:\033[m {peso}')
                    print(f'\033[1;35mGênero:\033[m {genero}')
                    print(f'\033[1;35mStatus:\033[m {status}')
                    print(f'\033[1;35mValor:\033[m R${valor}')
                    print('\033[1;35m~' * 100,'\033[m')
ver_animais()
def comprar_animal():
            print('\033[1;32m~'*100)
            print('~' *40,'COMPRAR ANIMAIS', '~' *40)
            print('~'*100,'\033[m')
            animal_input = input('Digite o animal que deseja comprar: ').strip().capitalize()
            encontrado = False
            for item in animais:

                if item[0].capitalize() == animal_input:
                    encontrado = True
                    quantidade_animal = int(input('Digite a quantidade desejada: '))
                    if quantidade_animal > item[1]:
                        print('\033[1;31mQuantidade indisponível em estoque!\033[m')
                        print(f'Estoque disponível: {item[1]}')

                    else:
                        valor_animal = item[4]
                        valor_total = quantidade_animal * valor_animal
                        if len(compras) >= 3:
                            desconto = valor_total * 0.10
                            valor_final = valor_total - desconto
                            print(f'\033[1;35mDesconto aplicado:\033[m {desconto}')

                        else:
                            valor_final = valor_total
                            print(f'\033[1;35mValor final:\033[m {valor_final}')
                            item[1] -= quantidade_animal
                            compras.append({'Animal':animal_input,'Quantidade':quantidade_animal,'Valor':valor_final})
                            print('\033[1;34mCompra realizada com sucesso!\033[m')
                    break
            if encontrado == False:
                print('\033[1;31mAnimal não encontrado!\033[m')
comprar_animal()
def ver_encomendas_animais():
            print('\033[1;32m~'*100)
            print('~' *40,'ENCOMENDAR ANIMAIS', '~' *39)
            print('~'*100,'\033[m')
            animal_input = input('Digite o animal que deseja encomendar: ').capitalize()
            encontrado = False 
            for item in animais:
                if item[0].capitalize() == animal_input:
                    encontrado = True 
                    break
                else:
                    print('\033[1;31mAnimal não encontrado!\033[m')
                    break
            while True:
                quantidade = int(input('Digite a quantidade desejada: '))
                if quantidade <= 0:
                    print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                    continue
                else:
                    break
            data = input('Digite a data desejada:\n(DD/MM/AA)\n ')
            horario = input('Digite o horário desejado: ')

            encomendas.append({'Animal':animal_input,'Quantidade':quantidade,'Data':data,'Horário':horario})

            print('\033[1;34mEncomenda realizada com sucesso!\033[m')
ver_encomendas_animais()
def ver_encomendas():

            if len(encomendas) == 0:
                print('\033[1;31mNenhuma encomenda realizada!\033[m')

            else:
                print('\033[1;32m~'*100)
                print('~' *40,'LISTA DE ENCOMENDAS', '~' *39)
                print('~'*100, '\033[m')

                for encomenda in encomendas:
                    if 'produto' in encomenda:
                        print(f"\033[1;35mProduto:\033[m {encomenda['produto']}")
                        print(f"\033[1;35mQuantidade:\033[m {encomenda['quantidade']}")
                        print(f"\033[1;35mData:\033[m {encomenda['data']}")
                        print(f"\033[1;35mHorário:\033[m {encomenda['horário']}")
                        print('\033[1;35m~'*100,'\033[m')
                    if 'animal' in encomenda:
                     print(f"\033[1;35mAnimal:\033[m {encomenda['animal']}")
                    print(f"\033[1;35mQuantidade:\033[m {encomenda['quantidade']}")
                    print(f"\033[1;35mData:\033[m {encomenda['data']}")
                    print(f"\033[1;35mHorário:\033[m {encomenda['horário']}")
                    print('\033[1;35m~'*100,'\033[m')
ver_encomendas()
def comprar_leite():
            print('\033[1;32m~'*100)
            print('~' *42,'COMPRAR LEITE', '~' *42)
            print('~'*100,'\033[m')
            quantidade_leite = int(input('Digite a quantidade desejada: '))
            if quantidade_leite > leite[0]:
                        print('\033[1;31mQuantidade indisponível em estoque!\033[m')
                        print(f'\033[1;35mEstoque disponível:\033[m {leite[0]}')

            else:
                        valor_leite = leite[1]
                        valor_total = quantidade_leite * valor_leite
                        if len(compras) >= 3:
                            desconto = valor_total * 0.10
                            valor_final = valor_total - desconto
                            print(f'\033[1;35mDesconto aplicado:\033[m {desconto}')

                        else:
                            valor_final = valor_total
                            print(f'\033[1;35mValor final:\033[m {valor_final}')
                            leite[0] -= quantidade_leite
                            compras.append({'produto':'LEITE','quantidade':quantidade_leite,'valor':valor_final})
                            print('\033[1;34mCompra realizada com sucesso!\033[m')
comprar_leite()
def historico_compras():
            print('\033[1;32m~'*100)
            print('~'*40,'HISTÓRICOS DE COMPRAS','~'*37)
            print('~'*100 ,'\033[m')
            if len(compras) == 0:
                print('\033[1;31mNenhuma encomenda realizada!\033[m')
            else:
                for compra in compras:
                    print('\033[1;35m~'*100,'\033[m')
                    if 'produto' in compra:
                        print(f"\033[1;35mProduto:\033[m{compra['produto']}")
                        print(f"\033[1;35mQuantidade:\033[m {compra['quantidade']}")
                        print(f"\033[1;35mData:\033[m {compra['data']}")
                        print(f"\033[1;35mHorário:\033[m {compra['horário']}")
                        print('\033[1;35m~'*100,'\033[m')
                    if 'animal' in compra:
                        print(f"\033[1;35mAnimal:\033[m{compra['animal']}")
                        print(f"\033[1;35mQuantidade:\033[m{compra['quantidade']}")
                        print(f"\033[1;35mValor:\033[m R${compra['valor']}")
historico_compras()   
def beneficios_cliente():
            print('\033[1;32m~'*100)
            print('~'*40,'BENEFÍCIOS DO CLIENTE','~'*37)
            print('~'*100,'\033[m')
            if len(compras) >= 3:
                print('\033[1;34mVocê já possui direito aos 10% de desconto nas compras.\033[m')
                
            else: 
                faltam = 3 - len(compras)
                print(f'\033[1;34mFaltam {faltam} compras para liberar os 10% de desconto.\033[m')
beneficios_cliente()
def formas_pagamento():
            print('\033[1;32m~'*100)
            print('~'*40,'FORMAS DE PAGAMENTO','~'*39)
            print('~'*100)
            print('\033[m[\033[1;33m1\033[m] PIX')
            print('[\033[1;33m2\033[m] BOLETO')
            pagamento = input('Escolha a forma de pagamento: ')

            if pagamento == '1':
                print('\033[1;32m~'*35,'Pagamento via PIX selecionado!','~'*34,'\033[1;32m')
                if pagamento == '1':
                    qrcode_terminal.draw('') 
                    print("\033[1;34m\nPagamento gerado com sucesso!\n\033[m")
                else:
                    print('\033[1;31m\nOpção inválida!\n\033[m')

            elif pagamento == '2':
                print('\033[1;32m~'*33,'Pagamento via BOLETO selecionado!','~'*33,'\033[m')
                print('\033[1;34mBoleto gerado com sucesso!\033[m')

            else:
                print('\033[1;31mOpção inválida!\033[m') 
formas_pagamento()
def voltando_inicio():
    print('\033[1;34mVoltando ao menu inicial...\033[m')
voltando_inicio()
                   