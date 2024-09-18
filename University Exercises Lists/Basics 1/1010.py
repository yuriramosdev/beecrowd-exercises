"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, 
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada:
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída:
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois 
pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
"""

peca1, numero_pecas1, valor_unit1 = input().split()
peca2, numero_pecas2, valor_unit2 = input().split()

peca1, numero_pecas1, peca2, numero_pecas2 = int(peca1), int(numero_pecas1), int(peca2), int(numero_pecas2)
valor_unit1, valor_unit2 = float(valor_unit1), float(valor_unit2)

pagamento = (numero_pecas1 * valor_unit1 + numero_pecas2 * valor_unit2)

print(f'VALOR A PAGAR: R$ {pagamento:.2f}')
