menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

menu2 = """
[d] Depositar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    if numero_saques < 3:
        opcao = input(menu)
        print()
    else:
        opcao = input(menu2)
        print()

    if opcao == "d":
        deposito = float(input('Informe o valor a depositar: '))
        if deposito > 0:
            saldo += deposito
            print(f'Deposito de R$ {deposito:.2f} efetuado com sucesso!')
            extrato += f'Deposito {deposito:10.2f}\n'
        else:
            print('Valor inválido!')

    elif (opcao == "s") and (numero_saques < 3):
        print(numero_saques)
        saque = float(input('Informe o valor a sacar: '))

        if saque <= 0:
            print('Valor inválido!')
            continue

        if (saque <= saldo) and (numero_saques < 3) and (saque <= LIMITE):
            saldo -= saque
            print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
            extrato += f'Saque    {saque:10.2f}\n'
        elif saque > LIMITE:
            print(f'Pedido de saque excedeu o limite, solicite um valor abaixo do limite de {LIMITE:.2f}!')
        elif numero_saques == 3:
            print(f'Excedeu o limite de saques diários!')
        else:
            print('Não foi possível realizar o saque, reveja o saldo antes de realizar o saque novamente!')

        numero_saques += 1

    elif opcao == "e":
        print('Extrato bancário\n')
        print(extrato)
        print(f'Saldo    {saldo:10.2f}')

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
