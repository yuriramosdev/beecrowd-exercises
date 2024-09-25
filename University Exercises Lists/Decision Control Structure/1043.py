"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. 
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X

Entrada:
A entrada contém três valores reais.

Saída:
O resultado deve ser apresentado com uma casa decimal.
"""

a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

lista = a, b, c
lista_ordenada = sorted(lista)
area = ((a + b) * c) / 2
perimetro = a + b + c

if lista_ordenada[0] + lista_ordenada[1] > lista_ordenada[2]:
    print(f'Perimetro = {a + b + c}')
else:
    print(f'Area = {area}')