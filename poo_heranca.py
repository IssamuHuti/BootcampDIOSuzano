# herança unica (simples)

class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o motor!')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, carregado, cor, placa, numero_rodas): # está fazendo a troca de implementação de método informado na classe base
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def esta_carregado(self):
        print(f'{'Sim' if self.carregado else 'Não'} está carregado')

moto = Moto('Preta', 'ABC1234', 2)
moto.ligar_motor()

carro = Carro('Branco', 'XYZ', 4)
carro.ligar_motor()

caminhao = Caminhao('Verde', 'DEL5465', 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)


# herança multipla

class Animal():
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): # **kw está pegando da classe pai (Animal) todas as caracteristicas e metodos
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

    def __str__(self):
        return self.__class__.__name__ # retorna o nome da classe que o chamar


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

    def __str__(self):
        return 'ave 42'

class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, nro_patas):
        print(Ornitorrinco.__mro__)

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


class FalarMixin:
    def Falar(self):
        return 'Ola mundo'


gato = Gato(nro_patas=4, cor_pelo='Preto') # a chamada das classificações virou nomeada por causa que as caracteristicas herdadas da classe pai foi compactada em **kw
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo='Marrom', cor_bico='Vermelho')
print(ornitorrinco)
