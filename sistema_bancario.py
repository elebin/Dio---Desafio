menu = '''
Escolha uma das opções:

 [1] Deposito
 [2] Saque
 [3] Extrato
 [4] Sair
'''

    

limite_de_saque = 3
limite = 500
saldo = 0
numero_saque = 0



while True :

    opcao = input(menu)
    
    if opcao == "1":
        print("Deposito")
        valor_deposito = int(input("Insira valor de deposito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Seu novo saldo é de : ${saldo}")
        else:
            print("Valor invalido para deposito")

    elif opcao == "2":
        print("Saque")
        saque = int(input("Qual valor deseja sacar?: "))

        if saque > limite :
            print("Operação invalida, limite atingido!")
        
        elif saque > saldo:
            print("Saldo insuficiente.")

        elif numero_saque > limite_de_saque:
            print("Limite de saques diários atingido!")
        
        elif saque <= saldo and numero_saque <= limite_de_saque:
            saldo -= saque
            print(f"Seu novo saldo é de: ${saldo}")
            numero_saque += 1
            limite_de_saque -= 1
            print(f"Esse foi seu saque n° {numero_saque} e restam {limite_de_saque} saques diários")
        
    elif opcao == "3":
        print("Extrato")
        print(f'''
    Saldo corrente: ${saldo}
    Saques realizados: {numero_saque}
    ''')
        


        
        
    else:
        break
        
            
