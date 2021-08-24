def main():

    suma_calif = 0

    #escribe tu código abajo de esta línea
    for x in range(4):
        c = float(input("Calificación de la materia: "))
        suma_calif = c + suma_calif

    promedio = suma_calif/4

    print(f"El promedio es: {promedio}")
    
if __name__ == '__main__':
    main()
