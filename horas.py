base = int(input())
simbolos = input()
tempo = input()
segundos_por_simbolo = float(input())

tempo_convertido = 0
magnitude = len(tempo)
for simbolo in tempo:
    magnitude -= 1

    tempo_convertido += base ** magnitude * simbolos.index(simbolo) * segundos_por_simbolo

print(f"{tempo_convertido:.2f}")