'''
Faça um programa que leia duas listas e que gere uma terceira com os elementos da primeira.
'''

## lista 1
l1 = []
while True:
    e = input('Digite um elemento para ser adicionado na lista 1 (0 para sair): ')
    if e == '0':
        break
    l1.append(e)

## lista 2
l2 = []
while True:
    e = input('Digite um elemento para ser adicionado na lista 2 (0 para sair): ')
    if e == '0':
        break
    l2.append(e)

## lista 3
l3 = l1 + l2

print(l3)
