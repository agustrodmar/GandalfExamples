# Ejercicio 1: Escribir un programa que pregunte el nombre del usuario en la consola y
# después que el usuario lo introduzca muestre por pantalla la cadena
# "Hola <nombre>".
def ejercicio1():
    nombre = input("¿Cómo te llamas?")

    print("Hola " + nombre)


# Ejercicio 2: Escribir un programa que muestre por pantalla el resultado de la siguiente
# operación aritmética
def ejercicio2():
    n1 = 3
    n2 = 2
    n3 = 2
    n4 = 5

    formula = (n1 + n2) / (n3 * n4)

    resultado = pow(formula, 2)

    print(resultado)


# Ejercicio 3: Escribir un programa que pregunte al usuario por el número de horas
# trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le
# corresponde."
def ejercicio3():
    horas_trabajadas = int(input("Cuantas horas has trabajado?"))
    coste_hora = int(input("¿A qué coste te las han pagado?"))
    resultado = (horas_trabajadas * coste_hora)

    print("Deben pagarte " + str(resultado) + " euros.")


# Ejercicio 4: Escribir un programa que lea un entero positivo, n, introducido por
# el usuario y después muestre por pantalla la suma de todos los enteros desde 1
# hasta n. La suma de los n primeros enteros positivos puede ser calculada de la
# siguiente forma: suma = n(n +1) / 2
def ejercicio4():
    numero = int(input("Introduce el número mágico: "))

    suma = numero * (numero + 1) / 2

    print(" La suma de 1 al número mágico es de " + str(suma))


# Ejercicio 5: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por
# pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice
# de masa corporal calculado redondeado con dos decimales.
def ejercicio5():
    peso = float((input("Introduce tu peso: ")))
    altura = float((input("Introduce tu altura: ")))
    calculo_imc = round(peso / pow(altura, 2), 2) # El segundo 2, representa el número de decimales

    print(calculo_imc)


def main(ejercio=ejercicio5()):
    return ejercio
