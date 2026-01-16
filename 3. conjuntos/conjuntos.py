# um set é uma coleção que não possui objetos repetidos. Ele traz NÃO ordenados e é mutável.

data = set([1,2,3,1,3,4])
print(data) # saída: {1, 2, 3, 4}

print(set('banana')) # saída: {'b', 'a', 'n'

linguagens = {"Python","Java","C++","JavaScript","Python"} # saída: {'Java', 'C++', 'JavaScript', 'Python'}

print(linguagens)

#consumindo valores em um set
numeros = {1,2,3,4,5,6,7,8,9,10}
numeros = list(numeros) # convertendo set em lista
print(numeros[0])

carros = {"gol","uno","palio","fusca"}
for carro in carros:
    print(carro)

for i, carros in enumerate(carros):
    print(i, carros)

conjuntos_a = {1,2,3,4,5}
conjuntos_b = {4,5,6,7,8}

union = conjuntos_a.union(conjuntos_b) # une os dois conjuntos  

intersection = conjuntos_a.intersection(conjuntos_b) # retorna os valores que existem em ambos os conjuntos

print(union)
print(intersection)

difference = conjuntos_a.difference(conjuntos_b) # retorna os valores que existem apenas no conjunto A
print(difference)

difference_b = conjuntos_b.difference(conjuntos_a) # retorna os valores que existem apenas no conjunto B
print(difference_b)

diferenca_simetrica = conjuntos_a.symmetric_difference(conjuntos_b)
print(diferenca_simetrica) # retorna os valores que existem em apenas um dos conjuntos

subset = conjuntos_a.issubset(conjuntos_b) # verifica se o conjunto A é um subconjunto da união
print(subset)

superset = conjuntos_a.issuperset(conjuntos_b) # verifica se o conjunto A é um superconjunto da união
print(superset)

a = {1,2,3}
b = {4,5,6}
c = {1,4}
print(a.isdisjoint(b)) # True, não possuem elementos em comum
print(a.isdisjoint(c)) # False, possuem elementos em comum

# add
#adiciona apenas o que não existe no set
sorteio = {1,23}
sorteio.add(10)
sorteio.add(23)

# sorteio.clear() # limpa o set
sorteio.copy() # retorna uma cópia do set

print(sorteio)

numeros = {1,2,3,4,5}
numeros.discard(3) # remove o elemento do set, se não existir não gera erro
numeros.discard(10) # não gera erro

numeros.pop() # remove um elemento aleatório do set
print(numeros)
numeros.pop()
print(numeros)

numeros.remove(2) # remove o elemento do set, se não existir gera erro
print(numeros)

# o remove gera erro e o discard não gera erro. depende da ncessidade do programador qual usar
len(numeros) # retorna o tamanho do set