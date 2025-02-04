quantidade_depositos = int(input())

depositos = [bin(int(deposito))[2:] for deposito in input().split(" ")]
magnitude_chave = max([len(deposito) for deposito in depositos])
depositos = ["0" * (magnitude_chave - len(deposito)) + deposito for deposito in depositos]

expressao = ""
resultado_chave = 0
for magnitude_atual in range(magnitude_chave, 0, -1):
    algarismo = sum([int(deposito[magnitude_chave - magnitude_atual]) for deposito in depositos])
    if algarismo == 0:
        continue

    expressao += f"{algarismo}*2^{magnitude_atual - 1}+"
    resultado_chave += algarismo * 2 ** (magnitude_atual - 1)

print(f"saida: {expressao[:len(expressao) - 1]}={resultado_chave}")