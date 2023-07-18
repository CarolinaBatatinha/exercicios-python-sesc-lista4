# 8.	Escreva um programa para calcular o reajuste salarial dos empregados de uma empresa, de acordo com os seguintes critérios:
# a.	Os funcionários com salário inferior a 1.000,00 devem ter um reajuste de 55%;
# b.	Funcionários com salário de 1.000,00 (inclusive) a 2.500,00 (inclusive) devem ter um reajuste de 33%;
# c.	Os funcionários com salário superior a 2.500,00 devem ter um reajuste de 20%;
# Crie uma função que receba o salário do funcionário e mostre o valor do reajuste.

def calcular_reajuste(salario):
    if salario < 1000:
        return salario * .55
    
    elif 1000 >= salario < 2500:
        return salario * .33
    else:
        return salario * .2

salario = float(input('Informe seu salário: '))
reajuste = calcular_reajuste(salario)

print(f'\nSalário antigo: R$ {salario:.2f}')
print(f'Reajuste: R$ {reajuste:.2f}')

