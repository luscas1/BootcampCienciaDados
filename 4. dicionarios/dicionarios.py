# dicionario é um cojunto não ordenado de par chave: valor separada por vírgulas
# dicionarios são representados por chaves {}

# a chave deve ser um objeto imutável (string, número ou tupla)
# o valor pode ser qualquer tipo de objeto (mutável ou imutável)

pessoa = {
    'nome': 'Lucas',
    'idade': 23,
    'cidade': 'Rio de Janeiro'
}

# ou 

pessoa = dict(nome='Lucas',idade=23,cidade='Rio de Janeiro')

pessoa['telefone'] = '21974208294'
print(pessoa)

print(pessoa['nome'])

pessoa['cidade'] = 'São Paulo'
print(pessoa)

# dicionarios aninhados

contatos = {
    "lucas@gmail.com": {"nome": "Lucas", "telefone": "123"},
    "beatriz@gmail.com": {"nome": "Beatriz", "telefone": "456"},
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "789"},
    "duda@gmail.com": {"nome": "Duda", "telefone": "101112", "extra": {"a": 1}},
}

print(contatos["lucas@gmail.com"]["telefone"])  # Acessa o telefone de Lucas

print(contatos["duda@gmail.com"]["extra"]["a"])

# iterando sobre dicionarios

for email in contatos:
    print(email, contatos[email])

for chave, valor in contatos.items():
    print(chave, valor)

# métodos 

# copy
copia = contatos.copy()
print(copia)

# clear
copia.clear()

# fromkeys
novodic = dict.fromkeys(['nome', 'idade', 'cidade'])
print(novodic)

novodic2 = dict.fromkeys(['nome', 'idade', 'cidade'], 'vazio')
print(novodic2)

# get
# contatos['chave'] # keyerror
contatos.get('chave') # não da erro e atribui null
contatos.get('chave', {}) # não da erro e atribui {}
contatos.get('lucas@gmail.com', {}) # encontra a chave e traz o resultado certo

# items

print(contatos.items()) # retorna tupla com cada item do dict

# keys

print(contatos.keys())

# pop

pop = contatos.pop('duda@gmail.com')

print(pop)

# pop2 = contatos.pop('duda@gmail.com') # da erro por não encontrar

pop2 = contatos.pop('duda@gmail.com', 'não encontrado') # evita o erro
print(pop2)

# popitem

print(contatos)
print(contatos.popitem()) # apaga o último e retorna o item apagado

#setdefault
nomes = {"nome": "Lucas", "estado": "RJ"}
print(nomes)
ns = nomes.setdefault("nome", "Pedro" )
print(ns)
nomes2 = nomes.setdefault("idade", 23)
print(nomes) #adiciona se não ta e retorna oq add

# update
contatos2 = {"lucas@gmail.com": {"nome": "Lucas", "telefone": 1234}}

contatos2.update({"lucas@gmail.com": {"nome": "Lu"}})

print(contatos2)

contatos2.update({"teste@gmail.com": {"nome": "teste", "telefone": 5678}})

print(contatos2)

# values, quando n precisa saber as chaves.

print(contatos2.values())

# in 

contatos3 = {
    "lucas@gmail.com": {"nome": "Lucas", "telefone": "123"},
    "beatriz@gmail.com": {"nome": "Beatriz", "telefone": "456"},
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "789"},
    "duda@gmail.com": {"nome": "Duda", "telefone": "101112", "extra": {"a": 1}},
}

result = "lucas@gmail.com" in contatos3
result_nome = "nome" in contatos3["lucas@gmail.com"]

print(result)
print(result_nome)

# del, remove o objeto passado

del contatos3["lucas@gmail.com"]["telefone"]
del contatos3["duda@gmail.com"]

print(contatos3)

carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
print(carro.get('motor'))