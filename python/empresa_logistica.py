peso = int(input("Saludos, ingresa el peso de el paquete en kilogramos: "))
destino = int(input("Eliga la zona de destino (1, 2 o 3): "))
if destino == 1:
    precio = peso * 5
    print ("El precio del envio es: ", precio,"$")
elif destino == 2:
    precio_2 = peso * 7.5
    print ("El precio del envio es: ", precio_2,"$")
elif destino == 3:
    precio_3 = peso * 10
    print ("El precio del envio es: ", precio_3,"$")
else: 
    print ("La zona de destino es incorrecta vuelva a intentarlo")
