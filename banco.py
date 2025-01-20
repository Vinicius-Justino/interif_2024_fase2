quantidade_operacoes, tamanho_amostra = [int(n) for n in input().split()]
operacoes = [int(n) for n in input().split()]

avisos = 0
for i in range(quantidade_operacoes - tamanho_amostra):
    mediana_amostra = sorted(operacoes[i : i + tamanho_amostra])[tamanho_amostra // 2]
    
    if operacoes[i + tamanho_amostra] >= mediana_amostra * 2:
        avisos += 1

print(avisos)