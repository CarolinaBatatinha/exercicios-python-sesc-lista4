#4.	Elabore um algoritmo para ler os números N e P, e calcule a exponenciação de N^P utilizando uma função chamada expon( ... ) que você deverá criar.

from math import pow

def expon(N, P):
    res = pow(N, P)
    return res

N = int(input('Informe um valor para N: '))
P = int(input('Informe um valor para P: '))

resultado_exponenciacao = expon(N, P)

print(f'O resultado de {N} elevado a {P} é igual a {resultado_exponenciacao}.')