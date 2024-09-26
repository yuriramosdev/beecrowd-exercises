"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A 
representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, 
com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada:
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída:
Imprima todas as classificações do triângulo especificado na entrada.
"""

a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

lista = a, b, c 
lista_ordenada = sorted(lista, reverse=True)

if lista_ordenada[0] < lista_ordenada[1] + lista_ordenada[2]:
    t_retangulo = lista_ordenada[0] ** 2 == lista_ordenada[1] ** 2 + lista_ordenada[2] ** 2
    t_obtusangulo = lista_ordenada[0] ** 2 > lista_ordenada[1] ** 2 + lista_ordenada[2] ** 2
    t_acutangulo = lista_ordenada[0] ** 2 < lista_ordenada[1] ** 2 + lista_ordenada[2] ** 2
    t_equilatero = lista_ordenada[0] == lista_ordenada[1] == lista_ordenada[2]

    if t_retangulo:
        print('TRIANGULO RETANGULO')
    if t_obtusangulo:
        print('TRIANGULO OBTUSANGULO')
    if t_acutangulo:
        print('TRIANGULO ACUTANGULO')
    if t_equilatero:
        print('TRIANGULO EQUILATERO')
    if lista_ordenada[0] == lista_ordenada[1] != lista_ordenada[2] or lista_ordenada[0] == lista_ordenada[2] != lista_ordenada[1] or lista_ordenada[1] == lista_ordenada[2] != lista_ordenada[0]:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')