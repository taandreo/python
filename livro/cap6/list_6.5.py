'''
Adiciona números a uma lista até digitar zero, depois mostra todos os números na ordem em que foram inseridos.
'''
l = []
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    l = l + [n]

print(l)

x = 0

while x < len(l):
    print(l[x])
    x += 1
