class Cuenta:
    def __init__(self, saldo: float, tasa_anual: float):
        self.saldo = saldo
        self.numero_consignaciones = 0
        self.numero_retiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0

    def consignar(self, cantidad: float):
        self.saldo += cantidad
        self.numero_consignaciones += 1

    def retirar(self, cantidad: float):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            self.numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        tasa_mensual = self.tasa_anual / 12 / 100
        interes_mensual = self.saldo * tasa_mensual
        self.saldo += interes_mensual

    def extracto_mensual(self):
        self.saldo -= self.comision_mensual
        self.calcular_interes()

    def imprimir(self):
        print(f"Saldo: ${self.saldo:.2f}")
        print(f"Comisión mensual: ${self.comision_mensual:.2f}")


class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self.activa = saldo >= 10000

    def consignar(self, cantidad: float):
        if self.activa:
            super().consignar(cantidad)
        else:
            print("La cuenta está inactiva, no se puede consignar.")

    def retirar(self, cantidad: float):
        if self.activa:
            super().retirar(cantidad)
        else:
            print("La cuenta está inactiva, no se puede retirar.")

    def extracto_mensual(self):
        if self.numero_retiros > 4:
            self.comision_mensual += (self.numero_retiros - 4) * 1000
        super().extracto_mensual()
        self.activa = self.saldo >= 10000

    def imprimir(self):
        super().imprimir()
        print(f"Numero de transacciones: {self.numero_consignaciones + self.numero_retiros}")


class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self.sobregiro = 0

    def retirar(self, cantidad: float):
        if cantidad > self.saldo:
            self.sobregiro += cantidad - self.saldo
            self.saldo = 0
            self.numero_retiros += 1
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self.sobregiro > 0:
            if cantidad >= self.sobregiro:
                cantidad -= self.sobregiro
                self.sobregiro = 0
            else:
                self.sobregiro -= cantidad
                cantidad = 0
        super().consignar(cantidad)

    def imprimir(self):
        print("Cuenta Corriente")
        super().imprimir()
        print(f"Sobregiro: ${self.sobregiro:.2f}")
        print(f"Numero de transacciones: {self.numero_consignaciones + self.numero_retiros}")


# Ejemplo de uso:
def main():
    saldo_inicial = float(input("Ingrese saldo inicial: $"))
    tasa_anual = float(input("Ingrese tasa de interes (%): "))

    cuenta_ahorros = CuentaAhorros(saldo_inicial, tasa_anual)

    cantidad_consignar = float(input("Cantidad a consignar: $"))
    cuenta_ahorros.consignar(cantidad_consignar)

    cantidad_retirar = float(input("Cantidad a retirar: $"))
    cuenta_ahorros.retirar(cantidad_retirar)

    cuenta_ahorros.extracto_mensual()
    cuenta_ahorros.imprimir()


if __name__ == "__main__":
    main()
