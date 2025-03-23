import datetime

def data_hora_hoje():
    data_hoje = datetime.datetime.today()
    data_config = data_hoje.strftime('%d/%m/%Y')
    return data_config

def hora_operacao(data_hoje):
    agora = datetime.datetime.now()
    data_config_hora = f'{data_hoje} {agora.strftime('%H:%M')}'
    return data_config_hora

def abertura(menu, hoje, numero_operacoes):
    print(f'{hoje} - Limite de operação diária realizável: {10-numero_operacoes}')
    opcao = input(menu)
    print()
    return opcao

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


saldo = 0
LIMITE = 500
extrato = ""
numero_operacoes = 0
LIMITE_OPERACOES = 10
hoje = data_hora_hoje()
hora = hora_operacao(hoje)


while True:
    if numero_operacoes < LIMITE_OPERACOES:
        opcao_menu = abertura(menu, hoje, numero_operacoes)
    else:
        opcao_menu = abertura(menu2, hoje, numero_operacoes)

    if opcao_menu == "d":
        deposito = float(input('Informe o valor a depositar: '))
        if (deposito > 0) and (numero_operacoes < LIMITE_OPERACOES):
            saldo += deposito
            print(f'Deposito de R$ {deposito:.2f} efetuado com sucesso!')
            extrato += f'{hora}  Deposito {deposito:10.2f}\n'
        elif numero_operacoes >= LIMITE_OPERACOES:
            print('Limite de operações diárias atingidas, tente novamente em outro dia!')
            continue
        else:
            print('Valor inválido!')
            continue

        numero_operacoes += 1

    elif (opcao_menu == "s") and (numero_operacoes < LIMITE_OPERACOES):
        saque = float(input('Informe o valor a sacar: '))

        if saque <= 0:
            print('Valor inválido!')
            continue

        if (saque <= saldo) and (numero_operacoes < LIMITE_OPERACOES) and (saque <= LIMITE):
            saldo -= saque
            print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
            extrato += f'{hora}  Saque    {saque:10.2f}\n'
        elif saque > LIMITE:
            print(f'Pedido de saque excedeu o limite, solicite um valor abaixo do limite de {LIMITE:.2f}!')
            continue
        elif numero_operacoes == LIMITE_OPERACOES:
            print(f'Limite de operações diárias atingidas, tente novamente em outro dia!')
            continue
        else:
            print('Não foi possível realizar o saque, reveja o saldo antes de realizar o saque novamente!')
            continue

        numero_operacoes += 1

    elif opcao_menu == "e":
        print('Extrato bancário\n')
        print(extrato)
        print(f'                  Saldo    {saldo:10.2f}')

    elif opcao_menu == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
