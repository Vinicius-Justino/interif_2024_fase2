excesso = int(input())

precos = []
precos_existentes = {}
for i in range(int(input())):
    preco_produto = int(input())
    
    precos.append(preco_produto)
    precos_existentes[preco_produto] = "existe"

for preco in precos:
    try:
        if precos_existentes[excesso - preco] == "existe":
            produtos_removidos = sorted([precos.index(preco), precos.index(excesso - preco)])
            print(f"{min(produtos_removidos)} {max(produtos_removidos)}")
            break
    except KeyError:
        continue