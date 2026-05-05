nome = str(input("Informe seu nome:"))
salario = float(input("Informe seu salário:"))
reajuste = float(input("Digite o percentual de reajuste: "))

calculo = salario+(salario*reajuste/100)

print("Olá ",nome,"Seu salário reajustado é :" ,calculo,)

