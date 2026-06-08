# funções adm
animais = {}
lista_animais = []



def cadastro_animais():
    print('\033[1;32m~'*40,'CADASTRO DE ANIMAIS','~\033[m'*39)
    animais['Animal'] = input('Digite o animal que você deseja cadastrar: ').capitalize()
    while True:
        animais['Peso'] = float(input('Digite o peso do animal: '))
        if animais['Peso'] <= 0 :
            print('Esse peso é inválido para o animal, tente novamente!')
            continue
        else:
            break
    animais['Gênero'] = input('Digite o gênero do animal: ')
    animais ['Status'] = input('Digite o status do animal: ')
    while True:
        animais['Valor'] = float(input('Digite o valor do animal: '))
        if animais['Valor'] <= 0 :
            print('Esse valor é inválido para o animal, tente novamente!')
            continue
        else:
            break 
    lista_animais.append(animais.copy())
    print(lista_animais)
cadastro_animais()