
import maskpass
from email_validator import validate_email, EmailNotValidError

#login
login_cliente = [('cliente1','senha1'),('cliente2','senha2')]
login_adm = [('adm1','senha1'),('adm2','senha2')]
menu_login = []
login_encontrado_cliente = False
login_encontrado_adm = False

def verificação_login():
    while True:
            login = input('Digite o email: ').lower().strip()
            try:
                validate_email(login)
            except EmailNotValidError:
                print('\033[1;31mEmail inválido, tente novamente!\033[m')
                continue
            senha = maskpass.askpass(prompt='Digite a senha que você deseja usar: ', mask='*')
            login_encontrado = False
            login_encontrado_cliente = False
            login_encontrado_adm = False

            for i in login_cliente:
                if login == i[0] and senha == i[1]:
                    login_encontrado = True
                    login_encontrado_cliente = True
                    print('\033[1;34mLogin cliente encontrado com sucesso!\033[m')
                    break
            if login_encontrado == False:
                for i in login_adm:
                    if login == i[0] and senha == i[1]:
                        login_encontrado = True
                        login_encontrado_adm = True
                        print('\033[1;34mLogin ADM encontrado com sucesso!\033[m')
                        break
            if login_encontrado == False:
                print('\033[1;31mLogin não encontrado, tente novamente!\033[m')
            else:
                break  

#cadas cliente
def cadastro_cliente():
    while True:
        login = input('Digite o email: ').lower().strip()
        try:
            validate_email(login)
        except EmailNotValidError:
            print('\033[1;31mEmail inválido, tente novamente!\033[m')
            continue
        print('\033[1;31m*a senha precisa ter no mínimo 8 caracteres*\n*a senha precisa ter letras e números*\033[m')   
        senha = maskpass.askpass(prompt='Digite a senha que você deseja usar: ', mask='\033[1;37m*\033[m')
        if len(senha) < 8:
                print('\033[1;31mSenha muito curta, tente novamente!\033[m')
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
                        confirmar_senha = maskpass.askpass(prompt='Confirme sua senha: ', mask='\033[1;37*\033[m')
                        if confirmar_senha == senha:
                            login_cliente.append([login, senha])
                            print('\033[1;34mCadastro realizado com sucesso!\033[m')
                            break
                        else:
                            print('\033[1;31mAs senhas não coincidem!\033[m')
                else:
                        print('\033[1;31mA senha não contém letras e números!\033[m')
                        break
        break
# cadas adm
def cadastro_adm():
    while True:
        login = input('Digite o email: ').lower().strip()
        try:
            validate_email(login)
        except EmailNotValidError:
            print('\033[1;31mEmail inválido, tente novamente!\033[m')
            continue
        print('\033[1;31m*a senha precisa ter no mínimo 8 caracteres*\n*a senha precisa ter letras e números*\033[m')   
        senha = maskpass.askpass(prompt='Digite a senha que você deseja usar: ', mask='*')
        if len(senha) < 8:
                print('\033[1;31mSenha muito curta, tente novamente!\033[m')
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
                            print('\033[1;34mCadastro realizado com sucesso!\033[m')
                            break
                        else:
                            print('\033[1;31mAs senhas não coincidem!\033[m')
                else:
                        print('\033[1;31mA senha não contém letras e números!\033[m')
                        break
        break

def voltando_inicio():
    print('\033[1;34mVoltando ao menu inicial...\033[m')
