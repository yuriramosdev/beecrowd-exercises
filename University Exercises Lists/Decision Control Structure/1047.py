"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
"""

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

duracao_horas = 0
duracao_minutos = 0

if hora_final > hora_inicial or (hora_final == hora_inicial and minuto_final >= minuto_inicial):
    duracao_horas = hora_final - hora_inicial
    duracao_minutos = minuto_final - minuto_inicial
else:
    duracao_horas = 24 - hora_inicial + hora_final
    duracao_minutos = minuto_final - minuto_inicial

if duracao_minutos < 0:
    duracao_minutos += 60
    duracao_horas -= 1

if duracao_horas == 0 and duracao_minutos == 0:
    duracao_horas = 24

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")