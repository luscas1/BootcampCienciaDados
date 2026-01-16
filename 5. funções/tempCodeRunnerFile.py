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
