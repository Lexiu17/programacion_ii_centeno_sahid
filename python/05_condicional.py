#condicional if
#simple

combustible = 5
if combustible >= 10:
    print("Puedes despegar")

#condicional if-else
creditos = int(input("Ingresa la cantidad de creditos: "))
precio_repuesto = int(input("Ingresa el precio del repuesto: "))
if creditos >= precio_repuesto:
    print("puedes comprar el repuesto")
else:
    print("no puedes comprar el repuesto")

#if anidado
if creditos >= precio_repuesto:
    print("puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("te sobraran creditos")
    else:
        print("no te sobraran creditos")
else:
    print("no tienes creditos suficientes para comprar el repuesto")

#condicional if-elif-else
if creditos >= precio_repuesto:
    print("puedes comprar el repuesto")
elif creditos == precio_repuesto:
    print("puedes comprar el repuesto pero no te sobraran creditos")
else:
    print("no tienes creditos suficientes para comprar el repuesto")

tipo_repuesto = input("Ingresa el tipo de repuesto (motor, ala, escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuesto and tipo_repuesto == "ala":
    print("puedes comprar el repuesto y te sobraran creditos")
elif tipo_repuesto == "ala" and creditos >= precio_repuesto:
    print("puedes comprar el repuesto y te sobraran creditos")
elif tipo_repuesto == "escudo" and creditos >= precio_repuesto:
    print("puedes comprar el repuesto y te sobraran creditos")
else:
    print("no tienes creditos suficientes para comprar el repuesto")