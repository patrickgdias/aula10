# biblioteca para números aleátorios
import random
import os

os.system('cls')
# n = random.randint(1, 5)
# m = random.randint(1, 5)
# print(n, m)

# lst_numeros = [random.randint(1,10) for i in range (5)]
# print (lst_numeros)


# EXEMPLO 02 - FUNÇÃO
def gerar_numeros(i, f, q):
    lst_num = [random.randint(i, f) for num in range(q)]
    return lst_num


ini = int(input('Informe o primeiro número: '))
fin = int(input('Informe o último número: '))
qtd = int(input('Quantos números? '))

numeros = gerar_numeros(ini, fin, qtd)
print(numeros)









