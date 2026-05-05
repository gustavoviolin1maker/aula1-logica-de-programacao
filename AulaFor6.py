import random

for i in range(100):
    numero = random.randint(0, 10)
    print("O primeiro número da soma é:", numero)
    numero2 = random.randint(0, 10)
    print("O segundo número da soma é:", numero2)
    print("Qual a soma dos dois números? (Digite zero para sair)")
    resposta = int(input("Digite a resposta: "))
    if resposta == 0:
        break
    soma = numero + numero2
    if resposta == soma:
        print("==================================")
        print("Parabéns! Você acertou.")
        print("==================================")
    else:
        print("==================================")
        print("Que pena! Você errou.")
        print("A soma dos números é:", soma)
        print("==================================")
        
