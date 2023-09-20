# Calculos básicos
def somar(*args):
    sum=0
    for i in args:
      sum +=i
    return sum

def subtrair(a, b):
    return float(a) - float(b)

def dividir(a, b):
    if b==0:
        return 0
    return  float(a) / float(b)

def multiplicar(*args):
      multiplicar=1
      for i in args:
        multiplicar=multiplicar*i
      return multiplicar

def potencia(a, b):
    return float(a) ** float(b)

def porcentagem(a,b):
    return float(a) * float(b/100)
  
# Estatística
def media(*a):
  soma=0
  qtd=len(a)
  for i in a:
    soma+=i
  media = soma/qtd
  return media

def media_ponderada(a):
  c = 1
  soma = 0
  soma_pesos = 0
  while(a >= c):
    b = float(input('Digite os valores para a média: '))
    P = int(input('Digite o peso: '))
    soma_pesos = soma_pesos + P
    peso = b * P
    soma = soma + peso
    c += 1
  media = soma/soma_pesos
  return media

def mediana(array):
  lista2 = []
  lista = array
  lista1 = sorted(lista)
  a = len(lista1)
  b = a // 2
  if a % 2 ==0:
    lista2.append(lista1[b])
    lista2.append(lista1[b-1])
  else:
    lista2.append(lista1[b])
  return lista2
# Cálculos financeiros
def juros_simples(capital, taxa_juros, tempo):
  juros=(capital*(taxa_juros/100)*tempo)
  montante=capital+juros
  return montante

def juros_compostos(capital, taxa_juros, tempo):
  montante=capital*potencia((1+(taxa_juros/100)),tempo)
  return montante

# Binários
def decimal_binario(x):
  lista = []
  cont = 0
  while(x / 2 > 0):
    aux = x % 2
    x = x // 2
    lista.append(aux)
    cont = cont + 1
  lista.reverse()
  for i in lista:
     print(i)

def decimal_octal(x):
  lista = []
  cont = 0
  while(x / 8 > 0):
    aux = x % 8
    x = x // 8
    lista.append(aux)
    cont = cont + 1
  lista.reverse()
  for i in lista:
    print(i)

def decimal_hexadecimal(x):
  lista = []
  cont = 0
  while(x / 16 > 0):
    aux = x % 16
    x = x // 16
    lista.append(aux)
    cont = cont + 1
  lista.reverse()
  for i in lista:
    print(i)

def binario_decimal(x):
  lista = []
  z = 1
  soma = 0
  for i in range(x):
    y = int(input(f'Digite o {z}º número: '))
    lista.append(y)
    z += 1
  x = x - 1
  for i in lista:
    w = i*2**x
    soma += w
    x = x - 1
  print(soma)

def octal_decimal(x):
  lista = []
  z = 1
  soma = 0
  for i in range(x):
    y = int(input(f'Digite o {z}º número: '))
    lista.append(y)
    z += 1
  x = x - 1
  for i in lista:
    w = i*8**x
    soma += w
    x = x - 1
  print(soma)

def hexadecimal_decimal(x):
  lista = []
  z = 1
  soma = 0
  for i in range(x):
    y = int(input(f'Digite o {z}º número: '))
    lista.append(y)
    z += 1
  x = x - 1
  for i in lista:
    w = i*16**x
    soma += w
    x = x - 1
  print(soma)

def octal_binario(x):
  tabela =  {'0':'000',
        '1':'001',
        '2':'010',
        '3':'011',
        '4':'100',
        '5':'101',
        '6':'110',
        '7':'111'}
  z = 1
  lista = []
  for i in range(x):
    y = input(f'Digite o {z}º número: ')
    z +=1
    for i in tabela:
      lista.append(tabela[y])
      break
  for i in lista:
    print(i, end=" ")

def hexadecimal_binario(x):
  tabela =  {'0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'}
  z = 1
  lista = []
  for i in range(x):
    y = input(f'Digite o {z}º número: ')
    z +=1
    for i in tabela:
      lista.append(tabela[y])
      break
  for i in lista:
    print(i)

def binario_octal(x):
  tabela =  {'000':'0',
        '001':'1',
        '010':'2',
        '011':'3',
        '100':'4',
        '101':'5',
        '110':'5',
        '111':'7'}
  z = 1
  lista = []
  for i in range(x):
    y = input(f'Digite o {z}º número: ')
    z +=1
    for i in tabela:
      lista.append(tabela[y])
      break
  for i in lista:
    print(i)

def binario_hexadecimal(x):
  tabela =  {'0000':'0',
        '0001':'1',
        '0010':'2',
        '0011':'3',
        '0100':'4',
        '0101':'5',
        '0110':'6',
        '0111':'7',
        '1000':'8',
        '1001':'9',
        '1010':'A',
        '1011':'B',
        '1100':'C',
        '1101':'D',
        '1110':'E',
        '1111':'F'}
  z = 1
  lista = []
  for i in range(x):
    y = input(f'Digite o {z}º número: ')
    z +=1
    for i in tabela:
      lista.append(tabela[y])
      break
  for i in lista:
    print(i)

