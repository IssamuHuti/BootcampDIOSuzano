def mensagem():
    print('Ola, mundo!')

def mensagem2(nome):
    print(f'seja bem vindo {nome}!')

def mensagem3(nome='ninguem'):
    print(f'seja bem vindo {nome}!')

def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return [antecessor, sucessor]

def salvar_carro(marca, modelo, ano, placa):
    print('Carro registrado com sucesso!')
    print(f'''
    Marca   = {marca}
    Modelo  = {modelo}
    Ano     = {ano}
    Placa   = {placa}
    ''')

def exibir_poema(data, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem_poema = f'{data} \n\n{texto}\n\n{meta_dados}'
    print(mensagem_poema)

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # as informações antes do "/" não podem ser argumentos nomeados, ou seja, modelo='nome_modelo' não é permitido
    print(modelo, ano, placa, marca, motor, combustivel)
    # se tivesse * no meio dos parametros da função carro, tudo que vier depois desse argumento é necessariamente obrigado a ser um argumento nomeado

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def mostrar_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação é de {resultado}')

def salario_bonus(bonus, lista):
    global salario # já que não foi puxado pelo argumento da função, ela puxa a variável fora da função e dos argumentos informados

    lista_aux = lista.copy() # criou a cópia da lista principal para alteração
    lista_aux.append(2)
    print(f'lista_aux={lista_aux}')

    salario += bonus
    return salario

mensagem()
mensagem2('Lucas')
mensagem3()
mensagem3('Issamu')
mensagem3()
print()

print(calcular_total([10, 20, 34]))
print(retornar_antecessor_sucessor(10))
print()

salvar_carro('Fiat', 'Uno', 2020, 'ABD-5358')
salvar_carro(marca='Fiat', modelo='Uno', ano=2020, placa='ABD-5358')

exibir_poema('Sexta-feira, 26 de agosto de 2022', 'Zen of python', 'Beautiful is better than ugly', autor='Tim Petter', ano_poema=1999)

criar_carro('Palio', 1998, 'ADO-4323', 'Fiat', '1.0', 'Gasolina')
criar_carro('Palio', 1998, 'ADO-4323', marca='Fiat', motor='1.0', combustivel='Gasolina')
# criar_carro(modelo='Palio', ano=1998, placa='ADO-4323', marca='Fiat', motor='1.0', combustivel='Gasolina') # invalido
print()

mostrar_resultado(10, 20, somar)
mostrar_resultado(10, 20, subtrair)

op = somar

print(op(50, 10))
print()

salario = 2000

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)