
# for - normalmente para o número exatpo de repetições
for i in range(0,5,1):
    print(i)

# for else
for i in range(5):
    
    if i == 2:
        continue
    print(i)

else:
    print("Fim do loop for")

#while

infinito = True 
x = 0

while infinito:
    print(f'contagem: {x}')
    x += 1

#while else

countagem = 100 
x = 0

while x < countagem + 1:
    print(f'contagem: {x}')
    x += 1
else:
    print("Fim do loop while")

for i in range (0,11,2):
    print(i)

print(range(0,11,2))
print(list(range(0,11,2)))

