"""
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um 
dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada:
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída:
Apresente a duração do jogo conforme exemplo abaixo.
"""

a, b = map(int, input().split())

if a > b:
    duracao = 24 - a + b
    print(f'O JOGO DUROU {duracao} HORA(S)')
elif a < b:
    duracao = b - a
    print(f'O JOGO DUROU {duracao} HORA(S)')
else:
    duracao = 24
    print(f'O JOGO DUROU {duracao} HORA(S)')