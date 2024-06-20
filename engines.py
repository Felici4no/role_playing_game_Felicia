print('...._....')

def get_nick():
    while True:
        nick = input('Nick: ')
        if len(nick) >= 4:
            return nick
        else:
            print('Nick inválido. Deve ter pelo menos 4 caracteres.')
