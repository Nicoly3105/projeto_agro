import qrcode_terminal
from barcode import Code128
from barcode.writer import ImageWriter


def gerar_boleto():
    codigo = "3419179001010435100479102015000889860000015000"

    boleto = Code128(codigo, writer=ImageWriter())
    arquivo = boleto.save("boleto")
    print('\033[1;34m')
    print('=' * 80)
    print(' ' * 30 + 'BOLETO BANCÁRIO')
    print('=' * 80)
    print('Linha Digitável:')
    print(codigo)
    print('=' * 80)
    print(f'Código de barras salvo em: {arquivo}')
    print('\033[m')
    def formas_pagamento():
     print('\033[1;32m~' * 100)
    print('~' * 40, 'FORMAS DE PAGAMENTO', '~' * 39)
    print('~' * 100)
    print('\033[m[\033[1;33m1\033[m] PIX')
    print('[\033[1;33m2\033[m] BOLETO')

    pagamento = input('Escolha a forma de pagamento: ')

    if pagamento == '1':
        print('\033[1;32m~' * 35, 'Pagamento via PIX selecionado!', '~' * 34)
        qrcode_terminal.draw("PIX-EXEMPLO")
        print("\033[1;34m\nPagamento gerado com sucesso!\n\033[m")

        formas_pagamento()

    elif pagamento == '2':
        print('\033[1;32m~' * 33, 'Pagamento via BOLETO selecionado!', '~' * 33)
        gerar_boleto()

    else:
        print('\033[1;31mOpção inválida!\033[m')
gerar_boleto()
    
     