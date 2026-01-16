# Programar em funções é o mesmo que programar de maneira estruturada - paradigma de programação

def saudacao():
    print("Olá, usuário!")

saudacao()

def saudacao_nome(nome = None):
    print(f"Seja bem vindo, {nome}!")

def saudacao_nome_posicional(nome):
    print(f"Seja bem vindo, {nome}!")


saudacao_nome(nome = "Lucas") # **kwargs preferir pois mapeia e evita problemas com futuras alterações, argumentos posicionados x nomeados
saudacao_nome(**{"nome":"Lucas"})
saudacao_nome("Lucas")
saudacao()

def soma(numeros):
    return sum(numeros)

def sucessor_antecessor(numero):
    sucessor = numero + 1
    antecessor = numero - 1
    return f'sucessor: {sucessor}\nantecessor: {antecessor}'

print(soma([1,2,3,4]))

print(sucessor_antecessor(2))


#args e kwargs - *args valores vem como tupla e **kwargs os valores vem como dicionario
def exibir_poema(data, *args, **kwargs): #pode ser qualquer nome: *lista/**dicionario ou */** ou *a/**b
    texto = "\n".join(args)
    meta_dados = "\n".join([f'\n{chave.title()}: {valor}' for chave,valor in kwargs.items()])
    mensagem = f'{data}\n\n{texto}{meta_dados}'
    print(mensagem)

exibir_poema("04/12/2025","Zen of Pyton","Beatiful is better than ugly",autor = "Tim Peters", ano = 1999)

# Parâmetros especiais

def carros(modelo,ano,placa,/,marca,motor,combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

carros("Palio",1999,"XYZ",marca="Fiat",motor=1.6,combustivel="Flex") # obriga antes da / ser posiciona, depois pode ser posicional ou por chave
carros("Palio",1999,"XYZ","Fiat",1.6,"Flex")
carros(modelo="Palio",ano=1999,placa="XYZ",marca="Fiat",motor=1.6,combustivel="Flex") # TypeError: carros() got some positional-only arguments passed as keyword arguments: 'modelo, ano, placa'

def motos(*, nome = None, marca = None, ano = None):
    print(nome,marca,ano)

motos(nome="Fazer",marca="Yamaha",ano=2012)
motos("Fazer","Yamaha",2012) # TypeError: motos() takes 0 positional arguments but 3 were given  

def bicicleta(modelo,marca,/,*,ano=None,cor=None): #hibrido  modelo ano placa por posição e ano e cor por chave
    print(modelo,marca,ano,cor)

bicicleta("Street","Caloi",ano=2020,cor="Preta")

# Objetos de primeira classe: é um objeto que pode ser passado, retornado por função ou atribuído por variável.

def somar(a,b):
    return "+", a+b

def subtrair(a,b):

    return "-", a - b

def exibir_soma(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado da operação {a} {resultado[0]} {b} = {resultado[1]}")
    
exibir_soma(2,4,somar)
exibir_soma(2,4,subtrair)

operacao = somar
print(operacao(1,2)[1])

# Escopo local e escopo global: dentro do bloco da função é local
salario = 2000

def salario_bonus(bonus,lista):
    global salario
    lista.append(2)
    salario += bonus
    return salario

lista = [1]
print(salario_bonus(100,lista))
print(lista)


salario = 2000

def salario_bonus2(bonus,lista):
    global salario
    lista_copy = lista.copy()
    lista_copy.append(2)
    print(f'aux {lista_copy}')
    salario += bonus
    return salario

lista = [1]
print(salario_bonus2(100,lista))
print(lista)
