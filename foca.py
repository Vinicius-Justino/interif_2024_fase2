iteracoes = int(input())

pessoas = []
seguidores = {}
seguidos = {}
pagerank_atual = {}
for nome in input().split(" "):
    pessoas.append(nome)
    seguidores[nome] = []
    seguidos[nome] = 0
    pagerank_atual[nome] = 1

for pessoa in pessoas:
    relacoes = input().split(" ")
    for j in range(len(relacoes)):
        if relacoes[j] == "0":
            continue

        seguidores[pessoas[j]].append(pessoa)
        seguidos[pessoa] += 1

for i in range(iteracoes):
    prox_pagerank = {}

    for pessoa in pessoas:
        pagerank = 0

        for seguidor in seguidores[pessoa]:
            pagerank += pagerank_atual[seguidor] / seguidos[seguidor]
        
        prox_pagerank[pessoa] = pagerank

    pagerank_atual = prox_pagerank.copy()

pageranks_organizados = {}
for pessoa in pessoas:
    try:
        pageranks_organizados[pagerank_atual[pessoa]].append(pessoa)
    except KeyError:
        pageranks_organizados[pagerank_atual[pessoa]] = [pessoa]

for pagerank in reversed(sorted(pageranks_organizados.keys())):
    for pessoa in pageranks_organizados[pagerank]:
        print(f"{pessoa}: {pagerank_atual[pessoa]:.6f}")