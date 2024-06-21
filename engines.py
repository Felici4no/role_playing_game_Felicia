print('...._....')
import time
import sys
#Basic ux ui
def typewriter(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Para pular para a próxima linha após terminar o texto

# Testando a função com um atraso menor para efeito mais realista


def textcolor(color, text):
    # Definindo os códigos de cores
    cores = {
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'azul': '\033[34m',
        'ciano': '\033[36m',
        'magenta': '\033[35m',
        'amarelo': '\033[33m',
        'preto': '\033[30m',
        'branco': '\033[37m',
        'restaura': '\033[0m',
        'negrito': '\033[1m',
        'reverso': '\033[2m',
        'fundo_preto': '\033[40m',
        'fundo_vermelho': '\033[41m',
        'fundo_verde': '\033[42m',
        'fundo_amarelo': '\033[43m',
        'fundo_azul': '\033[44m',
        'fundo_magenta': '\033[45m',
        'fundo_ciano': '\033[46m',
        'fundo_branco': '\033[47m'
    }

    # Pegando o código de cor
    cor_codigo = cores.get(color, '\033[0m')  # Padrão para restaura se a cor não for encontrada

    # Imprimindo o texto com a cor desejada
    print(f'{cor_codigo}{text}\033[0m')

def get_nick():
    while True:
        nick = input('Nick: ')
        if len(nick) >= 4:
            return nick
        else:
            print('Nick inválido. Deve ter pelo menos 4 caracteres.')
