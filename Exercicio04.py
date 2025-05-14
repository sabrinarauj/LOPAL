def calcular_troco(valor_compra, valor_pago):
    valor_troco = valor_pago - valor_compra
    if valor_pago < valor_compra:
        return 0
    return valor_troco

valor_compra = float(input("Digite o valor total da compra: "))
valor_pago = float(input("Digite o valor pago: "))

resultado = calcular_troco(valor_compra, valor_pago)
print(f"O valor do troco a ser dado é de: R${resultado:.2f}")