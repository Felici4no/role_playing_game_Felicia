class Item:
    def __init__(self, nome, atributo, tamanho):
        self.nome = nome
        self.atributo = atributo
        self.tamanho = tamanho


class Mochila:
    def __init__(self, nome):
        self.nome = nome
        self.slots = {}

    def entradaItem(self, obj):
        self.slots[obj.nome] = obj

    def saidaItem(self, item_nome):
        if item_nome in self.slots:
            del self.slots[item_nome]
            print(f'Item {item_nome} removido da mochila')
        else:
            print(f'Item {item_nome} não encontrado na mochila')

    def usarItem(self, item_nome):
        if item_nome in self.slots:
            print(f'Usando o item {item_nome}')
        else:
            print(f'Item {item_nome} não encontrado na mochila')

    def showStatus(self):
        print(f'Mochila {self.nome} tem {len(self.slots)} itens:\n{self.slots}')


class Personagem:
    def __init__(self, nome, vida, ataque, defesa, velocidade):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.slots = {}

    def status(self):
        uxVida = '+' * self.vida
        print('_______________________')
        print(f'{self.nome} | {uxVida}')
        print(f'ATK: {self.ataque} | DEF: {self.defesa}')
        print(f'VEL: {self.velocidade} | BAG: {len(self.slots)}')
        print('_______________________')

    def bag_interna(self, action):
        if action == 1 or action == 'usar':
            print('Selecione qual item deseja usar:')
        elif action == 2 or action == 'remover':
            print('Selecione qual item deseja remover:')
        else:
            print('Erro function')

    def bag_externa(self, action, add):
        if action == 1 or action == 'adicionar':
            print('Selecionando item para adicionar:')
            self.slots[add.nome] = add
        else:
            print('Erro function')

    def status_bag(self):
        for item_nome in self.slots:
            print(f'{item_nome}: {self.slots[item_nome]}')


# Criando instâncias
lucas = Personagem('Lucas', 10, 3, 2, 1)
graveto = Item('Gravetinho', {'ataque': -1}, 1)
bag = Mochila('Mochila do Lucas')

# Adicionando item à mochila
bag.entradaItem(graveto)
bag.showStatus()

# Adicionando item à mochila interna do personagem
lucas.bag_externa(1, graveto)
lucas.status()
lucas.status_bag()

# Usando item
bag.usarItem('Gravetinho')
