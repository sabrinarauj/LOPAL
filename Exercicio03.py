def converter_celsius_para_fahrenheit(c):
    f = c * (1.8 + 32)
    return f

c = float(input("Digite uma temperatura em °C: "))
resultado = converter_celsius_para_fahrenheit(c)

print(f"A temperatura em Fahrenheit é de: {resultado:.1f}")