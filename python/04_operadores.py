#operadores
"""
operadores aritméticos
+ suma
- resta
* multiplicación
/ división
// división entera
% módulo
** potencia
"""
valor1 = 10
valor2 = 3
print("Suma:", valor1 + valor2)
print("Resta:", valor1 - valor2)
print("Multiplicación:", valor1 * valor2)
print("División:", valor1 / valor2)
print("División entera:", valor1 // valor2)
print("Módulo:", valor1 % valor2)
print("Potencia:", valor1 ** valor2)

print("tabla de multiplicar del 5:")
multiplicador = 5
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3)
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)

print("area de un triangulo con base 5 y altura 10:", (5 * 10) / 2)

#operadores de comparación
"""
== (igual)
!= (diferente)
> (mayor que)
< (menor que)
>= (mayor o igual que)
<= (menor o igual que)
"""

velocidad_anakin = 900
velocidad_sebulba = 950
print("¿La velocidad de Anakin es igual a la de Sebulba?", velocidad_anakin == velocidad_sebulba)
print("¿La velocidad de Anakin es diferente a la de Sebulba?", velocidad_anakin != velocidad_sebulba)
print("¿La velocidad de Anakin es mayor que la de Sebulba?", velocidad_anakin > velocidad_sebulba)
print("¿La velocidad de Anakin es menor que la de Sebulba?", velocidad_anakin < velocidad_sebulba)
print("¿La velocidad de Anakin es mayor o igual que la de Sebulba?", velocidad_anakin >= velocidad_sebulba)
print("¿La velocidad de Anakin es menor o igual que la de Sebulba?", velocidad_anakin <= velocidad_sebulba)

#operadores lógicos
"""
and (y)
or (o)
not (no)
"""
motores_funcionando = True
escudos_activados = False
combustible = 80

print("todos los sistemas están operativos?", motores_funcionando and escudos_activados)
print("al menos un sistema está operativo?", motores_funcionando or escudos_activados)
print("¿los motores no están funcionando?", not motores_funcionando)

cantidad_motores = 2
cantidad_alas = 4
combustible = 100

print("¿la nave tiene al menos 2 motores y 4 alas?") 
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)
print("¿la nave tiene al menos 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4 and combustible >= 50)
print("¿la nave no tiene al menos 2 motores?")
print(not cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)

#operadores de asignación
"""
= asignación
+= suma y asigna
-= resta y asigna
*= multiplica y asigna
/= divide y asigna
//= divide entera y asigna
%= módulo y asigna
**= potencia y asigna
"""
velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de += 50:", velocidad)
velocidad -= 30
print("Velocidad después de -= 30:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de *= 2:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de /= 4:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de %= 7:", velocidad)
velocidad //= 2
print("Velocidad después de //= 2:", velocidad)
velocidad **= 2
print("Velocidad después de **= 2:", velocidad)

#precedencia de operadores
"""
1. ()
2. ** (potencia)
3. *, /, //, % (multiplicación, división, división entera, módulo)
4. +, - (suma, resta)
5. <, <=, >, >= (comparación)
6. ==, != (comparación de igualdad y desigualdad)
7. not 
8. and
9. or
"""

resultado = 10 + 5 * 2
print("resultado: ", resultado)
resultado_2 = (10 + 5) * 2
print("resultado_2: ", resultado_2)
resultado_3 = 10 + 5 * 2 ** 2
print("resultado_3: ", resultado_3)
