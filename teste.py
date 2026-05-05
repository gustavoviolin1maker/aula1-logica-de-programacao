import math

while True:
    valor = int(input("Digite O número: (digite zero para sair) "))
    if valor == 0:
        break
    resultado = math.prod(range(1, valor + 1))
    print("O fatorial desse numero é:", resultado)  
