"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. 
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
"""

valor = input()
valor = float(valor)

print('NOTAS:')
valor_100 = valor // 100
print(f'{valor_100:.0f} nota(s) de R$ 100.00')
valor_50 = valor % 100 // 50
print(f'{valor_50:.0f} nota(s) de R$ 50.00')
valor_20 = valor % 100 % 50 // 20
print(f'{valor_20:.0f} nota(s) de R$ 20.00')
valor_10 = valor % 100 % 50 % 20 // 10
print(f'{valor_10:.0f} nota(s) de R$ 10.00')
valor_5 = valor % 100 % 50 % 20 % 10 // 5
print(f'{valor_5:.0f} nota(s) de R$ 5.00')
valor_2 = valor % 100 % 50 % 20 % 10 % 5 // 2
print(f'{valor_2:.0f} nota(s) de R$ 2.00')

print('MOEDAS:')
valor_1 = valor % 100 % 50 % 20 % 10 % 5 % 2 // 1
print(f'{valor_1:.0f} moeda(s) de R$ 1.00')
valor_050 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 // 0.50
print(f'{valor_050:.0f} moeda(s) de R$ 0.50')
valor_025 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 // 0.25
print(f'{valor_025:.0f} moeda(s) de R$ 0.25')
valor_010 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 // 0.10
print(f'{valor_010:.0f} moeda(s) de R$ 0.10')
valor_005 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 // 0.05
print(f'{valor_005:.0f} moeda(s) de R$ 0.05')
valor_001 = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1 % 0.50 % 0.25 % 0.10 % 0.05 / 0.01
print(f'{valor_001:.0f} moeda(s) de R$ 0.01')