# é uma sequência mutável e ordenada de elementos, que pode armazenar qualquer objeto (int,float,str,listas etc)

# declaração de listas
frutas = ['banana', 'maçã', 'laranja', 'uva']
frutas_vazias = [] # lista vazia

letras = list('python')
print(letras)

lista = list(range(10))

print(frutas[0])
print(frutas[-1]) # último elemento
print(frutas[1:3]) # fatiamento

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
print(matriz[0])
print(matriz[0][1])
print(matriz[2][-1])

lita_carros = ['gol', 'uno', 'palio']

for index, carro in enumerate(lita_carros):
    print(carro), print(index)

#list comprehension

numeros = [1, 2, 3, 4, 5]
quadrados = [n**2 for n in numeros]

pares = [n for n in numeros if n % 2 == 0]
# = retorno, for iterador, condição
# ou 

# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)

print(quadrados)
print(pares)

#métodos da classe list
lista.append(0) # adiciona um elemento ao final da lista
lista.clear() # limpa a lista
lista.copy() # retorna uma cópia da lista

l1 = [1, 2, 3]
l2 = l1.copy()

l2[0] = 0

print(l1)
print(l2)

l3 = l1 # não cria uma cópia, apenas referencia a mesma lista
l3[0] = 9
print(l1)
print(l3)

lista.count(2) # conta quantas vezes o elemento aparece na lista
lista.extend([10, 11, 12]) # adiciona vários elementos ao final da lista
lista.insert(0, -1) # insere um elemento na posição desejada
lista.index(3) # retorna o índice do primeiro elemento encontrado
lista.pop() # remove e retorna o último elemento da lista
lista.remove(2) # remove a primeira ocorrência do elemento especificado
lista.reverse() # inverte a ordem dos elementos na list
lista.sort() # ordena os elementos da lista
lista.sort(reverse=True) # ordena em ordem decrescente
lista.sort(key=lambda x: len(x)) # ordena com base em uma função personalizada
lista.sort(key=lambda x: len(x), reverse=True) # ordena com base em uma função personalizada em ordem decrescente
sorted(lista) # retorna uma nova lista ordenada sem modificar a original

lista = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(lista)