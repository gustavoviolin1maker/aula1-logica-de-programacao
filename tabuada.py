while True:
    tabuada = int(input("Digite a tabuada de sua preferencia (0 para sair): "))
    if tabuada == 0:
        print("Saindo...")
        break
    minimo = int(input("Digite o valor minimo a ser calculado: "))
    maximo = int(input("Digite o valor maximo a ser calculado: "))
    i = minimo
    while i <= maximo:
        print(f"{tabuada} x {i} = {tabuada * i}")
        i += 1