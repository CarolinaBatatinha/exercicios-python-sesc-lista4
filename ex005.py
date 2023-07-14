#5.	Faça um programa que receba o valor a ser depositado pelo usuário e a taxa de juros, crie uma função para calcular o rendimento e utilize-a para mostrar quanto o usuário terá depois da aplicação dos juros.

def calcula_rendimento (valor_depositado, taxa_juros):
    rendimento = valor_depositado * (taxa_juros/100)
    valor_final = valor_depositado + rendimento
    return valor_final

valor_depositado = float(input("Informe o valor a ser depositado em R$: "))
taxa_juros = float(input("Informe a taxa de juros em %: "))

valor_final = calcula_rendimento(valor_depositado,taxa_juros)

print(f'Sua aplicação de R$ {valor_depositado:.2f} rendeu R$ {valor_final:.2f} na sua conta.')