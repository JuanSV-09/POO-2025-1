# Módulo: universidad.py

class Persona:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion

    def get_nombre(self) -> str:
        return self.nombre

    def get_direccion(self) -> str:
        return self.direccion

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def set_direccion(self, direccion: str):
        self.direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    def get_carrera(self) -> str:
        return self.carrera

    def get_semestre(self) -> int:
        return self.semestre

    def set_carrera(self, carrera: str):
        self.carrera = carrera

    def set_semestre(self, semestre: int):
        self.semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def get_departamento(self) -> str:
        return self.departamento

    def get_categoria(self) -> str:
        return self.categoria

    def set_departamento(self, departamento: str):
        self.departamento = departamento

    def set_categoria(self, categoria: str):
        self.categoria = categoria

def main():
    print("--- Crear Estudiante ---")
    nombre_est = input("Nombre del estudiante: ")
    direccion_est = input("Dirección del estudiante: ")
    carrera = input("Carrera: ")
    semestre = int(input("Semestre: "))

    estudiante = Estudiante(nombre_est, direccion_est, carrera, semestre)

    print("\nDatos del estudiante:")
    print(f"Nombre: {estudiante.get_nombre()}")
    print(f"Dirección: {estudiante.get_direccion()}")
    print(f"Carrera: {estudiante.get_carrera()}")
    print(f"Semestre: {estudiante.get_semestre()}")

    print("\n--- Crear Profesor ---")
    nombre_prof = input("Nombre del profesor: ")
    direccion_prof = input("Dirección del profesor: ")
    departamento = input("Departamento: ")
    categoria = input("Categoría: ")

    profesor = Profesor(nombre_prof, direccion_prof, departamento, categoria)

    print("\nDatos del profesor:")
    print(f"Nombre: {profesor.get_nombre()}")
    print(f"Dirección: {profesor.get_direccion()}")
    print(f"Departamento: {profesor.get_departamento()}")
    print(f"Categoría: {profesor.get_categoria()}")

if __name__ == "__main__":
    main()