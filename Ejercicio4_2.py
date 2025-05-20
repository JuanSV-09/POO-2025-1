class Inmueble:
    def __init__(self, identificador: int, area: int, direccion: str):
        self.identificador = identificador
        self.area = area
        self.direccion = direccion
        self.precio_venta = 0

    def calcular_precio_venta(self, valor_area: float):
        self.precio_venta = self.area * valor_area
        return self.precio_venta

    def imprimir(self):
        print(f"Identificador: {self.identificador}")
        print(f"Área: {self.area} m²")
        print(f"Dirección: {self.direccion}")
        print(f"Precio de venta: ${self.precio_venta:,.0f}")


class InmuebleVivienda(Inmueble):
    def __init__(self, identificador, area, direccion, habitaciones, banos):
        super().__init__(identificador, area, direccion)
        self.habitaciones = habitaciones
        self.banos = banos

    def imprimir(self):
        super().imprimir()
        print(f"Habitaciones: {self.habitaciones}")
        print(f"Baños: {self.banos}")


class Casa(InmuebleVivienda):
    def __init__(self, identificador, area, direccion, habitaciones, banos, pisos):
        super().__init__(identificador, area, direccion, habitaciones, banos)
        self.pisos = pisos

    def imprimir(self):
        super().imprimir()
        print(f"Pisos: {self.pisos}")


class Apartamento(InmuebleVivienda):
    def __init__(self, identificador, area, direccion, habitaciones, banos):
        super().__init__(identificador, area, direccion, habitaciones, banos)


class CasaRural(Casa):
    VALOR_AREA = 1500000

    def __init__(self, identificador, area, direccion, habitaciones, banos, pisos, distancia, altitud):
        super().__init__(identificador, area, direccion, habitaciones, banos, pisos)
        self.distancia = distancia
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal: {self.distancia} km")
        print(f"Altitud: {self.altitud} msnm")


class CasaUrbana(Casa):
    def __init__(self, identificador, area, direccion, habitaciones, banos, pisos):
        super().__init__(identificador, area, direccion, habitaciones, banos, pisos)


class CasaConjuntoCerrado(CasaUrbana):
    VALOR_AREA = 2500000

    def __init__(self, identificador, area, direccion, habitaciones, banos, pisos, administracion, piscina, deportivos):
        super().__init__(identificador, area, direccion, habitaciones, banos, pisos)
        self.administracion = administracion
        self.piscina = piscina
        self.deportivos = deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Administración: ${self.administracion:,.0f}")
        print(f"Piscina: {'Sí' if self.piscina else 'No'}")
        print(f"Campos deportivos: {'Sí' if self.deportivos else 'No'}")


class CasaIndependiente(CasaUrbana):
    VALOR_AREA = 3000000


class ApartamentoFamiliar(Apartamento):
    VALOR_AREA = 2000000

    def __init__(self, identificador, area, direccion, habitaciones, banos, administracion):
        super().__init__(identificador, area, direccion, habitaciones, banos)
        self.administracion = administracion

    def imprimir(self):
        super().imprimir()
        print(f"Administración: ${self.administracion:,.0f}")


class Apartaestudio(Apartamento):
    VALOR_AREA = 1500000

    def __init__(self, identificador, area, direccion):
        super().__init__(identificador, area, direccion, 1, 1)


class Local(Inmueble):
    def __init__(self, identificador, area, direccion, tipo_local):
        super().__init__(identificador, area, direccion)
        self.tipo_local = tipo_local  # "INTERNO" o "CALLE"

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local: {self.tipo_local}")


class LocalComercial(Local):
    VALOR_AREA = 3000000

    def __init__(self, identificador, area, direccion, tipo_local, centro_comercial):
        super().__init__(identificador, area, direccion, tipo_local)
        self.centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial: {self.centro_comercial}")


class Oficina(Local):
    VALOR_AREA = 3500000

    def __init__(self, identificador, area, direccion, tipo_local, es_gobierno):
        super().__init__(identificador, area, direccion, tipo_local)
        self.es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"¿Es gubernamental?: {'Sí' if self.es_gobierno else 'No'}")

def main():
    print("Seleccione el tipo de inmueble:")
    print("1. Apartamento Familiar")
    print("2. Apartaestudio")
    print("3. Casa en Conjunto Cerrado")
    print("4. Casa Rural")
    print("5. Local Comercial")
    print("6. Oficina")
    opcion = input("Ingrese una opción (1-6): ")

    if opcion == "1":
        id = int(input("Identificador: "))
        area = int(input("Área (m²): "))
        direccion = input("Dirección: ")
        habitaciones = int(input("Habitaciones: "))
        banos = int(input("Baños: "))
        administracion = int(input("Valor administración: "))
        inmueble = ApartamentoFamiliar(id, area, direccion, habitaciones, banos, administracion)
        inmueble.calcular_precio_venta(ApartamentoFamiliar.VALOR_AREA)

    elif opcion == "2":
        id = int(input("Identificador: "))
        area = int(input("Área (m²): "))
        direccion = input("Dirección: ")
        inmueble = Apartaestudio(id, area, direccion)
        inmueble.calcular_precio_venta(Apartaestudio.VALOR_AREA)

    elif opcion == "3":
        id = int(input("Identificador: "))
        area = int(input("Área (m²): "))
        direccion = input("Dirección: ")
        habitaciones = int(input("Habitaciones: "))
        banos = int(input("Baños: "))
        pisos = int(input("Pisos: "))
        administracion = int(input("Valor administración: "))
        piscina = input("¿Tiene piscina? (s/n): ").lower() == "s"
        deportivos = input("¿Tiene campos deportivos? (s/n): ").lower() == "s"
        inmueble = CasaConjuntoCerrado(id, area, direccion, habitaciones, banos, pisos, administracion, piscina, deportivos)
        inmueble.calcular_precio_venta(CasaConjuntoCerrado.VALOR_AREA)

    elif opcion == "4":
        id = int(input("Identificador: "))
        area = int(input("Área (m²): "))
        direccion = input("Dirección: ")
        habitaciones = int(input("Habitaciones: "))
        banos = int(input("Baños: "))
        pisos = int(input("Pisos: "))
        distancia = int(input("Distancia a cabecera municipal (km): "))
        altitud = int(input("Altitud (msnm): "))
        inmueble = CasaRural(id, area, direccion, habitaciones, banos, pisos, distancia, altitud)
        inmueble.calcular_precio_venta(CasaRural.VALOR_AREA)

    elif opcion == "5":
        id = int(input("Identificador: "))
        area = int(input("Área (m²): "))
        direccion = input("Dirección: ")
        tipo_local = input("Tipo de local (INTERNO/CALLE): ")
        centro_comercial = input("Nombre del centro comercial: ")
        inmueble = LocalComercial(id, area, direccion, tipo_local, centro_comercial)
        inmueble.calcular_precio_venta(LocalComercial.VALOR_AREA)

    elif opcion == "6":
        id = int(input("Identificador: "))
        area = int(input("Área (m²): "))
        direccion = input("Dirección: ")
        tipo_local = input("Tipo de local (INTERNO/CALLE): ")
        es_gobierno = input("¿Es gubernamental? (s/n): ").lower() == "s"
        inmueble = Oficina(id, area, direccion, tipo_local, es_gobierno)
        inmueble.calcular_precio_venta(Oficina.VALOR_AREA)

    else:
        print("Opción inválida.")
        return

    print("\n--- Información del inmueble ---")
    inmueble.imprimir()

if __name__ == "__main__":
    main()