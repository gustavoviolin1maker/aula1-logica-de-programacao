Nmin = int(input("Entre com o valor inicial da sequencia: "))
Nmax = int(input("Entre com o valor final da sequencia"))
for i in range(Nmin, Nmax+1):
    resto = i%2
    if resto == 0:
        print(i," - Par")
    else:
        print(i," - Impar")
    print("Obrigado por usar o sistema")    