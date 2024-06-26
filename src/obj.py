class Item:
    def __init__(self, nome, atributo, tamanho):
        self.nome = nome
        self.atributo = atributo
        self.tamanho = tamanho

    def __repr__(self):
        return f"Item(nome={self.nome}, atributo={self.atributo}, tamanho={self.tamanho})"

class Mochila:
    def __init__(self, nome):
        self.nome = nome
        self.slots = {}

    def entradaItem(self, obj):
        self.slots[obj.nome] = obj
        print(f'Item {obj.nome} adicionado à mochila {self.nome}')

    def saidaItem(self, item_nome):
        if item_nome in self.slots:
            del self.slots[item_nome]
            print(f'Item {item_nome} removido da mochila {self.nome}')
        else:
            print(f'Item {item_nome} não encontrado na mochila {self.nome}')

    def usarItem(self, item_nome):
        if item_nome in self.slots:
            print(f'Usando o item {item_nome}')
        else:
            print(f'Item {item_nome} não encontrado na mochila {self.nome}')

    def showStatus(self):
        print(f'Mochila {self.nome} tem {len(self.slots)} itens:')
        for item_nome, item in self.slots.items():
            print(f' - {item}')

# Criando instâncias de Item
graveto = Item('Gravetinho', {'ataque': -1}, 1)
pocao = Item('Poção de Vida', {'vida': +5}, 1)
escudo = Item('Escudo de Madeira', {'defesa': +2}, 3)

# Criando uma instância de Mochila
bag = Mochila('Mochila do Lucas')

# Adicionando itens à mochila
bag.entradaItem(graveto)
bag.entradaItem(pocao)
bag.entradaItem(escudo)

# Mostrando o status da mochila
bag.showStatus()

# Removendo um item da mochila
bag.saidaItem('Gravetinho')

# Mostrando o status atualizado da mochila
bag.showStatus()

# Usando um item da mochila
bag.usarItem('Poção de Vida')
