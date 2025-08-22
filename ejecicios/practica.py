
#pedir edad y verificar si es niño, hasta 12 años. Adolecente, 12 a 17 años o adulto


#imprimir una tabla de multiplicar

#Leer una palabra y contar cuantas vocales tiene usando el FOR

#Pedir un número n y calcular la suma de 1 hasta n en un bucle
opcion = int(input("Ingrese una opción válida\n" \
"1. Imprimir: pedir edad y verificar si es niño, hasta 12 años. Adolecente, 12 a 17 años o adulto\n" \
"2. Imprimir: una tabla de multiplicar "))
def switch_case(opcion):
    if opcion == 1:
        edad = int(input("Ingrese una edad: "))
        if edad <= 12:
            print("Por la edad es un niño")
        elif edad >= 13:
            print("Por la edad es mayor de edad")
        return
    elif opcion == 2:
        print("Tabla de multiplicar:")
        numero = int(input("Ingrese el número al que quiere validar su tabla de multiplicar"))
        multiplo = 0
        while multiplo <= 10:
            print(numero, " x ", multiplo, " = ", numero*multiplo)
            multiplo+=1
        return
    elif opcion == 3:
        palabra = input("Ingrese una palabra para identificar cuantas vocales tiene: ")
        vocales ="aeiouAEIOU"
        contador = 1
        for letra in palabra:
            if letra in vocales:
                contador+=1
        print(f"La palabra'{palabra}' tiene '{contador}' vocales.")
        return "Opción 3 seleccionada"
    else:
        return "Opción no válida"