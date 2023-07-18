# 7.	Faça um programa que receba 3 números e mostre, utilizando funções:

# -	Os números em ordem crescente
# -	Os números em ordem decrescente
# -	Os números pares
# -	Os números ímpares
# -	Os números maiores que 3 e menores que 10

def ordenar_crescente(numeros):
    return sorted(numeros)

def ordenar_descrescente(numeros):
    return sorted(numeros, reverse=True)

def mostrar_pares(numeros):
    return sorted([num for num in numeros if num % 2 == 0])

def mostrar_impares(numeros):
    return sorted([num for num in numeros if num % 2 != 0])

def mostrar_maiores_que_3_e_menores_que_10(numeros):
    return [num for num in numeros if 3 < num < 10]

numeros = []

for contador in range(1, 4):
    num = int(input(f'Digite o {contador}º número: '))
    numeros.append(num)

    ordem_crescente = ordenar_crescente(numeros)
    ordem_decrescente = ordenar_descrescente(numeros)
    pares = mostrar_pares(numeros)
    impares = mostrar_impares(numeros)
    maiores_que_3_e_menores_que_10 = mostrar_maiores_que_3_e_menores_que_10(numeros)


print(f'\nOrdem crescente: {ordem_crescente}')
print(f'Ordem decrescente: {ordem_decrescente}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {impares}')
print(f'Números maiores que 3 e menores que 10: {maiores_que_3_e_menores_que_10}')