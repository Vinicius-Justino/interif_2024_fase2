alunos, orcamento, preco_barra = [float(n) for n in input().split()]

if 0 in [alunos, preco_barra]:
    print(int(alunos))
else:
    print(int((orcamento / preco_barra) // alunos))