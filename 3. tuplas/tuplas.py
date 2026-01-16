# As tuplas são imutáveis, do começo ao fim do código

tupla = ('Python', 'Java', 'C++', 'JavaScript',) # virgula no final é opcional, mas recomendada para boas praticas para não confundir com parênteses comuns de precedencia

frutas = ['banana', 'maçã', 'laranja', 'uva']

letras = tuple('python')

frutas_tupla = tuple(frutas) # convertendo lista em tupla

print(frutas_tupla[0])
print(letras[0:2])

# metodos

print(tupla.count('Java')) # conta quantas vezes o elemento aparece na tupla
print(tupla.index('C++')) # retorna o índice do elemento
print(len(tupla)) # tamanho da tupla

carros = ("gol") 
print(isinstance(carros, tuple))

soma_aulas = 6 + 10 + 10 + 7 + 7 + 7 + 4 + 4
print(soma_aulas)

