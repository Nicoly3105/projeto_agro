import qrcode_terminal
def qr_pix():
    print('\033[1;32m~'*100)
    print('~'*40,'FORMAS DE PAGAMENTO','~'*39)
    print('~'*100)
    print('\033[m[\033[1;33m1\033[m] PIX')
    print('[\033[1;33m2\033[m] BOLETO')

    pagamento = input('Escolha a forma de pagamento: ')
    if pagamento == '1':
        print('\033[1;32m~'*35,'\nPagamento via PIX selecionado!\n','~'*34,'\033[m')
        qrcode_terminal.draw('') 
        print("\nPagamento gerado com sucesso!\n")
    elif pagamento == '2':
        print('\nPagamento via BOLETO selecionado!')
        print('Boleto gerado com sucesso!\n')
    else:
        print('\nOpção inválida!\n')
qr_pix()
    
     