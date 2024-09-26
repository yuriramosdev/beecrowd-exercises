salario_inicial = float(input())
salario_com_reajuste = 0
reajuste = 0
percentual = 0

if 0 < salario_inicial <= 400:
    percentual += 15
    reajuste = salario_inicial * percentual / 100
    novo_salario = salario_inicial + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')
elif 400 < salario_inicial <= 800:
    percentual += 12
    reajuste = salario_inicial * percentual / 100
    novo_salario = salario_inicial + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')
elif 800 < salario_inicial <= 1200:
    percentual += 10
    reajuste = salario_inicial * percentual / 100
    novo_salario = salario_inicial + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')
elif 1200 < salario_inicial <= 2000:
    percentual += 7
    reajuste = salario_inicial * percentual / 100
    novo_salario = salario_inicial + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')
else:
    percentual += 4
    reajuste = salario_inicial * percentual / 100
    novo_salario = salario_inicial + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')