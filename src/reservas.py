
def main():
    import random

    # Diccionario con las distancias entre las ciudades
    distancias = {
        ('Medellín', 'Bogotá'): 240,
        ('Medellín', 'Cartagena'): 461,
        ('Bogotá', 'Cartagena'): 657,
    }

    # Función para obtener la distancia entre dos ciudades
    def obtener_distancia(origen, destino):
        if (origen, destino) in distancias:
            return distancias[(origen, destino)]
        else:
            return distancias[(destino, origen)]

    # Función para calcular el precio del boleto
    def calcular_precio(distancia, dia_semana):
        if distancia < 400:
            if dia_semana in ['lunes', 'martes', 'miércoles', 'jueves']:
                return 79900
            else:
                return 119900
        else:
            if dia_semana in ['lunes', 'martes', 'miércoles', 'jueves']:
                return 156900
            else:
                return 213000

    # Función principal del sistema de reservas
    def sistema_reservas():
        # Información del usuario
        titulo = input("Ingrese su título (Sr. o Sra.): ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        
        # Saludo personalizado
        print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!")
        
        # Selección de vuelo
        print("Seleccione su ciudad de origen:")
        ciudades = ["Medellín", "Bogotá", "Cartagena"]
        for i, ciudad in enumerate(ciudades):
            print(f"{i+1}. {ciudad}")
        origen = ciudades[int(input("Ingrese el número de su ciudad de origen: ")) - 1]

        for i, ciudad in enumerate(ciudades):
            if ciudad != origen:
                print(f"{i+1}. {ciudad}")
        destino = ciudades[int(input("Ingrese el número de su ciudad de destino: ")) - 1]
        
        if origen not in ciudades or destino not in ciudades or origen == destino:
            print("Error: Origen y destino inválidos.")
            return
        
        dia_semana = input("Ingrese el día de la semana en que desea viajar (por ejemplo, lunes): ")
        dia_mes = int(input("Ingrese el día del mes en que desea viajar (1-30): "))
        
        # Calcular la distancia y el precio del boleto
        distancia = obtener_distancia(origen, destino)
        precio = calcular_precio(distancia, dia_semana)
        
        # Asignación de asiento
        print("Seleccione su preferencia de asiento:")
        print("1. Pasillo")
        print("2. Ventana")
        print("3. Sin preferencia")
        
        preferencia_asiento = int(input("Ingrese el número de su preferencia de asiento: "))
        
        if preferencia_asiento == 1:
            letra_asiento = "C"
        elif preferencia_asiento == 2:
            letra_asiento = "A"
        else:
            letra_asiento = "B"
        
        numero_asiento = random.randint(1, 29)
        asiento = f"{numero_asiento}{letra_asiento}"
        
        numero_asiento = random.randint(1, 29)
        asiento = f"{numero_asiento}{letra_asiento}"
        
        # Salida con la información del vuelo
        print("Resumen de su reserva")
        print(f"Nombre completo: {titulo} {nombre} {apellido}")
        print(f"Origen: {origen}")
        print(f"Destino: {destino}")
        print(f"Fecha de vuelo: {dia_semana}, {dia_mes}")
        print(f"Precio del boleto: ${precio:,}")
        print(f"Asiento asignado: {asiento}")

    # Llamada a la función principal
    if __name__ == "__main__":
        sistema_reservas()

if __name__ == "__main__":
    main()
