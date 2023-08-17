# 1.	Faça um programa que receba 5 números do tipo float maiores que zero, crie as seguintes funções:
# -	boolean verificaNumero(int float)
# -	void parImpar(int float)
# -	float media(float n1, float n2, float n3, float n4, float n5)
# -	float maior(float n1, float n2, float n3, float n4, float n5)
# -	float menor(float n1, float n2, float n3, float n4, float n5)
# Ao solicitar cada número, verifique se o mesmo é valido através da função verificaNumero, depois mostre se o número é par ou impar utilizando a função parImpar. Ao final mostre a média dos números, qual é o número maior e qual é o número menor.

def verifica_numero(num):
    if num > 0 and isinstance(num, float): 
        return True
    else: 
        return False
    
def par_impar(num):
    if num % 2 == 0:
        print(f'\n{num} é par')
    else:
        print(f'\n{num} é ímpar')

def calcula_media(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5

def menor_valor(n1, n2, n3, n4, n5):
    return min(n1, n2, n3, n4, n5)

def maior_valor(n1, n2, n3, n4, n5):
    return max(n1, n2, n3,n4, n5)

numeros = []

for i in range(1, 6):
    while True:
        try: 
            num = float(input(f'Digite o {i}º número: '))
            if verifica_numero(num):
                numeros.append(num)
                break
            else:
                print('Valor inválido. Digite novamente.')
        except ValueError:
            print('Entrada inválido. Digite novamente.')


for num in numeros:
    par_impar(num)

media = calcula_media(* numeros)
menorNum = menor_valor(* numeros)
maiorNum = maior_valor(* numeros)

print(f'''
====== RESULTADOS ======
    Média: {media}
    Menor número: {menorNum}
    Maior número: {maiorNum}
''')
