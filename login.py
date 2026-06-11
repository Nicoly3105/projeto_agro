#LOGIN
menu_login = []
login_cliente = []
login_adm = []
login_encontrado_cliente = False
login_encontrado_adm = False

while True:
    print('~'*100)
    print('~'*47,'MENU','~'*47)
    print('~'*100)
    print('[1]LOGIN \n[2]CADASTRAR CLIENTE NOVO\n[3]CADASTRAR NOVO ADM\n[4]SAIR')
    op_login = int(input('Digite a opção que deseja para prosseguir: '))

    if op_login == 1:
        while True:
            login = input('Digite o nome de usúario ou email: ').lower().strip()
            senha = input('Digite a senha: ').lower().strip()
            for i in login_cliente :
                if login == i[0] and senha == i[1]:
                    login_encontrado_cliente = True
                    print('Login encontrado com sucesso!')
                    break
                    
                else:
                    print('Login não encontrado, por favor, tente novamente!')
            for i in login_adm :
                if login == i[0] and senha == i[1]:
                    login_encontrado_adm = True
                    print('Login encontrado com sucesso!')
                    break

                    
                else:
                    print('Login não encontrado, por favor, tente novamente!')
            break
        continue
    elif op_login == 2:
        login = input('Digite um nome de usúario ou email que você deseja usar: ').strip().lower()
        print('*a senha precisa ter no mínimo 8 caracteres*\n*a senha precisa ter letras e números*')   
        while True:
            senha = input('Digite a senha que deseja usar: ').strip()
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
                        confirmar_senha = input('Confirme sua senha: ')

                        if confirmar_senha == senha:
                            login_cliente.append({'Login':login,'Senha': senha})
                            print('Cadastro realizado com sucesso!')
                            break
                        else:
                            print('As senhas não coincidem!')
            break
            
    elif op_login == 3:
        login = input('Digite um nome de usúario ou email que você deseja usar: ').strip().lower()
        print('*a senha precisa ter no mínimo 8 caracteres*\n*a senha precisa ter letras e números*')   
        while True:
            senha = input('Digite a senha que deseja usar: ').strip()
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
                        confirmar_senha = input('Confirme sua senha: ')

                        if confirmar_senha == senha:
                            login_adm.append([login, senha])
                            print('Cadastro realizado com sucesso!')
                            break
                        else:
                            print('As senhas não coincidem!')
            break
    elif op_login == 4:
        print('PROGRAMA ENCERRADO!')
        break

#MENU ADM
if login_encontrado_adm == True:
    while True:
        print('~'*100)
        print('~'*46,'MENU ADM','~'*46)
        print('~'*100)
        break


