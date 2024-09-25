"""
Leia 3 valores inteiros e ordene-os em ordem crescente. 
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada:
A entrada contem três números inteiros.

Saída:
Imprima a saída conforme foi especificado.
"""

v1, v2, v3 = input().split()
v1, v2, v3 = int(v1), int(v2), int(v3)

lista = v1, v2, v3

lista_ordem = sorted(lista)

print(f'{lista_ordem[0]}\n{lista_ordem[1]}\n{lista_ordem[2]}\n\n{lista[0]}\n{lista[1]}\n{lista[2]}')