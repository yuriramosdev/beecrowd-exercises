"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

codigo   especif.           preço
1        cachor quente      R$ 4,00
2        x-salada           R$ 4,50
3        x-bacon            R$ 5,00
4        torrada simples    R$ 2,00
5        refri              R$ 1,50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
"""

l1 = 4.00
l2 = 4.50
l3 = 5.00
l4 = 2.00
l5 = 1.50

print('Digite abaixo qual lanche você quer, e quantas unidades.')
cod, qtd = input().split()
cod, qtd = int(cod), int(qtd)

if cod == 1:
    conta = l1 * qtd
    print(f'Total: R$ {conta:.2f}')
elif cod == 2:
    conta = l2 * qtd
    print(f'Total: R$ {conta:.2f}')
elif cod == 3:
    conta = l3 * qtd
    print(f'Total: R$ {conta:.2f}')
elif cod == 4:
    conta = l4 * qtd
    print(f'Total: R$ {conta:.2f}')
elif cod == 5:
    conta = l5 * qtd
    print(f'Total: R$ {conta:.2f}')
else:
    print('Não temos esse lanche')