import datetime
from abc import ABC, abstractclassmethod, abstractproperty

def data_hora_hoje():
    data_hoje = datetime.datetime.today()
    data_config = data_hoje.strftime('%d/%m/%Y')
    return data_config

def hora_operacao(data_hoje):
    agora = datetime.datetime.now()
    data_config_hora = f'{data_hoje} {agora.strftime('%H:%M')}'
    return data_config_hora

def tela_opcoes(menu, hoje, numero_operacoes):
    print(f'{hoje} - Limite de operação diária realizável: {10-numero_operacoes}')
    opcao = input(menu)
    print()
    return opcao

def depositar(usuario_informado, conta_informado):
    global LIMITE_OPERACOES, hora, contas_usuarios

    while True:
        deposito = float(input('Informe o valor a depositar: '))

        if type(deposito) == int or type(deposito) == float:
            if (deposito > 0) and (contas_usuarios[usuario_informado][conta_informado][1] < LIMITE_OPERACOES):
                contas_usuarios[usuario_informado][conta_informado][0] += deposito
                print(f'Deposito de R$ {deposito:.2f} efetuado com sucesso!')
                contas_usuarios[usuario_informado][conta_informado][3] += f'{hora}  Deposito {deposito:10.2f}\n'
                contas_usuarios[usuario_informado][conta_informado][1] += 1
                break
            elif contas_usuarios[usuario_informado][conta_informado][1] >= LIMITE_OPERACOES:
                print('Limite de operações diárias atingidas, tente novamente em outro dia!')
            else:
                print('Valor inválido!')
        
        else:
            print('Informe números acima de 0')

def sacar(usuario_informado, conta_informado):
    global LIMITE_OPERACOES, hora, contas_usuarios

    saque = float(input('Informe o valor a sacar: '))

    if saque <= 0:
        print('Valor inválido!')
    elif saque > LIMITE:
        print(f'Pedido de saque excedeu o limite, solicite um valor abaixo do limite de {LIMITE:.2f}!')
    elif contas_usuarios[usuario_informado][conta_informado][1] == LIMITE_OPERACOES:
        print(f'Limite de operações diárias atingidas, tente novamente em outro dia!')
    elif (saque <= contas_usuarios[usuario_informado][conta_informado][0]) and (contas_usuarios[usuario_informado][conta_informado][1] < LIMITE_OPERACOES) and (saque <= LIMITE):
        contas_usuarios[usuario_informado][conta_informado][0] -= saque
        print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
        contas_usuarios[usuario_informado][conta_informado][3] += f'{hora}  Saque    {saque:10.2f}\n'
        contas_usuarios[usuario_informado][conta_informado][1] += 1
    else:
        print('Não foi possível realizar o saque, reveja o saldo antes de realizar o saque novamente!')

def mostrar_extrato(usuario_informado, conta_informado):
    global contas_usuarios

    if not contas_usuarios[usuario_informado][conta_informado][3]:
        print('Extrato bancário\n')
        print(f'                  Saldo    {contas_usuarios[usuario_informado][conta_informado][0]:10.2f}')
    else:
        print('Extrato bancário\n')
        print(contas_usuarios[usuario_informado][conta_informado][3])
        print(f'                  Saldo    {contas_usuarios[usuario_informado][conta_informado][0]:10.2f}')


def verificar_usuario():
    global usuario_informado, contas_usuarios, conta_informado

    usuario_ok = False
    conta_ok = False

    while usuario_ok == False:
        if usuario_informado not in contas_usuarios.keys():
            confirmar_criar_usuario = input('''Usuário não cadastrado, deseja cadastrar o usuário? 
            [s] - Sim
            [n] - Não
            ==> ''')
            if confirmar_criar_usuario == 's':
                criar_usuario()
            else:
                print('Digite o usuário corretamente!')
                usuario_informado = input('Usuário: ')
        else:
            usuario_ok = True
            break

    print(contas_usuarios[usuario_informado].keys())
    while conta_ok == False:
        if str(conta_informado) not in contas_usuarios[usuario_informado].keys():
            confirmar_criar_conta = input('''Conta não cadastrado, deseja cadastrar a Conta? 
            [s] - Sim
            [n] - Não
            ==> ''')
            if confirmar_criar_conta == 's':
                criar_conta()
            else:
                print('Digite a conta corretamente!')
                conta_informado = input('Conta: ')
        else:
            conta_ok == True
            break
    
    print(f'Bem vindo {usuario_informado}, {conta_informado}')

def criar_usuario():
    global dados_usuarios, usuarios, cpf_cadastrado, usuario_informado

    dados_usuario = {}

    while True:
        usuario = input('Informe como identificar o usuário ou digite [x] para cancelar o cadastro: ')
        print()

        if usuario in usuarios:
            print('Usuário cadastrado')
            break
        elif usuario == 'x':
            break
        else:
            usuarios.append(usuario)

            print('Dados cadastrais')
            nome = input('Nome completo: ')
            while True:
                data = input('Data de nascimento (dd/mm/aaaa): ')
                try:
                    datetime.datetime.strptime(data, '%d/%m/%Y')
                    break
                except ValueError:
                    print('Formáto inválido, tente novamente!')
            while True:
                cpf = int(input('CPF: '))
                if len(str(cpf)) == 11:
                    break
                else:
                    print('Digite somente 11 dígitos!')

            for _, informacao in dados_usuarios.items():
                if cpf == informacao['cpf']:
                    cpf_cadastrado = True

            if cpf_cadastrado == True:
                print('CPF já cadastrado')
                print('Digite novamente a nova conta!')
            else:
                logradouro = input('Logradouro: ')
                nro = input('Nro: ')
                bairro = input('Bairro: ')
                cidade = input('Cidade: ')
                uf = input('UF: ')
                endereco = ', '.join([logradouro, nro, bairro, cidade, uf])
                
                dados_usuario['nome'] = nome
                dados_usuario['data_nascimento'] = data
                dados_usuario['cpf'] = cpf
                dados_usuario['endereco'] = endereco

                dados_usuarios[usuario] = dados_usuario
                usuario_informado = usuario
                cpf_cadastrado = False
                break

def criar_conta():
    global contas_usuarios, usuarios, sequencia_contas

    AGENCIAS = ('0001', '0002', '0003')
    contas = {}
    conta = ''
    saldo = 0
    numero_operacoes = 0

    print('USUÁRIOS')
    for individuo in usuarios:
        print(individuo)

    while True:
        cadastrar_conta_usuario = input('Informe em qual usuário deseja cadastrar a nova conta:')
        if cadastrar_conta_usuario in usuarios:
            break
        else:
            print('Usuário não cadastrado')

    while True:
        agencia = int(input('''
Em qual agência será criada a conta:
1 - 0001
2 - 0002
3 - 0003
==> '''))
    
        if agencia == 1:
            conta += AGENCIAS[0]
            break
        elif agencia == 2:
            conta += AGENCIAS[1]
            break
        elif agencia == 3:
            conta += AGENCIAS[2]
            break
        else:
            print('Agencia inexistente, escolha uma das agencias cadastradas!')

    if agencia == 1:
        sequencia_contas[0] += 1

        conta += (5 - len(str(sequencia_contas[0]))) * '0' + str(sequencia_contas[0])
        contas[conta] = [saldo, numero_operacoes, conta, '']

    elif agencia == 2:
        sequencia_contas[1] += 1

        conta += (5 - len(str(sequencia_contas[1]))) * '0' + str(sequencia_contas[1])
        contas[conta] = [saldo, numero_operacoes, conta, '']
    
    elif agencia == 3:
        sequencia_contas[2] += 1

        conta += (5 - len(str(sequencia_contas[2]))) * '0' + str(sequencia_contas[2])
        contas[conta] = [saldo, numero_operacoes, conta, '']
        
    contas_usuarios[cadastrar_conta_usuario] = contas

class Clientes:
    pass

class PessoaFisica(Clientes):
    pass

class Conta:
    def __init__(self, saldo, ):
        pass

class ContaCorrente(Conta):
    pass

class Historico:
    pass

class Transacoes(ABC):
    pass

class Saque(Transacoes):
    pass

class Deposito(Transacoes):
    pass



menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

menu2 = """
[e] Extrato
[q] Sair

=> """

LIMITE, LIMITE_OPERACOES = ContaCorrente(500, 10)
hoje = data_hora_hoje()
hora = hora_operacao(hoje)
usuarios = []
login_senha = {}
dados_usuarios = {}
cpf_cadastrado = False
usuario_informado = ''
contas_usuarios = {} # {usuario: {conta1: [saldo, numero_operacoes]}, {conta2: [saldo, numero_operacoes]}, {conta3: [saldo, numero_operacoes]}}
sequencia_contas = [0, 0, 0]


while True:

    criar_ou_acessar = input(
        '''Bem vindo, o que deseja:
    [a] - Acessar
    [c] - Criar usuario
    [s] - Sair
    ==> ''')

    if criar_ou_acessar == 'a':
        if contas_usuarios != {}:
            print('CONTAS')
            for usuario, contas in contas_usuarios.items():
                for conta in contas.keys():
                    print(f'{usuario} - {conta}')

        usuario_informado = input('Usuário: ')
        conta_informado = input('Conta: ')
        verificar_usuario()

        if usuario_informado not in usuarios:
            continue

    elif criar_ou_acessar == 'c':
        criar_usuario()
        criar_conta()
        continue
    else:
        break

    if usuario_informado not in usuarios:
        continue

    while True:
        if contas_usuarios[usuario_informado][conta_informado][1] < LIMITE_OPERACOES:
            opcao_menu = tela_opcoes(menu, hoje, contas_usuarios[usuario_informado][conta_informado][1])
        else:
            opcao_menu = tela_opcoes(menu2, hoje, contas_usuarios[usuario_informado][conta_informado][1])

        if opcao_menu == "d":
            depositar(usuario_informado, conta_informado)

        elif (opcao_menu == "s") and (contas_usuarios[usuario_informado][conta_informado][1] < LIMITE_OPERACOES):
            sacar(usuario_informado, conta_informado)

        elif opcao_menu == "e":
            mostrar_extrato(usuario_informado, conta_informado)

        elif opcao_menu == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
