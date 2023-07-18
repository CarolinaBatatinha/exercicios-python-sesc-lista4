#6.	Crie uma tabela de conversão de polegada para centímetros. A tabela deve conter valores de 1 a 100 polegadas. Crie uma função para calcular o valor sabendo-se que cada polegada equivale a 2,54 cm.
def converte_polegada_em_centimetros(polegada):
    return polegada * 2.54

print(':.:.: TABELA DE CONVERSÃO (cm/ polegada) :.:.:')

for polegada in range(1, 101):
    cm = converte_polegada_em_centimetros(polegada)
    print(f'{polegada} polegadas\t=    {cm:.2f}cm')