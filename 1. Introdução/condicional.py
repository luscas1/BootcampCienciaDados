
# if/ else/ elif

saldo = 100
saque = 50

if saque <= saldo:
    print("Saque autorizado")
else:
    print("Saldo insuficiente")

idade = 23

if idade < 18:
    print("Menor de idade")

elif idade >= 18 and idade < 65:
    print("Adulto")

else:
    print("Idoso")

# if aninnhado 

tipo_conta = "comercial"
saldo = 250

if tipo_conta == "comercial":

    if saldo >= 1000:
        print("Juros de 1% ao mês")
    elif saldo < 1000 and saldo >= 500:
        print("Juros de 1.2% ao mês")
    else:
        print("Juros de 1.5% ao mês")


# if ternário
idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)