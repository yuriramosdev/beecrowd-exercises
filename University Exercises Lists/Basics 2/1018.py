"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) 
no qual o valor pode ser decomposto. As notas consideradas são 
de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo 
necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após 
cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""

valor = input()
valor = int(valor)
print(valor)
valor_100 = valor // 100
print(f'{valor_100} nota(s) de R$ 100,00')
valor_50 = valor % 100 // 50
print(f'{valor_50} nota(s) de R$ 50,00')
valor_20 = valor % 100 % 50 // 20
print(f'{valor_20} nota(s) de R$ 20,00')
valor_10 = valor % 100 % 50 % 20 // 10
print(f'{valor_10} nota(s) de R$ 10,00')
valor_5 = valor % 100 % 50 % 20 % 10 // 5
print(f'{valor_5} nota(s) de R$ 5,00')
valor_2 = valor % 100 % 50 % 20 % 10 % 5 // 2
print(f'{valor_2} nota(s) de R$ 2,00')
valor_1 = valor % 100 % 50 % 20 % 10 % 5 % 2 / 1
print(f'{valor_1:.0f} nota(s) de R$ 1,00')