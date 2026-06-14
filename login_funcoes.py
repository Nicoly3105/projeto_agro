import maskpass
from email_validator import validate_email, EmailNotValidError
from colorama import Fore, init
init()

#login
login_cliente = [{'Login': 'cliente1', 'Senha': 'senha1'},{'Login': 'cliente2', 'Senha': 'senha2'}]
login_adm = [{'Login': 'adm1', 'Senha': 'senha1'},{'Login': 'adm2', 'Senha': 'senha2'}]
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
                if login == i['Login'] and senha == i['Senha']:
                    login_encontrado = True
                    login_encontrado_cliente = True
                    print('\033[1;34mLogin cliente encontrado com sucesso!\033[m')
                    break
            if login_encontrado == False:
                for i in login_adm:
                    if login == i['Login'] and senha == i['Senha']:
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
        print('\033[1;33m*a senha precisa ter no mínimo 8 caracteres*\n*a senha precisa ter letras e números*\033[m')   
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
                        confirmar_senha = maskpass.askpass(prompt='Confirme sua senha: ', mask='\033[1;37m*\033[m')
                        if confirmar_senha == senha:
                            login_cliente.append({'Login':login,'Senha': senha})
                            print('\033[1;34mCadastro realizado com sucesso!\033[m')
                            break
                        else:
                            print('\033[1;31mAs senhas não coincidem!\033[m')
                else:
                        print('\033[1;31mA senha não contém letras e números!\033[m')
                        continue
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
        print('\033[1;33m*a senha precisa ter no mínimo 8 caracteres*\n*a senha precisa ter letras e números*\033[m')   
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
                            login_adm.append({'Login':login, 'Senha':senha})
                            print('\033[1;34mCadastro realizado com sucesso!\033[m')
                            break
                        else:
                            print('\033[1;31mAs senhas não coincidem!\033[m')
                else:
                        print('\033[1;31mA senha não contém letras e números!\033[m')
                        continue
                break

def voltando_inicio():
    print('\033[1;34mVoltando ao menu inicial...\033[m')


while True:
        
        print(Fore.GREEN + """                                       ██           ██          ██         ▀██ 
▄ ▄▄ ▄▄▄     ▄▄▄  ▄ ▄▄▄   ▄▄▄ ▄▄      ▄▄▄  ▄ ▄▄▄   ▄▄▄    ▄▄▄  ▄▄▄   ▄▄▄    ██ 
 ██ ██ ██  ▄██ ██  ██ ██   ██ █        ██   ██ ██   ██  ▄██ ▀█  ██  ▀▀▄██   ██ 
 ██ ██ ██  ██▀▀▀▀  ██ ██   ██ █        ██   ██ ██   ██  ███     ██  ▄█ ██   ██ 
▄██ ██ ██▄  ▀█▄▄▀ ▄██ ██▄  ▀█▄▀▄      ▄██▄ ▄██ ██▄ ▄██▄  ▀█▄▄▀ ▄██▄ ▀█▄▀▀▄ ▄██▄ """)
        
        print('[\033[1;33m1\033[m] LOGIN')
        print('[\033[1;33m2\033[m] CADASTRAR CLIENTE NOVO')
        print('[\033[1;33m3\033[m] CADASTRAR NOVO ADM')
        print('[\033[1;33m4\033[m] SAIR')
        op = int(input('Digite a opção desejada: '))
        if op == 1:
            verificação_login()
        elif op == 2:
            cadastro_cliente()
        elif op == 3:
            cadastro_adm()
        elif op == 4:
            voltando_inicio()
        
