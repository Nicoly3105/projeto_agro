from pybrcode.pix import generate_simple_pix
print('~'*100)
print('~'*40,'FORMAS DE PAGAMENTO','~'*39)
print('~'*100)
print('[\033[1;33m1\033[m] PIX')
print('[\033[1;33m2\033[m] BOLETO')
pagamento = input('Escolha a forma de pagamento: ')

if pagamento == '1':
    print('Pagamento via PIX selecionado!')
    pix = generate_simple_pix(
        fullname="Fazenda Sertão",
        key="fazendasertao@gmail.com",
        city="Cajazeiras",
        value=87.5,
        pix_id="PEDIDO001",
        description="Compra via pix"
)
    pix.imageToPath(".", "pix_cliente")
    print("QR Code gerado com sucesso!")
elif pagamento == '2':
                print('Pagamento via BOLETO selecionado!')
                print('Boleto gerado com sucesso!')
else:
                print('Opção invalida!')    
        
        