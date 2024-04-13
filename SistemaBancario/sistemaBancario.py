# Sistema bancár
def menu():
   x=int(input('''
********Menu********
1 - Fazer Depósito
2 - Fazer Saque
3 - Mostrar Extrato
4 - Sair
Escolher: '''))
   return x
def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo = saldo + valor
        print('\nDepósito efetuado com sucesso!')
        print(f'\nSeu saldo agora é de {saldo}')
        extrato+=valor
        #cont_dep+=1
    else:
        print('\nErro!!! Valor negativo ou 0!')
    return saldo,extrato


def saqueConta(saldo, valor,extrato,cont):
    if valor <= 0:
        print('\nErro!!! Valor negativo ou 0!')
    elif valor > limite:
        print('\nSó pode até 500R$ por saque!')        
    elif valor > saldo:
        print('\nErro!!! Saldo Insuficiente!')
    elif cont == limite_saques:
        print('\nLimite de saques atingido')
    else:
        saldo -=valor
        print('\nSaque efetuado com sucesso!')
        print(f'\nSeu saldo agora é de {saldo}')
        extrato+=valor
        cont+=1
    return saldo,extrato,cont

def mostraExtrato():
    print(f'''\n
*************************************************************************
Depósitos                  | Saque                  
*************************************************************************
+ R${extrato_dep:.2f}               | - R${extrato_saque:.2f}                              
        
**************************************************************************
''')
        
saldo_conta = 0.0

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

while condicao:
    x = menu()
    if x == 1:
        valor_dep = int(input('\nQuanto deseja depositar: '))
        saldo_conta,extrato_dep=deposito(saldo=saldo_conta,valor=valor_dep,extrato=extrato_dep)
    elif x == 2:
        valor_saque = int(input('\nQuanto deseja sacar: '))
        saldo_conta, extrato_saque, cont_saque= saqueConta(saldo=saldo_conta, valor=valor_saque, extrato=extrato_saque, cont=cont_saque)
    elif x == 3:
        mostraExtrato()
    elif x == 4:
        condicao=False
    else:
        print('\nOpção inválida')
