
def main():

    # Desintegración orbital de un satelite 

    def simulacion_desintegracion_orbital(altitud_inicial, coeficiente_arrastre, altitud_minima_seguridad):
        altitud_actual = altitud_inicial
        orbitas_completadas = 0

        # Bucle que simula cada órbita del satélite
        while altitud_actual > altitud_minima_seguridad:
            # Calcular la pérdida de altitud en cada órbita
            altitud_perdida = coeficiente_arrastre * altitud_actual
            
            # Restar la pérdida de altitud a la altitud actual
            altitud_actual -= altitud_perdida
            orbitas_completadas += 1
            
            # Incrementar ligeramente el coeficiente de arrastre
            coeficiente_arrastre += 0.0001
            
            # Si la pérdida de altitud es muy pequeña, se considera que el satélite se estabiliza
            if altitud_perdida < 0.01:
                print(f"El satélite se ha estabilizado en una órbita baja.")
                print(f"Altitud final: {altitud_actual:.2f} km")
                print(f"Órbitas completadas: {orbitas_completadas}")
                return

        # Si el bucle termina, el satélite ha reingresado a la atmósfera
        print("El satélite ha reingresado en la atmósfera terrestre y se ha desintegrado.")
        print(f"Órbitas completadas: {orbitas_completadas}")

    if __name__ == "__main__":
        print("Simulación de Desintegración Orbital de un Satélite")

        # Solicitar los datos de entrada al usuario
        altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en km): "))
        coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (por ejemplo, 0.01): "))
        altitud_minima_seguridad = float(input("Ingrese la altitud mínima de seguridad (en km): "))
        
        # Ejecutar la simulación
        simulacion_desintegracion_orbital(altitud_inicial, coeficiente_arrastre, altitud_minima_seguridad)

if __name__ == "__main__":
    main()
