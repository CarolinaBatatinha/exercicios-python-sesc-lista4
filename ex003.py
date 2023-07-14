#3.	Faça um algoritmo para calcular o cubo e o quadrado de todos os números pertencentes a um intervalo, incluindo o limite superior e inferior (utilize uma função criada por você que retorne o valor do cubo e do quadrado do número).
from math import pow

def calcula_quadrado(i):
    quadrado = pow(i, 2)
    print(f'{i}² = {quadrado}')

def calcula_cubo(i):
    cubo = pow(i,3)
    print(f'{i}³ = {cubo}')

limite_inferior = int(input('Defina um número como limite inferior: '))
limite_superior = int(input('Defina um número como limite superior: '))

for i in range(limite_inferior, limite_superior+1):
    print()
    calcula_quadrado(i)
    calcula_cubo(i)
    print()


