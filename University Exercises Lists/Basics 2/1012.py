"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. 
Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, 
sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. 
O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
"""

a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

area_triangulo = (a * c) / 2
print(f'TRIANGULO: {area_triangulo:.3f}')

area_circulo = 3.14159 * (c ** 2)
print(f'CIRCULO: {area_circulo:.3f}')

area_trapezio = ((a + b) * c) / 2
print(f'TRAPEZIO: {area_trapezio:.3f}')

area_quadrado = b ** 2
print(f'QUADRADO: {area_quadrado:.3f}')

area_retangulo = a * b
print(f'RETANGULO: {area_retangulo:.3f}')