class Nodo:
    def __init__(self, cedula, nombre, habitacion):
        self.cedula = cedula
        self.nombre = nombre
        self.habitacion = habitacion
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Agregar al final (orden de llegada)
    def agregar(self, cedula, nombre, habitacion):
        nuevo = Nodo(cedula, nombre, habitacion)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Eliminar por cédula
    def eliminar(self, cedula):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.cedula == cedula:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return actual.habitacion
            anterior = actual
            actual = actual.siguiente
        return None

    # Buscar individual
    def buscar(self, cedula):
        actual = self.cabeza
        while actual:
            if actual.cedula == cedula:
                return actual
            actual = actual.siguiente
        return None

    # Mostrar por orden de llegada
    def mostrar_por_llegada(self):
        actual = self.cabeza
        while actual:
            print("Cédula:", actual.cedula)
            print("Nombre:", actual.nombre)
            print("Habitación:", actual.habitacion)
            print("-------------------")
            actual = actual.siguiente

    # Mostrar ordenado por cédula
    def mostrar_por_cedula(self):
        lista_aux = []
        actual = self.cabeza

        while actual:
            lista_aux.append(actual)
            actual = actual.siguiente

        lista_aux.sort(key=lambda x: x.cedula)

        for h in lista_aux:
            print("Cédula:", h.cedula)
            print("Nombre:", h.nombre)
            print("Habitación:", h.habitacion)
            print("-------------------")

    # Mostrar habitaciones ocupadas
    def habitaciones_ocupadas(self):
        ocupadas = []
        actual = self.cabeza
        while actual:
            ocupadas.append(actual.habitacion)
            actual = actual.siguiente
        return ocupadas


# ===== PROGRAMA PRINCIPAL =====

lista = ListaEnlazada()
habitaciones_disponibles = set(range(1, 11))

while True:
    print("\n1. Agregar huésped")
    print("2. Retirar huésped")
    print("3. Consulta individual")
    print("4. Consulta total por orden de llegada")
    print("5. Consulta total por cédula")
    print("6. Ver habitaciones disponibles")
    print("7. Ver habitaciones ocupadas")
    print("8. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":
        cedula = input("Ingrese cédula: ")
        nombre = input("Ingrese nombre: ")
        habitacion = int(input("Ingrese habitación: "))

        if habitacion in habitaciones_disponibles:
            lista.agregar(cedula, nombre, habitacion)
            habitaciones_disponibles.remove(habitacion)
            print("Habitación asignada correctamente.")
        else:
            print("Habitación no disponible.")

    elif opcion == "2":
        cedula = input("Ingrese cédula del huésped: ")
        habitacion = lista.eliminar(cedula)

        if habitacion is not None:
            habitaciones_disponibles.add(habitacion)
            print("Huésped retirado correctamente.")
        else:
            print("Huésped no encontrado.")

    elif opcion == "3":
        cedula = input("Ingrese cédula: ")
        huesped = lista.buscar(cedula)

        if huesped:
            print("Cédula:", huesped.cedula)
            print("Nombre:", huesped.nombre)
            print("Habitación:", huesped.habitacion)
        else:
            print("No encontrado.")

    elif opcion == "4":
        print("\n--- Lista por orden de llegada ---")
        lista.mostrar_por_llegada()

    elif opcion == "5":
        print("\n--- Lista ordenada por cédula ---")
        lista.mostrar_por_cedula()

    elif opcion == "6":
        print("Habitaciones disponibles:", sorted(habitaciones_disponibles))

    elif opcion == "7":
        ocupadas = lista.habitaciones_ocupadas()
        print("Habitaciones ocupadas:", ocupadas)

    elif opcion == "8":
        break

    else:
        print("Opción inválida.")


        


