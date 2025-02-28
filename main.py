def solicitar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un número válido.")

n1 = solicitar_numero("Primer número: ")
n2 = solicitar_numero("Segundo número: ")

print("Suma: ", (n1+n2))
print("Resta: ", (n1-n2))
print("Multiplicacion: ", (n1*n2))
print("Division: ", (n1/n2))