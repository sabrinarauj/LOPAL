def calcular_imc():
    kg = 1
    altura = 1
    imc = kg / altura ** 2
    return imc

imc = 1
kg = float(input("Digite seu peso corporal: "))
altura = float(input("Digite sua altura: "))

resultado_imc = calcular_imc(imc)
print("Seu IMC atual é de: ",resultado_imc)