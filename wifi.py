quantidade_antenas, alcance_antenas = [int(n) for n in input().split(" ")]
lotes_ocupados = [int(n) - 1 for n in input().split(" ")]

casas = {}
for casa in lotes_ocupados:
    for lote in range(casa - alcance_antenas, casa + alcance_antenas + 1):
        if lote not in lotes_ocupados:
            continue

        try:
            casas[lote] += 1
        except KeyError:
            casas[lote] = 1

for casa in lotes_ocupados:
    cobertura = {}
    for lote in range(casa - alcance_antenas, casa + alcance_antenas + 1):
        if lote not in lotes_ocupados:
            continue
        
        cobertura[lote] = casas[lote]
    
    if 1 not in cobertura.values():
        quantidade_antenas -= 1

        for casa in cobertura.keys():
            casas[casa] -= 1

print(quantidade_antenas)