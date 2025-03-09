# Title: Desafio - Caixa Eletrônico
# Description: Simulação de um caixa eletrônico com as opções de depósito, saque e extrato.

menu = """
Escolha uma das opções abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Quanto deseja depositar? "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("ERRO! O valor informado é inválido.")

    elif opcao == "2":
        saque = float(input("Quanto deseja sacar? "))
        
        if saque > saldo:
            print("ERRO! Você não tem saldo suficiente.")

        elif saque > limite:
            print("ERRO! O valor do saque excede o seu limite.")

        elif quantidade_saques >= LIMITE_SAQUES:
            print("ERRO! Número máximo de saques atingido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            quantidade_saques += 1

        else:
            print("ERRO! O valor informado é inválido.")

    elif opcao == "3":
        print("\n=========== EXTRATO BANCÁRIO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato) #Se extrato for vazio, imprime a mensagem. Se não, imprime o extrato.
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("ERRO! Por favor selecione uma opção válida.")
