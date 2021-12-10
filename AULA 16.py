
numero = input('Digite um numero inteiro ')

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print('O numero e par')
    else:
        print('Esse numero e impar')
else:
    print('O numero nao e um numero inteiro')





