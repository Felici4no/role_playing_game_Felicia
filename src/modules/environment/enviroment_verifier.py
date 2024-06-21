# src/modules/environment/environment_verifier.py ###################
#
# Como já sugere o nome, aqui teremos os verificadores que determinam
# se a sua máquina de execução está apta para executar o program ou
# se há algum problema para tal.
#
# Apesar de parecer inútil, esse meio se faz muito importante quando
# pretende-se evitar erros/bugs durante a execução do programa
#
#####################################################################

class EnvChecker:

  def checkCurrentPath() -> bool:

    import os

    current_path: str = os.getcwd()

    print(current_path)

    return True
  #