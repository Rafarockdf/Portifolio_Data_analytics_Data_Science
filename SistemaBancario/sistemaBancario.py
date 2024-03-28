# Sistema bancár

saldo = 0.0
saque = 0.0
extrato = 0.0
limite = 500
limite_saques=3
condicao=True
i=0
y=0
extrato_dep=0.0
extrato_saque=0.0
cont_saque=0
cont_dep=0
menu='''
********Menu********
1 - Fazer Sepósito
2 - Fazer Saque
3 - Mostrar Extrato
4 - Sair
Escolher: '''
while condicao:
    x = int(input(menu))
    
    if x == 1:
        valor_dep = int(input('\nQuanto deseja depositar: '))
        if valor_dep > 0:
            saldo = saldo + valor_dep
            print('\nDepósito efetuado com sucesso!')
            print(f'\nSeu saldo agora é de {saldo}')
            extrato_dep+=valor_dep
            i+=1
            cont_dep+=1
        else:
            print('\nErro!!! Valor negativo ou 0!')     
    elif x == 2:
        valor_saque = int(input('\nQuanto deseja depositar: '))
        if valor_saque <= 0:
            print('\nErro!!! Valor negativo ou 0!')
        elif valor_saque > limite:
            print('\nSó pode até 500R$ por saque!')
        elif valor_saque > saldo:
            print('\nErro!!! Saldo Insuficiente!')
        elif cont_saque == limite_saques:
            print('\nLimite de saques atingido')
        else:
            saldo -=valor_saque
            print('\nSaque efetuado com sucesso!')
            print(f'\nSeu saldo agora é de {saldo}')
            extrato_saque+=valor_saque
            y+=1
            cont_saque+=1
    elif x == 3:
        print(f'''\n
*************************************************************************
Depósitos                  | Saque                  
*************************************************************************
+ R${extrato_dep:.2f}               | - R${extrato_saque:.2f}                              
        
**************************************************************************
''')
        
    elif x == 4:
        condicao=False
    else:
        print('\nOpção inválida')