"""
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. 
Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". 
Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". 
Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". 
Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. 
Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. 
Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a 
mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). 
Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última 
linha uma mensagem "Media final: " seguido da média final para esse aluno.

Entrada:
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

Saída:
Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema. 
Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".
"""

n1, n2, n3, n4 = input().split()
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)

peso_n1 = 2
peso_n2 = 3
peso_n3 = 4
peso_n4 = 1

media = (n1 * peso_n1 + n2 * peso_n2 + n3 * peso_n3 + n4 * peso_n4) / (peso_n1 + peso_n2 + peso_n3 + peso_n4)
print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota_exame = input()
    nota_exame_float = float(nota_exame)
    print(f'Nota exame: {nota_exame_float:.1f}')
    media_final = (media + nota_exame_float) / 2
    if media_final >= 5.0:
        print(f'Aluno aprovado.\nMedia final: {media_final:.1f}')
    elif media_final < 5.0:
        print(f'Aluno reprovado.\nMedia final: {media_final:.1f}')