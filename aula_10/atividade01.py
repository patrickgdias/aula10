# CALCULADORA
import random


def adicao(x, y):
    a = x + y
    return a


def divisao(x, y):
    d = x / y
    return d


def multiplicacao(x, y):
    m = x * y
    return m


def substracao(x, y):
    s = x - y
    return s 


# Inicio do programa
# x = int(input('Digite o primeiro número: '))
# y = int(input('Digite o segundo número: '))
x = random.randint(1, 100)
y = random.randint(1, 100)


a = adicao(x, y)
d = divisao(x, y)
m = multiplicacao(x, y)
s = substracao(x,y)

print(f' A soma dos números é {a}')
print(f' A multiplicacao dos números é {m}')
print(f' A divisao dos números é {d}')
print(f' A substração dos números é {s}')
