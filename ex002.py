#2.	Faça um algoritmo que receba um número correspondente a uma das tabuadas (somente números entre 1 e 10), crie uma função que receba o número digitado e imprima a tabuada do respectivo número. O programa termina quando o usuário digitar um valor inválido.

def calcula_tabuada(num):
    for i in range(1, 11):
        res = num * i
        print(f'{num} x {i} = {res}')

while True:
    try: 
        num = int(input('Digite um número de 1 a 10: '))
        if num < 1 or num > 10:
            break
        calcula_tabuada(num)

    except ValueError:
        print('Digite um número válido.')


