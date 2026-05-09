animais = [['vaca',37,'femea','gravida',8]]
produtos = [['coalho',7,'kg',6.5]]
while True:
    print('~'*100)
    print('~'*45,'MENU ADM','~'*45)
    print('~'*100)
    print('[1]CADASTRAR ANIMAL\n[2]VER ANIMAIS\n[3]CADASTRAR PRODUTO\n[4]VER PRODUTOS\n[5]CONVERSOR DE FABRICAÇÃO\n[6]VOLTAR')
    op_adm = int(input('Digite a opção que deseja para prosseguir: '))

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
        print('~'*100)
        print('~'*44,'CATEGORIAS','~'*44)
        print('~'*100)
        print('[1]QUEIJOS\n[2]LEITES\n[3]DERIVADOS\n[4]PRODUTOS PARA VENDA EM LOTE\n[5]PRODUTOS ARTESANAIS\n[6]VOLTAR')
        op_categoria = int(input('Digite a opção que deseja para prosseguir: '))
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
                produto = input('Digite o tipo de leite que você deseja cadastrar: ')
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
    elif op_adm == 4:
        for i in produtos:
            print(i)
    elif op_adm == 5:
         print('~'*38,'CONVERSOR DE FABRICAÇÃO','~'*39)
         print('[1]QUEIJO\n[2]DERIVADOS\n[3]ARTESANAIS')
         escolha = input('Qual produto você deseja fabricar? ')
