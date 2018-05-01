l = [0,0,0,0,0]
x = 0 
soma = 0 

while x < 5:
    nota = float(input('Digite a nota %d: ' %(x +1)))
    l[x] = nota
    x += 1

print('0 para sair do programa')
while True:
    e = int(input('Escolha um número para mostrar: ')) 
    if e == 0:
        break
    elif e > 5 or e < 0:
        print('Opção inválida')
    else:
        print('Posição %d: %.2f' %(e, l[e - 1]))
