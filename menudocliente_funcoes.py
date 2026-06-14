import qrcode_terminal
import msvcrt
import random
from rich.console import Console
from rich.panel import Panel
console = Console()
from colorama import Fore, init
init()

compras = []
encomendas = []
produtos = [{'Produto':'Leite','Quantidade':15,'Unidade':'L','Valor':8}]
animais = [{'Animal':'Porco','Quantidade':25,'Unidade:':'kg','Valor': 89}]
leite = {'Volume': 100, 'Valor': 5}
historico = []

def ver_produtos():
            if len(produtos) == 0:
                print('\033[1;31mNenhum produto cadastrado!\033[m')

            else:
                print('\033[1;32m~'*100)
                print('~' *41,'LISTA DE PRODUTOS', '~' *40)
                print('~'*100, '\033[m')
                for item in produtos:
                    print(f'\033[1;35mProduto:\033[m {item["Produto"]}')
                    print(f'\033[1;35mQuantidade:\033[m {item["Quantidade"]} {item["Unidade"]}')
                    print(f'\033[1;35mValor:\033[m R${item["Valor"]}')
                    print('\033[1;35m~' * 30,'\033[m')
def comprar_produto():
            print('\033[1;32m~'*100)
            print('~' *41,'COMPRAR PRODUTOS', '~' *41)
            print('~'*100, '\033[m')
            produto_input = input('Digite o produto que deseja comprar: ').strip().capitalize()
            encontrado = False
            for item in produtos:

                if item['Produto'].capitalize() == produto_input:
                    encontrado = True
                    quantidade_compra = int(input('Digite a quantidade desejada: '))
                    if quantidade_compra > item['Quantidade']:
                        print('\033[1;31mQuantidade indisponível em estoque!\033[m')
                        print(f'\033[1;35mEstoque disponível:\033[m {item["Quantidade"]}{item["Unidade"]}')

                    else:
                        unidade = item['Unidade']
                        valor_compra = item['Valor']
                        valor_total = quantidade_compra * valor_compra
                        if len(compras) >= 3:
                            desconto = valor_total * 0.10
                            valor_final = valor_total - desconto
                            print(f'\033[1;35mDesconto aplicado:\033[m R$ {desconto:.2f}')

                        else:
                         valor_final = valor_total
                         print(f'\033[1;35mValor final:\033[m R$ {valor_final:.2f}')
                         item['Quantidade'] -= quantidade_compra
                         compras.append({'Produto':produto_input,'Quantidade':quantidade_compra,'Unidade':unidade,'Valor':valor_final})
                         historico.append({'Ação':'Venda Produto', 'Item': produto_input,'Quantidade': quantidade_compra})
                         print('\033[1;34mCompra realizada com sucesso!\033[m')
                    break
            if encontrado == False:
                print('\033[1;31mProduto não encontrado!\033[m')
def ler_data():
    print("Data (DD/MM/AAAA): ", end="", flush=True)
    numeros = ""
    while True:
        tecla = msvcrt.getwch()
        if tecla == "\r":
            break
        if tecla == "\b":
            if len(numeros) > 0:
                numeros = numeros[:-1]
                print("\b \b", end="", flush=True)
            continue
        if tecla.isdigit() and len(numeros) < 8:
            numeros += tecla
            print(tecla, end="", flush=True)
            if len(numeros) == 2 or len(numeros) == 4:
                print("/", end="", flush=True)
    print()
    if len(numeros) != 8:
        print("⚠ Data incompleta!")
        return numeros
    return f"{numeros[:2]}/{numeros[2:4]}/{numeros[4:]}"
def ler_horario():
    print("Horário (HH:MM): ", end="", flush=True)
    numeros = ""
    while True:
        tecla = msvcrt.getwch()
        if tecla == "\r":
            break
        if tecla == "\b":
            if len(numeros) > 0:
                numeros = numeros[:-1]
            print("\b \b", end="", flush=True)
            continue
        if tecla.isdigit() and len(numeros) < 4:
            numeros += tecla
            display = numeros
            if len(numeros) > 2:
                display = numeros[:2] + ":" + numeros[2:]
            print("\rHorário (HH:MM): " + display, end="", flush=True)
        print()
    if len(numeros) != 4:
        print("⚠ Horário incompleto!")
        return numeros
    return f"{numeros[:2]}:{numeros[2:]}"
def encomendar_produto():
            print('\033[1;32m~'*100)
            print('~' *40,'ENCOMENDAR PRODUTOS', '~' *39)
            print('~'*100,'\033[m')
            produto_input = input('Digite o produto que deseja encomendar: ').capitalize()
            encontrado = False 
            for item in produtos:
                if item['Produto'].capitalize() == produto_input:
                    encontrado = True 
                    break
                else:
                    print('\033[1;31mProduto não encontrado!\033[m')
                    break
            while True:
                quantidade = int(input('Digite a quantidade desejada: '))
                if quantidade <= 0:
                    print('\033[1;31mQuantidade inexistente! Tente novamente.\033[m')
                    continue
                else:
                    break
            console.print(
            Panel(
            "📅 Digite a data no formato DD/MM/AAAA",
            title="Agendamento"
                    )
            )
            data = ler_data()
            horario = ler_horario()
            encomendas.append({'Produto':produto_input,'Quantidade':quantidade,'Data':data,'Horário':horario})
            print('\033[1;34mEncomenda realizada com sucesso!\033[m')
def ver_animais():
            if len(animais) == 0:
                print('\033[1;31mNenhum animal cadastrado!\033[m')
            else:
                print('\033[1;32m~'*100)
                print('~' *40,'LISTA DE ANIMAIS', '~' *40)
                print('~'*100, '\033[m')
                for item in animais:
                    print(f"\033[1;35mBrinco:\033[m {item['Brinco']}")
                    print(f'\033[1;35mAnimal:\033[m {item["Animal"]}')
                    print(f'\033[1;35mQuantidade:\033[m {item["Quantidade"]}')
                    print(f'\033[1;35mPeso:\033[m {item["Peso"]}')
                    print(f'\033[1;35mGênero:\033[m {item["Gênero"]}')
                    print(f'\033[1;35mStatus:\033[m {item["Status"]}')
                    print(f'\033[1;35mValor:\033[m R${item["Valor"]}')
                    print('\033[1;35m~' * 100,'\033[m')

def comprar_animal():
            print('\033[1;32m~'*100)
            print('~' *40,'COMPRAR ANIMAIS', '~' *40)
            print('~'*100,'\033[m')
            animal_input = input('Digite o animal que deseja comprar: ').strip().capitalize()
            encontrado = False
            for item in animais:

                if item['Animal'].capitalize() == animal_input:
                    encontrado = True
                    quantidade_animal = int(input('Digite a quantidade desejada: '))
                    if quantidade_animal > item['Quantidade']:
                        print('\033[1;31mQuantidade indisponível em estoque!\033[m')
                        print(f'Estoque disponível: {item["Quantidade"]}')

                    else:
                        valor_animal = item['Valor']
                        valor_total = quantidade_animal * valor_animal
                        if len(compras) >= 3:
                            desconto = valor_total * 0.10
                            valor_final = valor_total - desconto
                            print(f'\033[1;35mDesconto aplicado:\033[m R$ {desconto:.2f}')

                        else:
                            valor_final = valor_total
                            print(f'\033[1;35mValor final:\033[m R$ {valor_final:.2f}')
                            item['Quantidade'] -= quantidade_animal
                            compras.append({'Animal':animal_input,'Quantidade':quantidade_animal,'Valor':valor_final})
                            historico.append({'Ação':'Venda Animal', 'Item': animal_input, 'Quantidade': 1})
                            print('\033[1;34mCompra realizada com sucesso!\033[m')
                    break
            if encontrado == False:
                print('\033[1;31mAnimal não encontrado!\033[m')

def ver_encomendas_animais():
            print('\033[1;32m~'*100)
            print('~' *40,'ENCOMENDAR ANIMAIS', '~' *39)
            print('~'*100,'\033[m')
            animal_input = input('Digite o animal que deseja encomendar: ').capitalize()
            encontrado = False 
            for item in animais:
                if item['Animal'].capitalize() == animal_input:
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
            console.print(
            Panel(
            "📅 Digite a data desejada (DD/MM/AAAA)",
            title="Agendamento"
                    )
            )
            data = ler_data()
            horario = ler_horario()
            encomendas.append({'Animal':animal_input,'Quantidade':quantidade,'Data':data,'Horário':horario})
            print('\033[1;34mEncomenda realizada com sucesso!\033[m')

def ver_encomendas():

            if len(encomendas) == 0:
                print('\033[1;31mNenhuma encomenda realizada!\033[m')

            else:
                print('\033[1;32m~'*100)
                print('~' *40,'LISTA DE ENCOMENDAS', '~' *39)
                print('~'*100, '\033[m')

                for encomenda in encomendas:
                    if 'Produto' in encomenda:
                        print(f"\033[1;35mProduto:\033[m {encomenda['Produto']}")
                        print(f"\033[1;35mQuantidade:\033[m {encomenda['Quantidade']}")
                        print(f"\033[1;35mData:\033[m {encomenda['Data']}")
                        print(f"\033[1;35mHorário:\033[m {encomenda['Horário']}")
                        print('\033[1;35m~'*100,'\033[m')
                    if 'Animal' in encomenda:
                        print(f"\033[1;35mAnimal:\033[m {encomenda['Animal']}")
                        print(f"\033[1;35mQuantidade:\033[m {encomenda['Quantidade']}")
                        print(f"\033[1;35mData:\033[m {encomenda['Data']}")
                        print(f"\033[1;35mHorário:\033[m {encomenda['Horário']}")
                        print('\033[1;35m~'*100,'\033[m')

def comprar_leite():
            print('\033[1;32m~'*100)
            print('~' *42,'COMPRAR LEITE', '~' *42)
            print('~'*100,'\033[m')
            quantidade_leite = int(input('Digite a quantidade desejada: '))
            if quantidade_leite > leite['Volume']:
                        print('\033[1;31mQuantidade indisponível em estoque!\033[m')
                        print(f"\033[1;35mEstoque disponível:\033[m {leite['Volume']}")

            else:
                        valor_leite = leite['Valor']
                        valor_total = quantidade_leite * valor_leite
                        if len(compras) >= 3:
                            desconto = valor_total * 0.10
                            valor_final = valor_total - desconto
                            print(f'\033[1;35mDesconto aplicado:\033[m R$ {desconto:.2f}')

                        else:
                            valor_final = valor_total
                            print(f'\033[1;35mValor final:\033[m R$ {valor_final:.2f}')
                            leite['Volume'] -= quantidade_leite
                            compras.append({'Produto':'LEITE','Quantidade':quantidade_leite,'Valor':valor_final})
                            historico.append({'Ação':'Venda Leite', 'Item':'Leite', 'Quantidade': quantidade_leite})
                            print('\033[1;34mCompra realizada com sucesso!\033[m')

def recibo_compras():
        print('\033[1;32m~'*100)
        print('~'*40,'RECIBO DE COMPRAS','~'*37)
        print('~'*100 ,'\033[m')
        if len(compras) == 0:
                print('\033[1;31mNenhuma encomenda realizada!\033[m')
        else:
                for compra in compras:
                    print('\033[1;35m~'*100,'\033[m')
                    if 'Produto' in compra:
                        print(f"\033[1;35mProduto:\033[m{compra['Produto']}")
                        print(f"\033[1;35mQuantidade:\033[m {compra['Quantidade']}")
                        print(f"\033[1;35mUnidade:\033[m {compra['Unidade']}")
                        print(f"\033[1;35mValor:\033[m {compra['Valor']}")
                        print('\033[1;35m~'*100,'\033[m')
                    if 'Animal' in compra:
                        print(f"\033[1;35mAnimal:\033[m{compra['Animal']}")
                        print(f"\033[1;35mQuantidade:\033[m{compra['Quantidade']}")
                        print(f"\033[1;35mValor:\033[m R${compra['Valor']}")
  
def beneficios_cliente():
            print('\033[1;32m~'*100)
            print('~'*40,'BENEFÍCIOS DO CLIENTE','~'*37)
            print('~'*100,'\033[m')
            if len(compras) >= 3:
                print('\033[1;34mVocê já possui direito aos 10% de desconto nas compras.\033[m')
                
            else: 
                faltam = 3 - len(compras)
                print(f'\033[1;35mFaltam \033[m{faltam} \033[1;35mcompras para liberar os\033[m \033[1;33m10%\033[m \033[1;35mde desconto.\033[m')
def gerar_boleto(valor):
    linha_digitavel = ''.join([str(random.randint(0, 9)) for _ in range(47)])
    codigo_barras = ''.join([str(random.randint(0, 9)) for _ in range(44)])
    print('\033[1;32m~' * 100)
    print(' ' * 35, 'BOLETO GERADO NO SISTEMA', ' ' * 35)
    print('~' * 100, '\033[m')
    print(f'\033[1;35mValor:\033[m R$ {valor:.2f}')
    print(f'\033[1;35mLinha digitável:\033[m {linha_digitavel}')
    print(f'\033[1;35mCódigo de barras:\033[m {codigo_barras}')
    print('\033[1;32m~' * 100, '\033[m')
    print('\033[1;34mBoleto gerado com sucesso!\033[m')

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
                valor = float(input('Digite o valor da compra: R$ '))
                gerar_boleto(valor)
                print('\033[1;34mBoleto gerado com sucesso!\033[m')

            else:
                print('\033[1;31mOpção inválida!\033[m') 

def voltando_inicio():
    print('\033[1;34mVoltando ao menu inicial...\033[m')

while True:
        
        print(Fore.GREEN + """                                          ▀██                    ▀██   ██                   ▄         
▄ ▄▄ ▄▄▄     ▄▄▄  ▄ ▄▄▄   ▄▄▄ ▄▄        ▄▄ ██   ▄▄▄         ▄▄▄   ██  ▄▄▄    ▄▄▄  ▄ ▄▄▄    ██     ▄▄▄ 
 ██ ██ ██  ▄██ ██  ██ ██   ██ █       ▄██ ▀██  ██ ██      ▄██ ▀█  ██   ██  ▄██ ██  ██ ██  ▀██▀  ▄██ ██
 ██ ██ ██  ██▀▀▀▀  ██ ██   ██ █       ██▌  ██  ██ ██      ███     ██   ██  ██▀▀▀▀  ██ ██   ██   ██▀▀▀▀
▄██ ██ ██▄  ▀█▄▄▀ ▄██ ██▄  ▀█▄▀▄       ▀█▄▀██▄ ▀█▄█▀       ▀█▄▄▀ ▄██▄ ▄██▄  ▀█▄▄▀ ▄██ ██▄  ▀█▄▀  ▀█▄▄▀  """)
        
        print('\033[m[\033[1;33m1\033[m] VER PRODUTOS\n[\033[1;33m2\033[m] COMPRAR PRODUTOS\n[\033[1;33m3\033[m] ENCOMENDAR PRODUTOS\n[\033[1;33m4\033[m] VER ANIMAIS\n[\033[1;33m5\033[m] COMPRAR ANIMAL\n[\033[1;33m6\033[m] ENCOMENDAR ANIMAL\n[\033[1;33m7\033[m] VER ENCOMENDAS\n[\033[1;33m8\033[m] COMPRAR LEITE\n[\033[1;33m9\033[m] RECIBO DE COMPRAS\n[\033[1;33m10\033[m] BENEFÍCIOS DO CLIENTE\n[\033[1;33m11\033[m] FORMAS DE PAGAMENTO\n[\033[1;33m12\033[m] VOLTAR')
        op_cliente = int(input('Digite a opção desejada: '))
        if op_cliente == 1:
            ver_produtos()
        elif op_cliente == 2:
            comprar_produto()
        elif op_cliente == 3:
            encomendar_produto()
        elif op_cliente == 4:
            ver_animais()
        elif op_cliente == 5:
            comprar_animal()
        elif op_cliente == 6:
            ver_encomendas_animais()
        elif op_cliente == 7:
            ver_encomendas()
        elif op_cliente == 8:
            comprar_leite()
        elif op_cliente == 9:
            recibo_compras()
        elif op_cliente == 10:
            beneficios_cliente()
        elif op_cliente == 11:
            formas_pagamento()
        elif op_cliente == 12:
            voltando_inicio()

