# 10.	Elaborar um programa utilizando funções que calcule a média ponderada de um aluno da disciplina de Algoritmo. Esta média tem pesos: 4 para a primeira prova e 3 para a segunda prova. Após calculada a média, uma mensagem deve ser apresentada informando a situação do aluno: APROVADO COM MÉDIA ou NECESSITA FAZER SUBSTITUTIVA. Caso o aluno necessite fazer prova substitutiva, o programa deve pedir esta nota e calcular a nova média do aluno. Uma nova mensagem da situação deve informar ALUNO COM MÉDIA ou ALUNO REPROVADO. Obs: A prova substitutiva pode substituir a primeira prova ou a segunda prova, portanto o programa deve verificar quando o aluno fica com maior média, isto é, quando a primeira prova é substituída pela prova substitutiva ou quando a segunda prova é substituída pela prova substitutiva.

def calcular_media_ponderada(prova1, prova2):
    return (prova1 * 4 + prova2 * 3) / 7

def verificar_situacao_aluno(media):
    if media >= 7:
        return "APROVADO COM MÉDIA"
    else:
        return "NECESSITA FAZER SUBSTITUTIVA"

# Entrada das notas das provas
prova1 = float(input("Informe a nota da primeira prova: "))
prova2 = float(input("Informe a nota da segunda prova: "))

media_aluno = calcular_media_ponderada(prova1, prova2)
situacao_aluno = verificar_situacao_aluno(media_aluno)

print("Situação do aluno:", situacao_aluno)

# Verificar se é necessário fazer prova substitutiva
if situacao_aluno == "NECESSITA FAZER SUBSTITUTIVA":
    substitutiva = float(input("Informe a nota da prova substitutiva: "))
    
    # Calcular nova média substituindo a primeira prova
    nova_media1 = calcular_media_ponderada(substitutiva, prova2)
    
    # Calcular nova média substituindo a segunda prova
    nova_media2 = calcular_media_ponderada(prova1, substitutiva)
    
    if nova_media1 > media_aluno and nova_media1 >= nova_media2:
        situacao_aluno = "ALUNO COM MÉDIA"
    elif nova_media2 > media_aluno:
        situacao_aluno = "ALUNO COM MÉDIA"
    else:
        situacao_aluno = "ALUNO REPROVADO"
    
    print("Nova situação do aluno:", situacao_aluno)
