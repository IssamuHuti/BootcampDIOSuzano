class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # __init__ -> método contrutor ou inicializador
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1
        # self.alguma_caracteristica = atributo de uma classe
        # self é uma referencia explicita

        # __del__ -> método destrutor, coletor de lixo, não é necessário no python

    def buzinar(self):
        print('Plim plim')

    def parar(self):
        print('Parando bicicleta')
        print('Bicicleta parada')

    def correr(self):
        print('Swimmmmm ... ')

    def trocar_marcha(self, nro_marcha):
        # print(nro_marcha) # nro_marcha está recebendo o valor self da classe
        print('Trocando de marcha')

        def troca_marcha():
            if nro_marcha > self.marcha:
                print('Marcha trocada')
            else:
                print('Não foi possivel trocar de marcha')

    # def __str__(self):
    #     return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'
    # sem essa função, fazendo print da variável que impôs as caracteristicas, sai uns valores irreconheciveis

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'
    # dessa forma, não precisaria informar caracteristica por caracteristica para todas elas definidas em __init__

b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('verde', 'monark', 2000, 190)
# b2.buzinar()
# Bicicleta.buzinar(b2)
# as duas linhas acima executam a mesma função

print(b2)
b2.trocar_marcha()
