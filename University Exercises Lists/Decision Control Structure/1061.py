from datetime import datetime
"""
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, 
iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez 
que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar 
Pedrinho a calcular a duração deste evento.

Entrada:
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês 
no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. 
Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída:
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.
"""

inicio = input('Digite o dia de início do evento: ')
hora_inicio = input('Digite a hora de início do evento (hh : mm : ss): ')
fim = input('Digite o dia de término do evento: ')
hora_fim = input('Digite a hora de término do evento (hh : mm : ss): ')

#separar apenas o dia do mês
inicio = int(inicio.split()[1])
fim = int(fim.split()[1])

#formatando data e hora
data_inicio = f'2024-04-{inicio} {hora_inicio}'
data_fim = f'2024-04-{fim} {hora_fim}'

#convertendo para objetos datetime
datacomeco = datetime.strptime(data_inicio, '%Y-%m-%d %H : %M : %S')
datafinal = datetime.strptime(data_fim, '%Y-%m-%d %H : %M : %S')

#diferença
diferenca = datafinal - datacomeco

#separar os dias, horas, minutos e segundos
dias = diferenca.days
segundostotais = diferenca.seconds
horas = segundostotais // 3600
minutos = (segundostotais % 3600) // 60
segundos = segundostotais % 3600 % 60

print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')