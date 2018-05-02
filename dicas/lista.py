# Lista vazia
L = []

# Acessar o índice
L[0], L[1], L[2] ...

# Índice números negativos
L[-1] -- último
L[-2] -- penúltimo

# Alterar um elemento na lista
L[0] = 7

# Copiar uma lista 
V = L[:]

# Tamanho da lista
len(L) -- Retorna o número de elementos na lista

# Adicionar somente um elemento a uma lista
# Esse elemento pode ser um número, sring, outra lista ...

L = []
L.append('a') -- string
L.append(32) -- números

# Adicionar mais de um elemento a lista (lista + lista)

L = []
L.extend(['a','b','c'])
L.extend(['d'])

>> L
['a','b','c','d']

# Adição de lista com "+" (Usa o modo extend)
L = [2]
L = L + [7] # igual a L.append(7)    
>> L
[2, 7]

# Acrescentar duas listas a uma nova
l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2
>> l3
[1,2,3,4,5,6]
