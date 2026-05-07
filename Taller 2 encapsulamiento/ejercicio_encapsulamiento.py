class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        # Atributos privados (definidos por convención con guion bajo)
        self._titular = str(titular)
        
        # Validamos el saldo inicial para que coincida con la lógica del setter
        if saldo_inicial < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(saldo_inicial)

    # propiedad titular (Solo lectura)
    @property
    def titular(self):
        """Getter: Retorna el nombre del titular."""
        return self._titular
    
    # Nota: Al no definir un @titular.setter, el atributo se vuelve de solo lectura.

    # propiedad saldo (Lectura y Escritura controlada)
    @property
    def saldo(self):
        """Getter: Retorna el saldo actual."""
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        """Setter: Valida que el saldo no sea negativo antes de asignar."""
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(nuevo_saldo)

    # métodos de operación

    def depositar(self, cantidad):
        """Suma dinero al saldo si la cantidad es positiva."""
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """Resta dinero del saldo si hay fondos suficientes y la cantidad es válida."""
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False

# prueba de la clase CuentaBancaria
if __name__ == "__main__":
    try:
        # Crear la cuenta
        mi_ahorro = CuentaBancaria("Aly Santiago Cano", 500.0)
        print(f"Titular: {mi_ahorro.titular}")
        print(f"Saldo inicial: ${mi_ahorro.saldo}")

        # Operaciones exitosas
        if mi_ahorro.depositar(200):
            print(f"Deposito exitoso. Nuevo saldo: ${mi_ahorro.saldo}")
        
        if mi_ahorro.retirar(100):
            print(f"Retiro exitoso. Nuevo saldo: ${mi_ahorro.saldo}")

        # Intento de saldo negativo (Esto disparará el ValueError)
        print("\nProbando validacion de saldo negativo...")
        mi_ahorro.saldo = -10
        
    except ValueError as e:
        print(f"Error detectado: {e}")