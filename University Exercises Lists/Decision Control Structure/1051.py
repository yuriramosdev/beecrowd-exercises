"""
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não 
existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. 
A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e 
mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

de 0.00 a R$ 2000.00 - Isento
de R$ 2000.01 até R$ 3000.00 - 8%
de R$ 3000.01 até R$ 4500.00 - 18%
acima de R$ 4500.00 - 28%

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que 
fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% 
sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto. 
Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".
"""

salario = float(input())

if 0 <= salario < 2000.00:
    print('Isento')

if 2000.00 < salario <= 3000.00:
    salario_afetado = salario - 2000.00
    imposto = salario_afetado * 0.08
    print(f'R$ {imposto:.2f}')

elif 3000.00 < salario <= 4500.00:
    salario_afetado = salario - 2000.00 #se eu recebo 3500, 2000 fica isento, sobrou 1500
    salario_afetado = salario_afetado - 999.99 #retiro 999.99 que vai ser cobrado imposto de 8%, sobrou 500.01 = valor que vai ser 18%
    imposto1 = 999.99 * 0.08
    imposto2 = salario_afetado * 0.18
    imposto_final = imposto1 + imposto2
    print(f'R$ {imposto_final:.2f}')

elif salario > 4500.00:
    salario_afetado = salario - 2000 #isento
    salario_afetado = salario_afetado - 2500 #outras taxas
    imposto1 = 999.99 * 0.08
    imposto2 = 1499.99 * 0.18
    imposto3 = salario_afetado * 0.28
    imposto_final = imposto1 + imposto2 + imposto3
    print(f'R$ {imposto_final:.2f}')