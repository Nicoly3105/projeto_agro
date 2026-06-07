import qrcode_terminal

print('~'*100)
print('~'*40,'FORMAS DE PAGAMENTO','~'*39)
print('~'*100)
print('[\033[1;33m1\033[m] PIX')
print('[\033[1;33m2\033[m] BOLETO')

pagamento = input('Escolha a forma de pagamento: ')

if pagamento == '1':
    print('\nPagamento via PIX selecionado!\n')

    qrcode_terminal.draw('') 

    print("\nPagamento gerado com sucesso!\n")

elif pagamento == '2':
    print('\nPagamento via BOLETO selecionado!')
    print('Boleto gerado com sucesso!\n')

else:
    print('\nOpção inválida!\n')

    
     