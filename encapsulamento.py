# encapsulamento
class Conta:
    nacionalidade = 'brasileira' # variável de classe

    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # variável de instância
        self.nro_agencia = nro_agencia # variável de instância

    def depositar(self, valor):
        self.valor = valor

    def sacar(self, valor):
        self.valor = valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta('0001', 100)
conta.depositar(100)
print(conta.nro_agencia)

print(conta._saldo)


# propriedades (property)

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)
foo.x = 10
del foo.x
print(foo.x)


# variaveis de classe e variaveis de instancia
class Estudante:
    escola = 'DIO'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante('Lucas', 1)
aluno2 = Estudante('Maria', 2)
mostrar_valores(aluno1, aluno2)

Estudante.escola = 'Python'
aluno1.matricula = 3
aluno3 = Estudante('Joao', 4)

mostrar_valores(aluno1, aluno2, aluno3)


# Metodo de classe e metodo estatico

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod # quando for chamar o método, não será necessário instanciar nenhum dado na chamada, somente pegando as instâncias definidas na instância __init__
    # utiliza somente quando precisa pegar alguma instância dentro da classe
    # metodo de classe = metodo de fabrica
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod # utiliza quando não precisa pegar nenhuma instância dentro da classe 
    def e_de_maior(idade):
        return idade >= 18
    

p = Pessoa.criar_de_data_nascimento(1998, 20, 2, 'Lucas')
Pessoa.e_de_maior(18)
Pessoa.e_de_maior(28)
Pessoa.e_de_maior(16)


# Classa Abstrata

from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC): # classe abstratas não podem ser instanciadas, porém, os métodos abstratos precisam ser implementadas pelas classes filhas, o que força a uma padronização das classes filhas
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando TV')

    def desligar(self):
        print('Desligando TV')

    @property
    def marca(self):
        return 'LG'


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando Ar Condicionado')

    @property
    def marca(self):
        return 'LG'


controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar() # após iniciar essa linha, vai ocorrer erro, pois o metodo ''desligar'' informado em ControleRemoto não está informado dentro da classe ControleArCondicionado
