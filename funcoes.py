
import maskpass
from email_validator import validate_email, EmailNotValidError

#login
login_cliente = [('cliente1','senha1'),('cliente2','senha2')]
login_adm = [('adm1','senha1'),('adm2','senha2')]
menu_login = []
login_encontrado_cliente = False
login_encontrado_adm = False

def verificação_login(login,senha):
    while True:
            login = input('Digite o email: ').lower().strip()
            try:
                validate_email(login)
            except EmailNotValidError:
                print('Email inválido, tente novamente!')
                continue
            senha = maskpass.askpass(prompt='Digite a senha que você deseja usar: ', mask='*')
            login_encontrado = False
            login_encontrado_cliente = False
            login_encontrado_adm = False

            for i in login_cliente:
                if login == i[0] and senha == i[1]:
                    login_encontrado = True
                    login_encontrado_cliente = True
                    print('Login cliente encontrado com sucesso!')
                    break
            if login_encontrado == False:
                for i in login_adm:
                    if login == i[0] and senha == i[1]:
                        login_encontrado = True
                        login_encontrado_adm = True
                        print('Login ADM encontrado com sucesso!')
                        break
            if login_encontrado == False:
                print('Login não encontrado, tente novamente!')
            else:
                break  

#cadas cliente
def cadastro_cliente(login_cliente):
    while True:
        login = input('Digite o email: ').lower().strip()
        try:
            validate_email(login)
        except EmailNotValidError:
            print('Email inválido, tente novamente!')
            continue
        print('*a senha precisa ter no mínimo 8 caracteres*\n*a senha precisa ter letras e números*')   
        while True:
            senha = maskpass.askpass(prompt='Digite a senha que você deseja usar: ', mask='*')
            if len(senha) < 8:
                print('Senha muito curta, tente novamente!')
                continue
            else:
                tem_letra = False
                tem_numero = False
                for i in senha:
                    if i.isalpha():
                        tem_letra = True
                    if i.isdigit():
                        tem_numero = True
                    if tem_letra and tem_numero:
                        confirmar_senha = maskpass.askpass(prompt='Confirme sua senha: ', mask='*')
                        if confirmar_senha == senha:
                            login_cliente.append([login, senha])
                            print('Cadastro realizado com sucesso!')
                            break
                        else:
                            print('As senhas não coincidem!')
                else:
                    print('A senha não contém letras e números!')
                    break
            break
cadastro_cliente(login_cliente)
# cadas adm
def cadastro_adm():
    while True:
        login = input('Digite o email: ').lower().strip()
        try:
            validate_email(login)
        except EmailNotValidError:
            print('Email inválido, tente novamente!')
            continue
        print('*a senha precisa ter no mínimo 8 caracteres*\n*a senha precisa ter letras e números*')   
        while True:
            senha = maskpass.askpass(prompt='Digite a senha que você deseja usar: ', mask='*')
            if len(senha) < 8:
                print('Senha muito curta, tente novamente!')
                continue
            else:
                tem_letra = False
                tem_numero = False

                for i in senha:
                    if i.isalpha():
                        tem_letra = True
                    if i.isdigit():
                        tem_numero = True

                    if tem_letra and tem_numero:
                        confirmar_senha = maskpass.askpass(prompt='Confirme sua senha: ', mask='*')

                        if confirmar_senha == senha:
                            login_adm.append([login, senha])
                            print('Cadastro realizado com sucesso!')
                            break
                        else:
                            print('As senhas não coincidem!')
            break
