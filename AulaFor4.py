numeroInic = int(input(" digite o numero inicil: "))
numeroFinal = int(input(" digite o numero final: "))
NumeroDivi = int(input(" digite o numero divisor: "))

for i in range(numeroInic, numeroFinal + 1):
    if i % NumeroDivi == 0:
        print(i)
        
        