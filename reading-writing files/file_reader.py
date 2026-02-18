def cuadrado(numero):
    return numero ** 2

def cubo(numero):
    return numero ** 3

def main():
    numero = int(input("Ingrese un número: "))
    
    archivo = open("texto.txt", "r+", encoding="utf-8")
    with archivo as f:
        for i in range(numero + 1):
            f.write(f"{i} al cuadrado es {cuadrado(i)}\n")
        f.write("\n")  # Agrega una línea en blanco entre los cálculos

        for i in range(numero + 1):
            f.write(f"{i} al cubo es {cubo(i)}\n")
        f.write("Fin de los cálculos.\n")

        f.seek(0)  # Volver al inicio del archivo para leer su contenido
        print(f.read())  # Imprime el contenido del archivo

if __name__ == "__main__":
    main()