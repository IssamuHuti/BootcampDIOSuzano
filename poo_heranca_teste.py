class Veiculo():
    def __init__(self,modelo, cor, nro_rodas, placa, ano):
        self.modelo = modelo
        self.cor = cor
        self.nro_rodas = nro_rodas
        self.placa = placa
        self.ano = ano

    def incluir_dados_veiculo():
        tipo_veiculo = input('''Veiculo: 
1 - Moto
2 - Carro
3 - Caminhao
==> ''')
        modelo = input('Modelo do veiculo  : ')
        cor    = input('Cor do veiculo     : ')
        rodas  = input('Quantidade de rodas: ')
        placa  = input('Placa do veiculo   : ')
        ano    = input('Ano do veiculo     : ')

        return tipo_veiculo, modelo, cor, rodas, placa, ano

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


class Carro(Veiculo):
    def __init__(self,modelo, cor, nro_rodas, placa, ano, revisado, estoque):
        super().__init__(modelo, cor, nro_rodas, placa, ano)
        self.revisado = revisado
        self.estoque = estoque


class Moto(Veiculo):
    def __init__(self,modelo, cor, nro_rodas, placa, ano, revisado, estoque):
        super().__init__(modelo, cor, nro_rodas, placa, ano)
        self.revisado = revisado
        self.estoque = estoque


class Caminhao(Veiculo):
    def __init__(self,modelo, cor, nro_rodas, placa, ano, revisado, estoque):
        super().__init__(modelo, cor, nro_rodas, placa, ano)
        self.revisado = revisado
        self.estoque = estoque


veiculos = {'carros':{}, 'motos':{}, 'caminhoes':{}}

while True:
    tipo_veiculo, modelo, cor, rodas, placa, ano = Veiculo.incluir_dados_veiculo()
    if tipo_veiculo == '1':
        moto = Moto(modelo, cor, rodas, placa, ano, True, True)
        print(moto)

        veiculos['motos'][modelo] = [cor, rodas, placa, ano]
        break

    elif tipo_veiculo == '2':
        moto = Carro(modelo, cor, rodas, placa, ano, True, True)
        print(moto)

        veiculos['carros'][modelo] = [cor, rodas, placa, ano]
        break

    elif tipo_veiculo == '3':
        moto = Caminhao(modelo, cor, rodas, placa, ano, True, True)
        print(moto)

        veiculos['caminhoes'][modelo] = [cor, rodas, placa, ano]
        break
    else:
        print('Selecione somente as opções disponiveis')
        continue
for veiculo, dict in veiculos.items():
    for modelo, chars in dict.items():
        print(f'{modelo}: {chars}')

print(moto.revisado)
print(moto.estoque)
