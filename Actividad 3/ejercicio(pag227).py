# Módulo: tienda_mascotas.py

class Mascota:
    def __init__(self, nombre: str, edad: int, color: str):
        self.nombre = nombre
        self.edad = edad
        self.color = color


class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")


class PerroPequeno(Perro):
    RAZAS = ["caniche", "yorkshire terrier", "schnauzer", "chihuahua"]


class PerroMediano(Perro):
    RAZAS = ["collie", "dálmata", "bulldog", "galgo", "sabueso"]


class PerroGrande(Perro):
    RAZAS = ["pastor alemán", "doberman", "rotweiller"]


class Gato(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")


class GatoSinPelo(Gato):
    RAZAS = ["esfinge", "elfo", "donskoy"]


class GatoPeloLargo(Gato):
    RAZAS = ["angora", "himalayo", "balinés", "somalí"]


class GatoPeloCorto(Gato):
    RAZAS = ["azul ruso", "británico", "manx", "devon rex"]

def crear_perro():
    nombre = input("Nombre del perro: ")
    edad = int(input("Edad: "))
    color = input("Color: ")
    peso = float(input("Peso (kg): "))
    muerde = input("¿Muerde? (s/n): ").strip().lower() == "s"

    print("\nSeleccione el tipo de perro:")
    print("1. Pequeño")
    print("2. Mediano")
    print("3. Grande")
    tipo = input("Tipo: ")

    if tipo == "1":
        raza = input(f"Raza ({', '.join(PerroPequeno.RAZAS)}): ")
        perro = PerroPequeno(nombre, edad, color, peso, muerde)
    elif tipo == "2":
        raza = input(f"Raza ({', '.join(PerroMediano.RAZAS)}): ")
        perro = PerroMediano(nombre, edad, color, peso, muerde)
    else:
        raza = input(f"Raza ({', '.join(PerroGrande.RAZAS)}): ")
        perro = PerroGrande(nombre, edad, color, peso, muerde)

    print(f"\nResumen:")
    print(f"Nombre: {perro.nombre}, Edad: {perro.edad}, Color: {perro.color}")
    print(f"Peso: {perro.peso} kg, Muerde: {'Sí' if perro.muerde else 'No'}")
    print(f"Raza: {raza}")
    perro.sonido()


def crear_gato():
    nombre = input("Nombre del gato: ")
    edad = int(input("Edad: "))
    color = input("Color: ")
    altura = float(input("Altura de salto (cm): "))
    longitud = float(input("Longitud de salto (cm): "))

    print("\nSeleccione el tipo de gato:")
    print("1. Sin pelo")
    print("2. Pelo largo")
    print("3. Pelo corto")
    tipo = input("Tipo: ")

    if tipo == "1":
        raza = input(f"Raza ({', '.join(GatoSinPelo.RAZAS)}): ")
        gato = GatoSinPelo(nombre, edad, color, altura, longitud)
    elif tipo == "2":
        raza = input(f"Raza ({', '.join(GatoPeloLargo.RAZAS)}): ")
        gato = GatoPeloLargo(nombre, edad, color, altura, longitud)
    else:
        raza = input(f"Raza ({', '.join(GatoPeloCorto.RAZAS)}): ")
        gato = GatoPeloCorto(nombre, edad, color, altura, longitud)

    print(f"\nResumen:")
    print(f"Nombre: {gato.nombre}, Edad: {gato.edad}, Color: {gato.color}")
    print(f"Altura salto: {gato.altura_salto} cm, Longitud salto: {gato.longitud_salto} cm")
    print(f"Raza: {raza}")
    gato.sonido()


def main():
    print("Bienvenido a Tienda Mascotas")
    print("1. Ingresar Perro")
    print("2. Ingresar Gato")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_perro()
    elif opcion == "2":
        crear_gato()
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()