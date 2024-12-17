# Paso 1: Solicitar al usuario que ingrese la edad del cliente.
edad=int(input("Por favor indique la edad del cliente: "))

# Paso 2: Verificar si la edad cumple con los requisitos para ingresar

permitido=True if edad>=18 else False #ternario, es decir, poner en una misma linea el codigo

# Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca

if permitido:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("¡Lo sentimos! No puedes ingresar")