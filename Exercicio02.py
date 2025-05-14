def maior_n():
    numeros = input("Digite os números: ")
    lista = [float(num) for num in numeros.split()]

    maior = max(lista)
    print(f"O maior número digitado foi: {maior}")