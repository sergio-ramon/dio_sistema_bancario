def operar_deposito():
    valor = float(input("Digite o valor do depósito: "))

    if valor > 0:
        print("Depósito realiado com sucesso!")
        return valor
    else:
        print("Valor informado é inválido!")

def operar_saque(saldo, limite):
    valor = float(input("Digite o valor do saque: "))

    excede_limite = valor > limite
    excede_saldo = valor > saldo

    if excede_limite:
        print(f"Limite máximo de R$ {limite:.2f} por saque!")
    elif excede_saldo:
        print(f"Saldo insuficiente para realizar a operação!")
    elif valor > 0:
        print("Saque realiado com sucesso!")
        return valor
    else:
        print("Valor informado é inválido!")

def exibir_extrato(extrato, saldo):
    print("="*10 + " Extrato " + "="*10)
    print("Sem movimentações no período." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("="*29)
    

menu = """

[d] - Operar depósito
[s] - Operar saque
[e] - Consultar extrato
[q] - Sair

=> """

saldo = 0.00
limite_de_saque = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = operar_deposito()
        if valor != None:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = operar_saque(saldo, limite_de_saque)
            if valor != None:
                saldo -= valor
                extrato += f"Saque de R$ {valor:.2f}\n"
                numero_saques += 1
        else:
            print("Limite de saques excedido, tente novamente mais tarde.")

    elif opcao == "e":
        exibir_extrato(extrato, saldo)

    elif opcao == "q":
        break

    else:
        print("Opção inválida! Tente novamente.")