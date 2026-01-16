curso = 'PyTHOn'

print(curso.upper())

print(curso.lower())

print(curso.title())

nome = ' Lucas Motta '

print(nome.strip())

print(nome.lstrip())

print(nome.rstrip())

curso2 = 'python'

print(curso2.center(10,'#'))

print('-'.join(curso2))

# fatiamento
nome2 = 'Lucas Vinicius Motta da Silva'
print(nome2[0])

print(nome2[0:5])

print(nome2[14:])

print(nome2[0:5:2])

print(nome2[::-1])


mensagem = f"""
Olá, meu nome é {nome2} 
e eu estou aprendendo {curso2.upper()}!"""

print(mensagem)