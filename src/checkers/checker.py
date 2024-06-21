
# classe Visuals
class Visuals:
  """
  Visuals
  -------

  Classe responsável por armazenar as operações de caráter visual dos
  processos de checagem como:
  
  - animações
  - efeitos de escape
  - writers e flushers
  - interação com o usuário no geral

  ---

  Não é instanciável, apenas executável...
  """

  # constantes privadas da classe(animação):
  _BASE_ANIMATION_SLEEP_RATE  : float = 0.15
  _BASE_ANIMATION_TIMES_AMOUNT: int   = 16
  _BASE_ANIMATION_MODE        : str   = "replace"

  # constantes privadas da classe(format escapes):
  _RESET_ESCAPE         : str  = "\033[0m"
  _STRONG_ESCAPE_NEUTRAL: str  = "\033[1;34m"

  # função para abilitar o uso de escapes no Windows (cmd)
  def enableEscapes() -> None:
    """
    enableEscapes() -> None
    -----------------------

    Função para abilitar o uso de escapes no Windows.cmd!

    Muitas plataformas oferecem suporte para os escapes utilizados no
    projeto, até mesmo o Windows Powershell, mas nas versões mais
    velhas do Windows.cmd, não há esse tipo de suporte.

    Por isso o bloco a seguir serve para abilitar as operações de
    escape com a biblioteca os do Python.
    """

    # importando a biblioteca os
    import os

    # se o sistema operacional for Windows (nome = 'nt')
    if os.name == "nt":

      # chamas comando
      os.system("")
    #
  #

  def terminalClear() -> None:

    print("\033[2J\033[H", end = "")

    print("=" * 70)
  #

  def initializeCheckingMessage() -> None:
    
    Visuals.terminalClear()

    print(
      "A checagem do ambiente está prestes a " +
      Visuals._STRONG_ESCAPE_NEUTRAL           +
      "ser realizada "                         +
      Visuals._RESET_ESCAPE                    ,
      end = ""
    )

    Visuals.loadAnimation(["-", "\\", "|", "/"])
  #

  # função para realizar animações no terminal do usuário
  def loadAnimation(
    char_list     : list[str] | None = None                        ,
    sleep_rate    : float            = _BASE_ANIMATION_SLEEP_RATE  ,
    times_amount  : int              = _BASE_ANIMATION_TIMES_AMOUNT,
    animation_mode: str              = _BASE_ANIMATION_MODE
  ) -> None:

    import time, sys

    if any((
      char_list is None    ,
      len(char_list) < 2   ,
      sleep_rate     < 0.05,
      sleep_rate     > 10  ,
      times_amount   < 1   ,
      times_amount   > 30
    )):
      return None
    #

    for i in range(times_amount):

      print(char_list[i % len(char_list)], end = "", flush = True)

      time.sleep(sleep_rate)

      if animation_mode != "concat" and i < times_amount:
        sys.stdout.write("\b")
        sys.stdout.flush()
      #
    #
  #
#

# classe Checker
class Checker:
  """
  Checker
  -------

  Classe responsável por realizar a checagem das dependências do
  projeto em sua máquina.

  Não é instanciável, apenas executável...
  """

  _PYTHON_MINIMUM_VERSION: str = "3.12.2"
  
  # comparar tag de versões  
  def versionTagMatching(
    current_version: str,
    target_version : str
  ) -> bool | None:
    """
    versionTagMatching(str, str) -> bool
    ------------------------------------
    
    Essa função recebe dois argumentos em forma de `String`, sendo
    eles:

    >>> current_version: str # versão atual
    >>> target_version : str # versão mínima necessária

    ---

    Os argumentos são pegos em tipo `String` já geralmente eles são
    moldados em forma de `'A.B.C'` e não existe tipagem para esse
    tipo de dado em Python a não ser String...

    ---

    Quanto a execução do bloco, ele irá definir uma lista de inteiros
    a partir dos dois argumentos fornecidos, onde cada valor será
    comparado.

    ---

    Se o bloco obtiver inputs estranhos (que não satisfaça a
    operação), será retornado None para indicar o erro.

    ---

    Se a `current_version` for igual ou superior à target_version, o
    bloco retorna `True`, caso contrário `False`.
    """

    # criando lista de inteiros da versão atual
    current_values: list[int] = [
      int(x) for x in current_version.split(".")
    ]

    # criando a lista de inteiros da versão alvo
    target_values: list[int] = [
      int(x) for x in target_version.split(".")
    ]

    # fazendo teste 'OR operator'
    if any((
      len(current_values) != 3, # se o tamanho não for 3
      len(target_values ) != 3  # se o tamanho não for 3
    )):

      # retorne None para indicar o erro
      return None
    #

    # loop for para iterar nas duas listas
    for i in range(3):
      
      # se o valor atual for superior ao valor alvo
      if current_values[i] > target_values[i]:

        return True
      #

      # se o valor atual for inferior ao valor alvo
      elif current_values[i] < target_values[i]:

        return False
      #
    # caso sejam iguais, o loop continua

    # se a execução chegou até aqui, é porque todas os inteiros são
    # iguais, logo, satisfaz as condições da função, ou seja:
    return True
  #

  def moduleExists(module_name: str) -> bool:
    ...
  
  def moduleUpToDate(module_name: str) -> bool:
    ...

  # função que testa se o python está atualizado
  def pythonUpToDate(minimum_version: str) -> bool | None:
    """
    pythonUpToDate(str) -> bool
    ---------------------------

    Função que testa se a versão do Python em sua máquina satisfaz a
    versão mínima necessária para rodar o programa.

    ---

    - Recebe como argumento a versão mínima necessário `(String)`
    - Declara a versão atual do seu Python
    - Passa os dados para serem tratados pela função
    `versionTagMatching(str, str)`
    - A função citada acima retorna verdadeiro se satisfazer
    requisitos, falso se não satisfazer ou None caso the ocorrido um
    erro
    """

    # importando biblioteca necessário para realizar a operação
    import sys

    # otendo a versão do seu python
    your_version: str = sys.version.split(" ")[0]

    # atribuindo o retorno do matching numa variável
    up_to_date: bool | None = Checker.versionTagMatching(
      your_version   ,
      minimum_version
    )

    # retornando essa mesma variável
    return up_to_date
  #

#

class Action:

  import asyncio

  # funçao 'main' da classe Checker
  async def startChecking() -> None:
    """
    """

    Visuals.enableEscapes()

    Visuals.initializeCheckingMessage()
  #

  async def getPythonSafe() -> bool | None:

    Visuals.terminalClear()
  #

  def mainRun() -> bool:

    Action.startChecking()
    Action.getPythonSafe()
  #
#