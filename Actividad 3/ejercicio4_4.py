class Profesor:
    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Es un profesor titular.")

def main():
    # Polimorfismo: referencia tipo Profesor, objeto real tipo ProfesorTitular
    profesor1: Profesor = ProfesorTitular()
    profesor1.imprimir()  # Se debe imprimir: "Es un profesor titular."

if __name__ == "__main__":
    main()
