# src/main.py #######################################################
#
# Apesar do nome, esse arquivo não será o principal do do projeto.
# Ele será responsável apenas por rodar o código como um todo.
#
# Cada processo será separado em pequenos blocos, sejam classes,
# sejam funções ou até módulos. Após isso, todos as partições do
# programa serão juntas em um só meio de execução que será chamado
# aqui...
#
#####################################################################

from modules.environment.enviroment_verifier import EnvChecker

if __name__ == "__main__":

  some_bool: bool = EnvChecker.checkCurrentPath()
#


quit()

# a fim de não perder o código já escrito, ele será mantido logo
# abaixo, mesmo que não seja executado...
from engines import *

nickname = get_nick()
nickname = nickname.title()



# Testando a função
textcolor('vermelho', 'Este texto deve ser vermelho')

