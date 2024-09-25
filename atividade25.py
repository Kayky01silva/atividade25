# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).

aprovados = 0

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    
    if nota >= 7:
        aprovados += 1


# Exibe o resultado
print(f"Total de alunos aprovados: {aprovados}")
