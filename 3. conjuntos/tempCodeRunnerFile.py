
numeros = {1,2,3,4,5}
numeros.discard(3) # remove o elemento do set, se não existir não gera erro
numeros.discard(10) # não gera erro

numeros.pop() # remove um elemento aleatório do set
print(numeros)
numeros.pop()
print(numeros)

numeros.remove(2) # remove o elemento do set, se não existir gera erro
print(numeros)