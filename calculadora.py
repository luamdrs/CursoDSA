def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

print('======================')
print('      Calculadora     ')
print('======================')
print('[1] Adição')
print('[2] Subtração')
print('[3] Multiplicação')
print('[4] Divisão')
print('[5] Sair')

while True:
    opcao = input('Digite uma opção [1-4] ou 5 para sair: ')
    if opcao == '5': 
        print('>> Calculadora finalizada <<')
        break

    num1 = int(input('Digite o 1º número: '))
    num2 = int(input('Digite o 2º número: '))

    if opcao == '1':
        print(f'{num1} + {num2} = {somar(num1, num2)}')
    elif opcao == '2':
        print(f'{num1} - {num2} = {subtrair(num1, num2)}')
    elif opcao == '3':
        print(f'{num1} x {num2} = {multiplicar(num1, num2)}')
    elif opcao == '4':
        if num2 == '0':
            print('Erro: Divisão por zero não é permitida!')
        print(f'{num1} / {num2} = {dividir(num1, num2)}')
    else:
        print('Tentamos realizar a operação, mas identificamos que a opção digitada é inválida! Tente uma opção entre 1-4.')