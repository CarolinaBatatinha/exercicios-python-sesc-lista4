# 9.	Os salários dos empregados de uma empresa sofreram um aumento. Técnicos tiveram um aumento de 50%, gerentes de 30% e os demais de 10%. Faça um programa que calcule o salário reajustado para cada profissão.

def calcular_salario_reajustado(salario):
    if cargo == 1:
        print('\nCargo: Técnico')
        return salario * 1.5
    elif cargo == 2:
        print('\nCargo: Gerente')
        return salario * 1.3
    else:
        return salario * 1.1

cargo = int(input('Informe seu cargo:\n[1] - Técnico\n[2] - Gerente\n[3] - Demais cargos\n '))
salario = float(input('Informe seu salário em R$: '))

if 1 < cargo > 3:
    print('Número inválido. Programa encerrado.')
else:
    salario_reajustado = calcular_salario_reajustado(salario)

print(f'Salário reajustado: R$ {salario_reajustado:.2f}')

