limite = int(input())
multa = int(input())
adicional = int(input())
velocidade = int(input())

if velocidade <= limite:
    print(0)
else:
    print(multa + adicional * (velocidade - limite))